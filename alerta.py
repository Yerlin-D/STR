import time
from server import datos

def verificar_alertas():
    try:
        while True:
            try:
                alertas = [d for d in datos if d.get("estado") == "alerta"]

                if alertas:
                    print("⚠️ ALERTA: Se detectaron valores anormales:")
                    for alerta in alertas:
                        print(f"   - Ritmo Cardíaco: {alerta['ritmo_cardiaco']} bpm")
                        print(f"   - Temperatura: {alerta['temperatura']}°C")
                        print(f"   - Tensión Arterial: {alerta['tension_arterial']}")
                        print("-------------------------------------------------")

                time.sleep(5)

            except IndexError:
                print("No hay datos disponibles aún.")
                time.sleep(5)
            except KeyError as e:
                print(f"Error de clave en los datos: {e}")

    except KeyboardInterrupt:
        print("Ejecución del monitor de alertas detenida manualmente.")
    except Exception as e:
        print(f"Error inesperado en el sistema de alertas: {e}")

verificar_alertas()
