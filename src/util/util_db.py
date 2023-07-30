from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SQLAlchemyConnector:
    @staticmethod
    def init_app(app):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://vitus:vitus@db:3306/vp_db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)
