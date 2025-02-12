from flask import Flask
from models.routes import routes

app = Flask(__name__)


app.register_blueprint(routes)

if __name__ == '__main__':
    app.run()