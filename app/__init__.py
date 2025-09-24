
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

# Initialize extensions
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object("config")

    # Initialize extensions with app
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)

    # Register blueprints
    from app.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    from app.routes.schedule_routes import schedule_bp
    app.register_blueprint(schedule_bp, url_prefix="/api/schedule")

    from app.routes.feedback_routes import feedback_bp
    app.register_blueprint(feedback_bp, url_prefix="/api/feedback")

    from app.routes.export_routes import export_bp
    app.register_blueprint(export_bp, url_prefix="/api/export")

    from app.routes.welcome import welcome_bp
    app.register_blueprint(welcome_bp)





    # You can register more blueprints here later:
    # from app.routes.schedule_routes import schedule_bp
    # app.register_blueprint(schedule_bp, url_prefix="/api/schedule")

    return app
