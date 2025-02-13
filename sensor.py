import asyncio
import websockets
import json
import random

async def enviar_datos():
    uri = "ws://127.0.0.1:8000/ws"  # Dirección WebSocket del servidor
    async with websockets.connect(uri) as websocket:
        while True:
            # Simulación de signos vitales
            datos = {
                "ritmo_cardiaco": random.randint(50, 120),  # Frecuencia cardíaca (bpm)
                "temperatura": round(random.uniform(35.0, 40.0), 1),  # Temperatura en °C
                "tension_arterial": f"{random.randint(90, 160)}/{random.randint(60, 100)}"  # Presión arterial (sistólica/diastólica)
            }

            # Enviar datos al servidor
            await websocket.send(json.dumps(datos))
            print(f" Enviado: {datos}")

            await asyncio.sleep(2)  # Enviar datos cada 2 segundos

# Ejecutar el cliente WebSocket
asyncio.run(enviar_datos())
