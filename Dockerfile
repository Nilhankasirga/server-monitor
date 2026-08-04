# 1. Taban İmaj: İçinde Python ve pip hazır kurulu olan resmi Linux ortamı
FROM python:3.10-slim

# 2. Çalışma Dizini: Konteynırın içinde hangi klasörde çalışacağız?
WORKDIR /app

# 3. Bağımlılıkları Kopyala: Kendi bilgisayarımızdaki requirements.txt'yi konteynırın içine atıyoruz
COPY requirements.txt .

# 4. Yükleme Yap: Konteynırın İÇİNDEKİ Python ile paketleri yüklüyoruz (Bilgisayarımızda Python olmasa bile!)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Kodları Kopyala: main.py dosyamızı konteynırın içine kopyalıyoruz
COPY main.py .

# 6. Başlatma Komutu: Uygulamayı konteynır içinde başlatıyoruz
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]