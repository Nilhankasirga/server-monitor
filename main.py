import logging
import random
from fastapi import FastAPI
import psutil  # Yeni kütüphanemizi içe aktardık

app = FastAPI()

logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


@app.get("/status")
def get_status():
    temp = random.randint(30, 85)
    if temp > 75:
        logging.warning(
            f"YÜKSEK SICAKLIK: Sunucu sıcaklığı {temp}°C seviyesine ulaştı!"
        )
    else:
        logging.info(f"Normal çalışma: Sıcaklık {temp}°C.")

    return {"status": "running", "temperature": temp}


# --- YENİ EKLENEN KISIM ---
@app.get("/metrics")
def get_metrics():
    # CPU ve Bellek kullanım yüzdelerini alıyoruz
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent

    # Yüksek kaynak kullanımı varsa log yazalım
    if cpu_usage > 80 or memory_usage > 80:
        logging.warning(
            f"YÜKSEK KAYNAK KULLANIMI: CPU %{cpu_usage}, RAM %{memory_usage}"
        )
    else:
        logging.info(
            f"Kaynak Kullanımı Normal: CPU %{cpu_usage}, RAM %{memory_usage}"
        )

    return {
        "cpu_usage_percent": cpu_usage,
        "memory_usage_percent": memory_usage,
    }