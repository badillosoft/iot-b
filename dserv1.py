from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return "Hola daplicity :D"

app.run(port=80)
