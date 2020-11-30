import datetime
from flask import Flask, render_template, request, jsonify
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from flask_jwt_extended import JWTManager, get_jwt_identity, create_access_token, jwt_required
from flask_mail import Mail, Message
from models import db
import config



app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(config.ConfigDevelopment)
db.init_app(app)
jwt = JWTManager(app)
mail = Mail(app)
Migrate(app, db)
CORS(app)
manager = Manager(app)
manager.add_command("db", MigrateCommand)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/api/mail/test', methods=['GET'])
def send_mail_test():
    msg = Message("Test Mail", recipients=["lrodriguez@4geeks.co"])
    #msg.body = "Hola esto es una prueba"
    msg.html = "<h1>Hola esto es otra prueba con html</h1>"
    mail.send(msg)

    return jsonify({"success": "Email sent"}), 200


if __name__ == "__main__":
    manager.run()