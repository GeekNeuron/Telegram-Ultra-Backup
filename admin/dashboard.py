from flask import Blueprint, request, render_template, redirect, url_for
import jwt, os
from sqlalchemy.orm import sessionmaker
from bot.database import engine, BackupFile

dashboard_bp = Blueprint("dashboard", __name__, template_folder="templates")
SECRET_KEY = os.getenv("ADMIN_SECRET_KEY", "super-secret")
Session = sessionmaker(bind=engine)

def token_required(func):
    def wrapper(*args, **kwargs):
        token = request.cookies.get("token")
        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except:
            return redirect(url_for("auth.login_page"))
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

@dashboard_bp.route("/files")
@token_required
def file_list():
    session = Session()
    files = session.query(BackupFile).all()
    session.close()
    return render_template("dashboard.html", files=files)
