import os

LOG_FILE = "server.log"
CRITICAL_THRESHOLD = 3  # İzin verilen maksimum kritik hata sayısı


def analyze_logs():
    if not os.path.exists(LOG_FILE):
        print(
            f"❌ '{LOG_FILE}' bulunamadı. Lütfen önce sunucuya birkaç istek atın."
        )
        return

    warning_count = 0
    info_count = 0

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            if "WARNING" in line:
                warning_count += 1
            elif "INFO" in line:
                info_count += 1

    print("📊 --- LOG ANALİZ RAPORU ---")
    print(f"✅ Normal Çalışma (INFO) Sayısı : {info_count}")
    print(f"⚠️ Kritik Uyarı (WARNING) Sayısı : {warning_count}")
    print(f"📈 Toplam İnceleyen Satır Sayısı  : {len(lines)}")
    print("-" * 30)

    # Neden ekledik? Eşik değer kontrolü yapıp otomatik alarm üretmek için
    if warning_count > CRITICAL_THRESHOLD:
        print("🚨 ALARM: Sunucuda çok fazla sıcaklık artışı tespit edildi!")
        print(
            f"   Kritik Sayı: {warning_count} (Eşik Değer: {CRITICAL_THRESHOLD})"
        )
        print("   Lütfen soğutma sistemlerini kontrol edin.")
    else:
        print("🟢 Sistem Kararlı: Kritik hata eşik değerin altında.")


if __name__ == "__main__":
    analyze_logs()