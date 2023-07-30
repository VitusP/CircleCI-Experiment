from flask_migrate import Migrate, upgrade, init, migrate as main_migrate
from flask.cli import FlaskGroup
from controller import app, db

from models.model_test import Test
from models.model_user import User
migrate = Migrate(app, db)

cli = FlaskGroup(app)

@cli.command("db_init")
def db_init():
    with app.app_context():
        init(directory=migrate.directory)
        db.create_all()

@cli.command("db_migrate")
def db_migrate():
    with app.app_context():
        main_migrate(directory=migrate.directory)

@cli.command("db_upgrade")
def db_upgrade():
    with app.app_context():
        upgrade(directory=migrate.directory)

if __name__ == '__main__':
    cli()
