from flask import Blueprint, request, render_template, redirect, make_response
import bcrypt, jwt, datetime, os

auth_bp = Blueprint("auth", __name__, template_folder="templates")
SECRET_KEY = os.getenv("ADMIN_SECRET_KEY", "secret")
HASHED_PASSWORD = os.getenv("ADMIN_PASSWORD_HASH")

@auth_bp.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

@auth_bp.route("/login", methods=["POST"])
def login_post():
    data = request.form
    if not HASHED_PASSWORD:
        return render_template("login.html", error="Missing password hash.")

    if data["username"] == "admin" and bcrypt.checkpw(data["password"].encode(), HASHED_PASSWORD.encode()):
        token = jwt.encode(
            {"user": "admin", "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
            SECRET_KEY, algorithm="HS256"
        )
        resp = make_response(redirect("/admin/files"))
        resp.set_cookie("token", token)
        return resp

    return render_template("login.html", error="Invalid username or password.")
