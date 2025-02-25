from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# Koneksi ke MongoDB Atlas
MONGO_URI = "mongodb+srv://satriapambingkas:<db_password>@cluster0.ywamm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["iot_data"]  # Nama database
collection = db["sensor_data"]  # Nama collection

@app.route("/sensor-data", methods=["POST"])
def receive_data():
    try:
        data = request.json
        data["timestamp"] = datetime.utcnow()  # Tambahkan timestamp

        # Simpan ke MongoDB
        collection.insert_one(data)

        return jsonify({"message": "Data berhasil disimpan", "data": data}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
