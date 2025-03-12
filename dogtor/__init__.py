from flask import Flask

def create_app():
    app = Flask(__name__)
    
    @app.router("/")
    def hello():
        return "Hello world"
    
    
    
    
    return app
