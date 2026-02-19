from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Heyy congrats you have succesfully deploy your image!'