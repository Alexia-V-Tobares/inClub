from flask import Flask, request, jsonify, send_from_directory
from funciones import puede_entrar, archivar_asistentes, cargar_asistentes

app = Flask(__name__)


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/api/asistentes", methods=["GET"])
def listar_asistentes():
    asistentes = cargar_asistentes()
    return jsonify({"total": len(asistentes), "asistentes": asistentes})


@app.route("/api/asistentes", methods=["POST"])
def registrar_asistente():
    data = request.get_json(silent=True) or {}
    nombre = data.get("nombre", "").strip()
    edad = data.get("edad")
    tiene_entrada = data.get("tiene_entrada", "").strip().lower()

    if not nombre or edad is None or tiene_entrada not in ("si", "no"):
        return jsonify({"ok": False, "mensaje": "Datos inválidos"}), 400

    try:
        edad = int(edad)
    except (TypeError, ValueError):
        return jsonify({"ok": False, "mensaje": "Edad debe ser número"}), 400

    if not puede_entrar(edad, tiene_entrada):
        return jsonify({"ok": False, "mensaje": "Acceso denegado"}), 403

    asistentes = cargar_asistentes()
    nuevo = {"nombre": nombre.upper(), "edad": edad}
    asistentes.append(nuevo)
    archivar_asistentes(asistentes)

    return jsonify({"ok": True, "mensaje": "Bienvenido al club!", "asistente": nuevo}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
