from flask import Flask
import os
from .controllers.personal_controller import personal as personal_blueprint

isDebug = os.environ.get('DEBUG', False)
app = Flask(__name__)

app.register_blueprint(personal_blueprint)

if __name__ == '__main__':
    app.run(debug=isDebug, host="0.0.0.0", port=8080)
