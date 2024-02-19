from flask import Flask, render_template
from routes.generales import generales_bp

app = Flask(__name__)

app.register_blueprint(generales_bp)

if __name__ == "__main__":
    app.run(debug=True)
