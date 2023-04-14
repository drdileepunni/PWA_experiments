from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['TEMPLATES_AUTO_RELOAD'] = True
print(app.jinja_env)

db = SQLAlchemy(app)

@app.cli.command('init-db')
def init_db():
    with app.app_context():
        db.create_all()
        print('Initialized the database.')

from app import routes, models