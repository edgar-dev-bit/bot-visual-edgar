import os
import sys

def check_env_var(name, required=True):
    value = os.getenv(name)
    if required and not value:
        print(f"⚠️ FALTA: La variable '{name}' no está definida.")
        return False
    else:
        print(f"✅ {name} = {value}")
        return True

def check_config():
    print("\n🔍 Verificando configuración del entorno...\n")
    
    config_ok = True

    # Comprobación general
    config_ok &= check_env_var("BOT_MODE")
    config_ok &= check_env_var("TIMEFRAME")
    config_ok &= check_env_var("DEBUG_MODE")

    # Módulo de señales técnicas
    if os.getenv("BOT_MODE") == "TRADING":
        config_ok &= check_env_var("SIGNAL_STRENGTH_MIN")
        config_ok &= check_env_var("ASSET_FILTER")
        config_ok &= check_env_var("MAX_SIGNALS", required=False)

    # Módulo visual OCR
    if os.getenv("OCR_ACTIVE") == "TRUE":
        config_ok &= check_env_var("OCR_TESSERACT_PATH")
        config_ok &= check_env_var("INDICATORS_ACTIVE", required=False)

    # WebSocket
    config_ok &= check_env_var("WS_ENDPOINT")
    config_ok &= check_env_var("WS_TOKEN")

    if not config_ok:
        print("\n🚫 Error: Hay variables faltantes o inválidas.\n")
        sys.exit(1)

    print("\n🟢 Todo OK. Módulos listos para ejecutarse.\n")

    return True