from flask import Flask, request, jsonify
from bot.database import Database

app = Flask(__name__)
db = Database()

@app.route('/backups', methods=['GET'])
def get_backups():
    backups = db.get_all_backups()
    return jsonify([
        {
            "id": backup[0],
            "source": backup[2],
            "target": backup[3],
            "last_run": str(backup[4]),
            "interval": backup[5]
        } 
        for backup in backups
    ])

@app.route('/clone', methods=['POST'])
def register_clone():
    data = request.json
    clone_id = data.get('clone_id')
    user_id = data.get('user_id')
    
    if not clone_id or not user_id:
        return jsonify({"error": "Missing parameters"}), 400
    
    db.register_clone(clone_id, user_id)
    return jsonify({"status": "success"})

@app.route('/health', methods=['GET'])
def health_check():
    return "OK"

@app.route('/backups/<int:backup_id>', methods=['PUT'])
def update_backup(backup_id):
    new_interval = request.json.get('interval')
    db.update_backup_interval(backup_id, new_interval)
    return jsonify({"status": "updated"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
