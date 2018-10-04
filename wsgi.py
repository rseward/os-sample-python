from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    #greeting="Hello World!"
    greeting="namste duniya"
    return greeting

if __name__ == "__main__":
    application.run()
