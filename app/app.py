from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "ok",
        "message": "Servicio activo"
    }), 200

@app.route('/api/v1/handshake-info', methods=['GET'])
def handshake_info():
    # Retorna información enviada por los headers del proxy
    return jsonify({
        "client_ip": request.headers.get('X-Real-IP', request.remote_addr),
        "protocol_used": request.headers.get('X-SSL-Protocol', 'Desconocido'),
        "cipher_used": request.headers.get('X-SSL-Cipher', 'Desconocido')
    }), 200

@app.route('/api/v1/data', methods=['GET'])
def get_data():
    return jsonify({
        "simulation": "TLS 1.0 / 1.1 Handshake Test",
        "records": [
            {"id": 1, "status": "processed"},
            {"id": 2, "status": "processed"}
        ]
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
