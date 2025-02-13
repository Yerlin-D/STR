from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import json

app = FastAPI()
datos = []  # Almacenará los signos vitales en memoria

@app.get("/")
def home():
    return {"message": "Monitor de Signos Vitales en tiempo real está funcionando"}

@app.get("/historial")
def obtener_historial():
    return {"historial": datos}

# WebSocket para recibir datos del sensor
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Cliente conectado")

    try:
        while True:
            # Recibir datos del sensor
            data = await websocket.receive_text()
            dato = json.loads(data)

            # Determinar si hay alerta
            alerta = detectar_alerta(dato)

            # Guardar los datos con estado de alerta
            dato["estado"] = "alerta" if alerta else "normal"
            datos.append(dato)

            print(f"Recibido: {dato}")

            # Enviar respuesta con alerta o normal
            await websocket.send_text(json.dumps(dato))

    except WebSocketDisconnect:
        print(" Cliente desconectado")

# Función para detectar alertas
def detectar_alerta(dato):
    # Valores normales de referencia
    temp_normal = (36.0, 37.5)
    ritmo_normal = (60, 100)
    presion_normal = (90, 140, 60, 90)  # (Sistólica min, Sistólica max, Diastólica min, Diastólica max)

    sistolica, diastolica = map(int, dato["tension_arterial"].split("/"))

    if not (temp_normal[0] <= dato["temperatura"] <= temp_normal[1]):
        return True
    if not (ritmo_normal[0] <= dato["ritmo_cardiaco"] <= ritmo_normal[1]):
        return True
    if not (presion_normal[0] <= sistolica <= presion_normal[1] and presion_normal[2] <= diastolica <= presion_normal[3]):
        return True

    return False
