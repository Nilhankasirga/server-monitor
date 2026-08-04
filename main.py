import logging
import random
from fastapi import FastAPI

# Log yapılandırması: Logları hem terminale hem de 'server.log' dosyasına yazdıracağız
logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

app = FastAPI()


@app.get("/status")
def get_server_status():
    temperature = random.randint(35, 85)

    if temperature > 75:
        status_message = "CRITICAL: Server is overheating!"
        # Aşırı ısınma durumunda 'WARNING' seviyesinde log atıyoruz
        logging.warning(
            f"Sıcaklık Yüksek! Ölçülen Değer: {temperature}°C - Durum: KRİTİK"
        )
    else:
        status_message = "OK: Server temperature is normal."
        # Normal durumda 'INFO' seviyesinde log atıyoruz
        logging.info(
            f"Sıcaklık Normal. Ölçülen Değer: {temperature}°C - Durum: STABİL"
        )

    return {"cpu_temperature": temperature, "status": status_message}