
print("This will be the entry point")

print("But that's it folks")

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# '----+----1----+----2----+----3----+----4----+----5'
if __name__ == '__main__':
    # app.run(debug=True, host='localhost')
    app.run(debug=True, host='0.0.0.0')
