from flask import Blueprint, render_template, request

views = Blueprint(__name__, "views")


# Home Page
@views.route("/")
def home():
    return render_template("index.html")

# Login Page
@views.route('/login')
def login():
    return render_template("login.html")

# Sign Up Page
@views.route('sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
            email = request.form.get('email')
            first_name = request.form.get('firstName')
            password1 = request.form.get('password1')
            password2 = request.form.get('password2')
            with open('info.txt', 'a') as file:
                file.write(f"{email},{first_name},{password1}\n")
    return render_template("sign-up.html")

# Log Out Page
@views.route('/logout')
def logout():
    return render_template("logout.html")

# access unique webpages for individual names
@views.route("/profile/<username>")
def profile(username):
    return render_template("profiles.html", name=username)