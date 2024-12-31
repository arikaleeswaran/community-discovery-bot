from flask import Flask

def create_app(config_object=None):
    app = Flask(__name__)
    
    if config_object:
        app.config.from_object(config_object)
    
    from .routes import init_routes
    init_routes(app)
    
    return app
