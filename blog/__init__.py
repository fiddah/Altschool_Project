from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager 

app = Flask(__name__)
app.config['SECRET_KEY'] = '31894a26a4b028241c1c9a4c20dd8af4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# database instance
db = SQLAlchemy(app)

#Login manager
login_manager = LoginManager(app)
login_manager.login_view = 'Login'
login_manager.login_message_category = 'info'
#user authentication
bcrypt = Bcrypt(app)

from blog import routes