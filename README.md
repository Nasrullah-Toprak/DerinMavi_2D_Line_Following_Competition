# Derin Mavi Line Follower Challenge

Derin Mavi Robotik Takımı'nın çizgi izleme yarışmasına hoş geldiniz! Bu yarışmada 2D simülasyon ortamında çizgi izleyen bir robot algoritması geliştireceksiniz.

## Yarışma Kuralları

1. **Bu repoyu forklayın** - Kendi GitHub hesabınıza kopyalayın
2. **`solution.py` dosyasını düzenleyin** - Algoritmanızı geliştirin
3. **Test edin** - Lokal ortamda `python main.py` ile test edin
4. **Push yapın** - Çözümünüzü commit ve push edin
5. Otomatik değerlendirme yapılır ve sonuçlar leaderboard'a eklenir!

## Gereksinimler
- Python 3.x
- Gerekli kütüphaneler:
```bash
pip install pygame numpy opencv-python
```

## Otomatik Değerlendirme Süreci

1. `solution.py` dosyasını değiştirip push yaptığınızda GitHub Actions otomatik olarak tetiklenir
2. Çözümünüz headless modda test edilir
3. Başarılı olursanız süreniz leaderboard'a eklenir
4. En iyi süreniz kaydedilir

## 📁 Dosya Yapısı

├── solution.py          # 👈 SADECE BU DOSYAYI DÜZENLEYİN
├── main.py              # Görsel simülatör (değiştirmeyin)
├── track.png            # Yarış pisti
├── racing_car.png       # Robot görseli
├── update_leaderboard.py # Leaderboard güncelleyici
└── README.md 


## Önemli Notlar

- **Sadece `solution.py` dosyasını düzenleyin!** Diğer dosyaları değiştirmeniz durumunda değerlendirme başarısız olabilir.
- Çözümünüz **5 dk** içinde turu tamamlamalıdır, aksi halde timeout olur.
- Robot pistten çıkarsa veya takılırsa değerlendirme başarısız olur.


