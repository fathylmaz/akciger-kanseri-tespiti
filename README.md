# Akciğer Kanseri Tespiti — Üniversite Projesi

Bu depo, **üniversitede ekip olarak geliştirilip sunulmuş orijinal projenin** GitHub'da düzenli paylaşımı için hazırlanmıştır. Ayrı bir proje veya sıfırdan geliştirilen yeni sürüm değildir.

**Orijinal unsurlar korundu:** Flask uygulamasının temel işleyişi, HTML arayüz tasarımı, CNN modeline giriş ön işlemi (224x224 RGB, /255), üç sınıf sıralaması, örnek görüntüler ve sunum PDF'i. Sadece yayın için gerekli dosyalar ve temel güvenlik/hata kontrolü eklendi. Yazım hatası `Bengin` → `Benign` düzeltildi.

## İçerik

- `app.py`: Flask tahmin sunucusu
- `templates/index.html`: Üniversite projesindeki **değiştirilmemiş** arayüz
- `static/`: Üniversite projesindeki iki örnek görüntü
- `AkciğerKanserTeshisi (1).pdf`: Üniversite sunumu; proje ekibi bilgileri düzeltilmiş, teknik içerik korunmuştur.
- `data/`: büyük veri klasörü için yerel alan; içerik otomatik olarak Git'e eklenmez
- `MODEL_DOSYALARI.md`: iki orijinal model dosyasının ayırt edici özetleri

## Eğitilmiş CNN Modeli

Projenin orijinal eğitilmiş CNN modeli
`akcigerkansermodel.h5` dosyasıdır.

- Model türü: Convolutional Neural Network (CNN)
- Giriş boyutu: 224 × 224 × 3
- Çıkış sınıfları: Normal, Benign, Malignant
- Toplam parametre: 11.169.347
- Model formatı: Keras H5
- Dosya boyutu: 127,9 MiB

Model dosyası GitHub Releases bölümünde
v1.0.0 sürümüyle paylaşılmak üzere hazırlanmıştır.

Release yayımlandıktan sonra modeli indirip
`app.py` dosyasıyla aynı klasöre yerleştirin.

Model TensorFlow 2.21.0 ile başarıyla yüklenmiş
ve üç örnek görüntü üzerinde Flask arayüzünden
tahmin ürettiği doğrulanmıştır.

Model yalnızca akademik ve eğitim amaçlıdır.
Klinik tanı için doğrulanmamıştır.

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

## Yayın ve doğrulama kontrol listesi

- [x] Fatih Yılmaz ve Gamze Özateş'in ortak proje ve sunum paylaşımı için mutabakatı alındı.
- [x] Veri setinin kaynağı, DOI bilgisi ve kaynakta belirtilen lisansı README'ye eklendi.
- [x] Yerel arşivdeki 1.097 JPG görüntüsü ve üç sınıfın dosya sayıları kontrol edildi.
- [x] Orijinal CNN modeli TensorFlow 2.21.0 ile yüklendi; Flask arayüzünde üç örnek tahmin test edildi.
- [x] Sunumdaki metriklerin bağımsız olarak yeniden doğrulanmadığı ve hasta düzeyinde veri ayrımının doğrulanamadığı açıklandı.
- [x] Büyük veri seti Git deposuna eklenmedi; veri setinin resmî kaynak bağlantısı verildi.
- [x] Eğitilmiş modelin SHA-256 değeri doğrulandı ve `v1.0.0` GitHub Release taslağına yüklendi.
- [ ] `v1.0.0` Release yayımlandı ve modelin indirme bağlantısı test edildi.
- [x] Depodaki iki örnek PNG'de görünür doğrudan kimlik bilgileri ve metin/EXIF meta verisi için temel kontrol yapıldı; veri setinin kaynak sayfasındaki CC BY 4.0 lisansı incelendi. Bu, kapsamlı kimliksizleştirme veya dosya kökeni doğrulaması değildir.

*Not:* Kontrol listesindeki tamamlanan maddeler teknik/operasyonel kontrolleri ifade eder; klinik geçerlilik veya kapsamlı veri güvenliği denetimi anlamına gelmez.

## Proje Ekibi

Bu proje, üniversite kapsamında Fatih Yılmaz ve
Gamze Özateş tarafından birlikte geliştirilmiş
ve sunulmuştur.

### Ekip Üyeleri

- Fatih Yılmaz
- Gamze Özateş

Projenin orijinal akademik sunumu, ekip bilgileri
güncellenmiş şekilde depo içerisinde bulunmaktadır.
