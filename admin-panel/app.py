from flask import Flask, request, jsonify
from bot.database import Database

app = Flask(__name__)
db = Database()

@app.route('/backups', methods=['GET'])
def get_backups():
    return jsonify(db.get_all_backups())

@app.route('/clone', methods=['POST'])
def register_clone():
    data = request.json
    db.register_clone(data['clone_id'], data['user_id'])
    return jsonify({"status": "success"})

@app.route('/health', methods=['GET'])
def health_check():
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
