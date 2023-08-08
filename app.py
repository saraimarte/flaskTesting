from flask import Flask, redirect, url_for

app = Flask(__name__)

a = False

@app.route("/")
def home():
    return "Home Page"

@app.route("/<name>")
def user(name):
    return f'Hello {name}!'

@app.route("/admin")
def admin():
    if a:
        return "You are an admin!"
    else:
        return redirect(url_for("user", name = "Admin!"))
    

if __name__ == "__main__":
    app.run()