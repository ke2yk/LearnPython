from flask import Flask, render_template, request, url_for, redirect

#Flask is cool

app = Flask(__name__)

# Data for pages
pages = [
    {'title': 'Home', 'link': '/home.html'},
    {'title': 'Calendar', 'link': '/calendar'},
    {'title': 'Contact', 'link': '/contact'},
    {'title': 'Photo Gallery', 'link': '/gallery'},
    {'title': 'History', 'link': '/history'},
    {'title': 'About', 'link': '/about'},
    {'title': 'Login', 'link': '/login'}
]

# Routes for different pages
@app.route('/')
def home():
    return render_template('index.html', pages=pages)  

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
    return render_template('index.html', pages=pages)

@app.route('/calendar')
def calendar():
    return render_template('calendar.html', pages=pages)

@app.route('/contact')
def contact():
    return render_template('contact.html', pages=pages)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', pages=pages)

@app.route('/history')
def history():
    return render_template('history.html', pages=pages)

@app.route('/about')
def about():
    return render_template('about.html', pages=pages)

if __name__ == '__main__':
    app.run(debug=True)
