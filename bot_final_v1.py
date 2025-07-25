# -----------------------------------
# 🔌 Conexión WebSocket y envío señal
# -----------------------------------
import os
import websocket
import threading
import json
import time

# Cargar variables de entorno
WS_ENDPOINT = os.getenv("WS_ENDPOINT", "ws://localhost:3000")
BOT_MODE = os.getenv("BOT_MODE", "PRODUCTION")
DEBUG_MODE = os.getenv("DEBUG_MODE", "FALSE")

# Función para enviar señal por WebSocket
def send_signal(message):
    try:
        ws = websocket.create_connection(WS_ENDPOINT)
        ws.send(json.dumps(message))
        ws.close()
        if DEBUG_MODE.upper() == "TRUE":
            print(f"[DEBUG] Señal enviada: {message}")
    except Exception as e:
        print(f"[ERROR] Falló conexión WebSocket: {e}")

# Función para generar señal con parámetros
def generar_senal(tipo="BUY", fuerza=85, activo="EURUSD", tiempo="M1"):
    mensaje = {
        "tipo": tipo,
        "fuerza": fuerza,
        "activo": activo,
        "tiempo": tiempo,
        "modo": BOT_MODE,
        "timestamp": time.time()
    }
    send_signal(mensaje)

# Activar señal si el bot está en modo TRADING
if BOT_MODE.upper() == "TRADING":
    threading.Thread(target=generar_senal).start()
if __name__ == "__main__":
    generar_senal(tipo="SELL", fuerza=92, activo="GBPUSD", tiempo="M5")