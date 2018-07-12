# basic flask example from code.tutsplus.com
from flask import Flask
app = Flask(__name__)

# define the basic route '/' and its corresponding request handler
@app.route("/")
def main():
    return "Welcome!"

if __name__ == "__main__":
    app.run()
