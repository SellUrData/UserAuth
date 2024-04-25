from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
    app.run(debug = True)

# create_database(app)

# def create_database(app):
#     if not path.exists('pywbsite/' + DB_NAME):
#     db.create_all(app=app)
#     print('Created Database')