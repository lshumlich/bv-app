
from flask import Flask, render_template
import socket
import platform
import datetime

startTime = datetime.datetime.now()
print(f"-------- devops - training -------- server started: {startTime}")
cities = None

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', msg=get_info(), cities=cities)


@app.route("/stuff")
def hello_world():
    a = 'asdf'
    return f"""
    <p>Hello, World!</p>
    {get_info()}
"""


@app.route("/healthcheck")
def health_check():
    return f'app.py ok {datetime.datetime.now()}'


def get_info():
    servedTime = datetime.datetime.now()

    return f"""
    <h2>Version 0.12 2021-08-11 1:32AM </h2>
    <br/>gethostname: {socket.gethostname()}
    <br/>getfqdn: {socket.getfqdn()}
    <br/>architecture: {platform.architecture()}
    <br/>machine: {platform.machine()}
    <br/>processor: {platform.processor()}
    <br/>python_version: {platform.python_version()}
    <br/>system: {platform.system()}
    <br/>servedTime: {servedTime}
    <br/>Server Started: {startTime}
    <br/>
    """

# 
# List of canadian cities
# 
from utils.db import DB
db = DB()
db.select('select id,city from public.canadacities')
cities = db.result
# print('The list of cities')
# print(cities)
# '----+----1----+----2----+----3----+----4----+----5'
if __name__ == '__main__':
    # app.run(debug=True, host='localhost')
    # app.run(debug=True, host='0.0.0.0', port=80)
    app.run(debug=True, host='0.0.0.0')
