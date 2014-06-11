from flask import Flask
import settings

app = Flask(__name__)
app.config.from_object('myappname.settings')

import views
app.register_blueprint(views.general)

def create_app():
    return app