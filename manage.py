from unicodedata import name
from app import create_app, db
from flask_script import Manager,Server
from decouple import config
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Role, Blog, Comment, Category, Subscriber
from app.main.forms import BlogForm

app = create_app(config('env', default="development"))

manager = Manager(app)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db, User=User, Role=Role, Comment = Comment, 
        Category = Category, Blog = Blog, Subscriber = Subscriber )

@manager.command
def seed():
    "Add seed data to the database."
    roles = [Role(name="Admin"), Role(name="User")]
    categories = [
        Category(name="Food"),
        Category(name="Technology"),
        Category(name="Travel"),
        Category(name="Music"),
        Category(name="Fashion"),
    ]

    # db.session.add_all(roles)
    db.session.add_all(categories)
    db.session.commit()

@app.context_processor
def inject_user():
    blog_form = BlogForm()
    categories = Category.get_all_categories()
    return dict(blog_form=blog_form, categories=categories)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()