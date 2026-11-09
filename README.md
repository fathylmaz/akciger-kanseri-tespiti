# Akciğer Kanseri Tespiti — Üniversite Projesi

Bu depo, **üniversitede ekip olarak geliştirilip sunulmuş orijinal projenin** GitHub'da düzenli paylaşımı için hazırlanmıştır. Ayrı bir proje veya sıfırdan geliştirilen yeni sürüm değildir.

**Orijinal unsurlar korundu:** Flask uygulamasının temel işleyişi, HTML arayüz tasarımı, CNN modeline giriş ön işlemi (224x224 RGB, /255), üç sınıf sıralaması, örnek görüntüler ve sunum PDF'i. Sadece yayın için gerekli dosyalar ve temel güvenlik/hata kontrolü eklendi. Yazım hatası `Bengin` → `Benign` düzeltildi.

## İçerik

- `app.py`: Flask tahmin sunucusu
- `templates/index.html`: Üniversite projesindeki **değiştirilmemiş** arayüz
- `static/`: Üniversite projesindeki iki örnek görüntü
- `AkciğerKanserTeshisi (1).pdf`: Üniversite **orijinal sunumu, değiştirilmeden**
- `data/`: büyük veri klasörü için yerel alan; içerik otomatik olarak Git'e eklenmez
- `MODEL_DOSYALARI.md`: iki orijinal model dosyasının ayırt edici özetleri

## Başlatma (Windows, PowerShell)

1. Orijinal ZIP dosyanızdan `akcigerkansermodel.h5` dosyasını `app.py` ile aynı klasöre kopyalayın.
2. Terminali proje klasöründe açın, uygun Python sürümüyle sanal ortam oluşturun:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

3. `http://127.0.0.1:5000` adresinde uygulamayı açın.

**Yerel model doğrulaması:** Orijinal CNN modeli Python 3.13 ve TensorFlow 2.21.0 ortamında başarıyla yüklenmiştir. Modelin giriş boyutu (224, 224, 3), çıkış boyutu ise 3 sınıftır. Flask uygulamasında Normal, Benign ve Malignant sınıflarından seçilen birer görüntü doğru sınıflandırılmıştır (3/3). Bu sınırlı çalışma testi, modelin genel doğruluğunu veya klinik güvenilirliğini kanıtlamaz.

## Veri klasörü

Büyük görüntü klasörünüzü `data/` içine aynen kopyalayın. Dosya isimlerini veya sınıflama klasörlerini değiştirmeyin. Sonra:

```powershell
python scripts/veri_ozeti.py
```

Kullanılan veri setinin lisans/atıf ve kişisel veri şartlarını kontrol etmeden tüm görüntüleri herkese açık GitHub deposuna yüklemeyin. Tam veri gerekli ama büyükse resmî veri kaynağına link verilebilir; haklar elveriyorsa Git LFS de değerlendirilebilir.

### Kullanılan Veri Seti

Proje kapsamında IQ-OTH/NCCD Lung Cancer Dataset
kullanılmıştır.

Kaynak: https://data.mendeley.com/datasets/bhmdr45bh2/4

Veri seti DOI: 10.17632/bhmdr45bh2.4

Lisans: Creative Commons Attribution 4.0 (CC BY 4.0)

Projede kullanılan görüntülerin dağılımı:

| Sınıf | Görüntü Sayısı |
|---|---:|
| Normal | 416 |
| Benign | 120 |
| Malignant | 561 |
| **Toplam** | **1097** |

Veri seti orijinal klasör isimleri korunarak
kullanılmıştır. Büyük görüntü dosyaları GitHub
deposuna eklenmemiştir. Veri setine orijinal
kaynağından erişilebilir.

Bu sayılar yerel arşivdeki görüntü sayımlarına
dayanmaktadır. Hasta bazında bağımsız test
ayrımı doğrulanmamıştır.

## Akademik sonuç ve sınırlar

Üniversite sunumunda CNN sınıflandırma performansı bildirilmiştir. Bu sonuçlar **eski deney sonuçlarıdır**; burada yeniden eğitim veya bağımsız test yapılmadı. Sunumdaki doğruluk sayıları arasında farklılıklar görüldüğü ve hasta bazında test ayrımı doğrulanamadığı için klinik performans iddiasında bulunulmamalıdır. Bu araç **tıbbi tanı amacıyla kullanılamaz**.

## Paylaşmadan önce

- [ ] Ekipteki katkı sahipleri ve sunumun yayımlanması için mutabakat
- [ ] Veri setinin kaynağı, izinleri, lisansı ve kimliksizliği doğrulandı
- [x] Model yükleme ve örnek tahmin yerelde test edildi
- [ ] Eski sunumdaki metriklerin kaynağı ve sınırlılıkları açıkça belirtildi
- [ ] Büyük model/veri dosyaları için yayımlama yolu belirlendi

## Proje Ekibi

Bu proje, üniversite kapsamında Fatih Yılmaz ve
Gamze Özateş tarafından birlikte geliştirilmiş
ve sunulmuştur.

### Ekip Üyeleri

- Fatih Yılmaz
- Gamze Özateş

Projenin orijinal akademik sunumu, ekip bilgileri
güncellenmiş şekilde depo içerisinde bulunmaktadır.
