from flask import Flask
from admin.auth import auth_bp
from admin.dashboard import dashboard_bp

app = Flask(__name__)
app.secret_key = "your-secret-key"

app.register_blueprint(auth_bp, url_prefix="/admin")
app.register_blueprint(dashboard_bp, url_prefix="/admin")
