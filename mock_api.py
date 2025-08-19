from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

@app.route("/v1/transactions", methods=["POST"])
def transactions():
    data = request.json
    # Echo back with transaction_id
    return jsonify({"transaction_id": data.get("transaction_id", str(uuid.uuid4()))}), 202

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
