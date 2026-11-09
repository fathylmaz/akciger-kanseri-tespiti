from pathlib import Path

from flask import Flask, request, jsonify, render_template
from PIL import Image, UnidentifiedImageError
import numpy as np
import tensorflow as tf

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024  # En fazla 8 MB

# Üniversite projesindeki model, sınıf sırası ve ön işleme korunmuştur.
MODEL_PATH = Path(__file__).resolve().parent / 'akcigerkansermodel.h5'
model = tf.keras.models.load_model(str(MODEL_PATH), compile=False)
classes = ['Normal', 'Benign', 'Malignant']
ALLOWED_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.webp'}
Image.MAX_IMAGE_PIXELS = 20_000_000


@app.route('/')
def home():
    return render_template('index.html')


@app.errorhandler(413)
def payload_too_large(error):
    return jsonify({'error': 'Dosya 8 MB boyut sınırını aşıyor.'}), 413


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'Dosya bulunamadı.'}), 400

    uploaded = request.files['file']
    if not uploaded.filename:
        return jsonify({'error': 'Lütfen bir görüntü seçin.'}), 400
    if Path(uploaded.filename).suffix.lower() not in ALLOWED_EXTENSIONS:
        return jsonify({'error': 'PNG, JPG, JPEG veya WebP görüntüsü yükleyin.'}), 400

    try:
        # Orijinal ön işleme: RGB -> 224x224 -> /255 -> batch boyutu
        with Image.open(uploaded.stream) as src_img:
            img = src_img.convert('RGB')
        img = img.resize((224, 224))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        prediction = model.predict(img_array, verbose=0)
        pred_class = classes[int(np.argmax(prediction))]
        return jsonify({'prediction': pred_class})
    except (UnidentifiedImageError, OSError, ValueError, Image.DecompressionBombError):
        return jsonify({'error': 'Görüntü dosyası geçerli değil veya açılamıyor.'}), 400
    except Exception:
        app.logger.exception('Model tahmini sırasında hata')
        return jsonify({'error': 'Tahmin sırasında bir sunucu hatası oluştu.'}), 500


if __name__ == '__main__':
    app.run(debug=False)
