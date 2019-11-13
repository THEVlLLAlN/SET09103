from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    logged = 0
    if logged == 0:
        page ="""
        <html>
        <h1>Dungeons and Dragons: HUB</h1>
        <h2>Register </h2>
        </html>
        """
    return page 
