import os

LOG_FILE = "server.log"
CRITICAL_THRESHOLD = 3


def analyze_logs():
    if not os.path.exists(LOG_FILE):
        print(
            f"❌ '{LOG_FILE}' bulunamadı. Lütfen önce sunucuya istek atın."
        )
        return

    warning_count = 0
    info_count = 0
    high_resource_warnings = 0  # Yeni eklediğimiz kaynak uyarısı sayacı

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            if "WARNING" in line:
                warning_count += 1
                # Eğer uyarı kaynak kullanımıyla ilgiliyse bu sayacı artır
                if "KAYNAK KULLANIMI" in line:
                    high_resource_warnings += 1
            elif "INFO" in line:
                info_count += 1

    print("📊 --- GELİŞMİŞ LOG ANALİZ RAPORU ---")
    print(f"✅ Normal Çalışma (INFO) Sayısı    : {info_count}")
    print(f"⚠️ Toplam Kritik Uyarı (WARNING)    : {warning_count}")
    print(f"🔥 Yüksek Kaynak Kullanımı Uyarısı : {high_resource_warnings}")
    print(f"📈 Toplam İnceleyen Satır Sayısı    : {len(lines)}")
    print("-" * 35)

    if warning_count > CRITICAL_THRESHOLD:
        print("🚨 ALARM: Eşik değer aşıldı! Sunucuda inceleme yapmalısınız.")
    else:
        print("🟢 Sistem Kararlı: Sıcaklık ve kaynak kullanımı normal.")


if __name__ == "__main__":
    analyze_logs()