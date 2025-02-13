import time
from server import datos

def verificar_alertas():
    while True:
        alertas = [d for d in datos if d["estado"] == "alerta"]
        
        if alertas:
            print("⚠️ ALERTA: Se detectaron valores anormales:")
            for alerta in alertas:
                print(f"   - Ritmo Cardíaco: {alerta['ritmo_cardiaco']} bpm")
                print(f"   - Temperatura: {alerta['temperatura']}°C")
                print(f"   - Tensión Arterial: {alerta['tension_arterial']}")
                print("-------------------------------------------------")
        
        time.sleep(5)  # Verifica cada 5 segundos

verificar_alertas()
