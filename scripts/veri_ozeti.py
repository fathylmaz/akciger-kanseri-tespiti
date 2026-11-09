"""Yerel veri klasörünün sadece genel dosya sayısı/uzantı özetini yazdırır."""
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'data'
IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.webp', '.bmp', '.tif', '.tiff', '.dcm'}


def main():
    files = [p for p in ROOT.rglob('*') if p.is_file() and p.name != 'README.md']
    images = [p for p in files if p.suffix.lower() in IMAGE_EXTS]
    print(f'Veri klasörü: {ROOT}')
    print(f'Toplam dosya: {len(files)}; olası görüntü: {len(images)}')
    print('Uzantılar:', dict(sorted(Counter(p.suffix.lower() for p in images).items())))
    print('Üst dizinlere göre:',dict(sorted(Counter(p.relative_to(ROOT).parts[0] for p in images).items())))
    print('Not: Bu özet hasta düzeyinde ayrımı ya da veri kalitesini doğrulamaz.')


if __name__ == '__main__':
    main()
