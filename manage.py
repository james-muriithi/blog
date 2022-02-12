from app import create_app, db
from flask_script import Manager,Server
from decouple import config
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Role, Pitch, Comment, Category, Vote

app = create_app(config('env', default="development"))

manager = Manager(app)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db, User=User, Role=Role, Comment = Comment, 
        Category = Category, Pitch = Pitch, Vote = Vote )

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()