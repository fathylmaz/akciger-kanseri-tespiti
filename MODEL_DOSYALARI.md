# Orijinal model dosyaları

Orijinal ZIP içerisinde iki farklı `.h5` dosyası mevcuttur. Dosyalar aynı model olarak kabul edilmemelidir.

- `akcigerkansermodel.h5` — Flask uygulamasının kullandığı orijinal model. Yerel proje köküne bu dosyayı koyun.
- `lung_cancer_classifier.h5` — Ayrı ağırlıklara sahip ikinci dosya; hangi deneyle ilişkili olduğu doğrulanmalıdır.

## SHA-256

- `akcigerkansermodel.h5`: `0bd2e73e2ac311cbb5d0b058b00a8834e7a85aa10ef7b3decba7bc92189a49ac`
- `lung_cancer_classifier.h5`: `f28804adfc8ad079e6207f1c11d469efb0f29bef0c92a40f4673e6bb59c8706c`

Boyutları GitHub'ın standart tek dosya limitini aştığından varsayılan `.gitignore` bunları dışarıda bırakır. Yayın izni ve model seçimi netleştirilirse Git LFS veya GitHub Releases üzerinden dağıtılabilir.
