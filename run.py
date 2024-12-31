from flask import Flask
from app.routes import init_routes
from app.database import init_db
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)

init_db()
init_routes(app)

if __name__ == '__main__':
    app.run(port=5000)
