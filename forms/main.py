from flask import Flask, render_template, request, url_for, redirect
from hamdb import hamdb
#Flask is cool

app = Flask(__name__)

subscribers = []
calldata = []

# Routes for different pages
@app.route('/')
def home():
    title = "Club Home Page"
    return render_template('index.html',title=title)  

@app.route('/subscribe')
def suscribe():
    title = "subscribe to my newsletter"
    return render_template("subscribe.html", title=title) 

@app.route('/gethaminfo')
def gethaminfo():
    title = "Enter Your QSL Information"
    return render_template("gethaminfo.html", title=title) 

@app.route('/showhaminfo', methods=["POST"])
def showhaminfo():
    hamdb()
    title = "Thanks For Working W2AMC!"
    callsign = request.form.get("callsign")
    full_name = request.form.get("full_name")
    email = request.form.get("email")
    calldata.append(f"{callsign} {full_name} {email}")
    return render_template("showhaminfo.html", title=title, calldata=callinfo) 

@app.route('/form', methods=["POST"])
def form():
    title = "Thank You!"
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    subscribers.append(f"{first_name} {last_name} | {email}")
    return render_template("form.html", title=title, subscribers=subscribers) 

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    print (f"<h1>{usr}</h1>")
    return render_template('index.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
