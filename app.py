import os
import datetime
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

MONGO = PyMongo(app)


# ROUTE FOR PAGES STARTS

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/places")
def places():
    places = list(MONGO.db.place.find())
    return render_template("places.html", places=places)


@app.route("/newplace", methods=["GET", "POST"])
def newplace():
    if request.method == "POST":

        existing_place = MONGO.db.place.find_one(
            {"place_name": request.form.get("place_name")})

        if existing_place:
            flash("Place already exists")
            return redirect(url_for("places"))

        new_place = {
            "place_name": request.form.get("place_name").lower(),
            "place_location": request.form.get("place_location").lower(),
            "place_image": request.form.get("place_image"),
            "date": datetime.datetime.now(),
            "place_info": request.form.get("place_info"),
            "user_name": MONGO.db.users.find_one({
                "username": session["user"]})["name"]
        }
        MONGO.db.place.insert_one(new_place)
        flash("Thank You So Much for the contribution")
        return redirect(url_for("places"))

    return render_template("place.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":

        existing_user = MONGO.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))

        register = {
            "username": request.form.get("username"),
            "name": request.form.get("name"),
            "street": request.form.get("street"),
            "houseno": request.form.get("houseno"),
            "city": request.form.get("city"),
            "zip": request.form.get("zip"),
            "country": request.form.get("country"),
            "phone": request.form.get("phone"),
            "password": generate_password_hash(request.form.get("passw"))
        }
        MONGO.db.users.insert_one(register)

        session["user"] = request.form.get("_id")

        flash("We are happy to have you on bord!")
        return redirect(url_for(
            "profile", username=session["user"]))
    return render_template("signup.html")


@app.route("/update_user/<username>", methods=["GET", "POST"])
def update_user(username):
    if request.method == "POST":

        update = {
            "street": request.form.get("street"),
            "houseno": request.form.get("houseno"),
            "city": request.form.get("city"),
            "zip": request.form.get("zip"),
            "country": request.form.get("country"),
            "phone": request.form.get("phone"),
            "password": generate_password_hash(request.form.get("passw"))
        }
        MONGO.db.users.update({"_id": ObjectId(username)}, update)
        flash("done")

    profile = MONGO.db.users.find_one({"_id": ObjectId(username)})
    return render_template("profile.html", profile=profile)


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        existing_user = MONGO.db.users.find_one(
            {"username": request.form.get("username"), })

        if existing_user:

            if check_password_hash(
               existing_user["password"], request.form.get("passw")):
                session["user"] = request.form.get("username")
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "index", username=session["user"]))

            else:
                flash("Incorrect Username or Password")
                return redirect(url_for("index"))
        else:
            flash("No user found signup please")
            return redirect(url_for("signup"))
    return render_template("profile.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = MONGO.db.users.find_one({
        "username": session["user"]})

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("index"))


@app.route("/contactus", methods=["GET", "POST"])
def contactus():
    if request.method == "POST":

        contectus_message = {
            "name": request.form.get("sender_name"),
            "email": request.form.get("sender_name"),
            "phone": request.form.get("sender_phone"),
            "message": request.form.get("message"),
            "date": datetime.datetime.now.strftime("%y-%m-%d %h:%M:%S")}
        MONGO.db.messages.insert_one(contectus_message)
    flash("thank you for your message")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
