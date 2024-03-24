#__init_.py

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config.from_object(Config)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/mpappia/Desktop/Voyage_Aff-air/app/data/db_intern1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)

from app import routes, models  # Importations après l'initialisation de l'application

# Configurations spécifiques à la connexion
login_manager.login_view = 'login'  # par exemple

#TEST ADMIN

# Importez vos modèles après avoir initialisé db et login_manager
from app.models import users as User, Comment

# Déplacez l'importation de users et la création de la vue d'administration ici
def init_admin():
    admin = Admin(app, name='Dashboard', template_mode='bootstrap3')

    class UserAdminView(ModelView):
        column_list = ('id', 'pseudo_user', 'email_user')
        form_columns = ('pseudo_user', 'email_user', 'password_user', 'id_role')
    
    class CommentAdminView(ModelView):
        column_list = ('id','id_user','pseudo', 'created_at', 'content')
        form_columns = ('id_user','pseudo','content')  # Colonnes du formulaire d'édition

    admin.add_view(UserAdminView(User, db.session))
    admin.add_view(CommentAdminView(Comment, db.session))

# Appelez init_admin pour initialiser l'interface d'administration
init_admin()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))