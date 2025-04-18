import asyncio
import websockets
import json
import random

async def enviar_datos():
    uri = "ws://127.0.0.1:8000/ws"

    try:
        async with websockets.connect(uri) as websocket:
            while True:
                try:
                    datos = {
                        "ritmo_cardiaco": random.randint(50, 120),
                        "temperatura": round(random.uniform(35.0, 40.0), 1),
                        "tension_arterial": f"{random.randint(90, 160)}/{random.randint(60, 100)}"
                    }

                    await websocket.send(json.dumps(datos))
                    print(f" Enviado: {datos}")

                    await asyncio.sleep(2)

                except websockets.exceptions.ConnectionClosed:
                    print("Conexión cerrada con el servidor. Intentando reconectar...")
                    break
                except Exception as e:
                    print(f"Error inesperado en el sensor: {e}")

    except (ConnectionRefusedError, OSError):
        print("No se pudo conectar con el servidor. Asegúrate de que esté en ejecución.")
    except KeyboardInterrupt:
        print("Ejecución del sensor detenida manualmente.")

asyncio.run(enviar_datos())
