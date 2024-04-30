from functools import wraps
import os
from pathlib import Path
from flask import Flask, request, jsonify, Response
from flask_basicauth import BasicAuth

#initialize the internal Flask server
app = Flask("app")

# Set up basic authentication, name and password from .env variables
app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME') or "admin" #default name
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD') or "admin" #default pass
basic_auth = BasicAuth(app)

# Now you can use @requires_auth function decorator to require login on certain pages
def requires_auth(f):
    @wraps(f)
    async def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not (auth.username == app.config['BASIC_AUTH_USERNAME'] and auth.password == app.config['BASIC_AUTH_PASSWORD']):
            return Response(
                'Could not verify your access level for that URL.\n'
                'You have to login with proper credentials', 401,
                {'WWW-Authenticate': 'Basic realm="Login Required"'})
        return await f(*args, **kwargs)
    return decorated

# handle default address, show demo html page from ./test_form.html
@app.route('/', methods=['GET'])
async def test_form():
    return Path("./test_form.html").read_text()

# simple health check, just return OK to see the server is running
@app.route('/health', methods=['GET','POST'])
async def health_check():
    return "OK version 2"

# secret page, requires authentication
@app.route('/secret', methods=['GET'])
@requires_auth
async def secret_page():
    return Path("./secret_page.html").read_text()

# API address for POST requests
@app.route('/prompt', methods=['POST'])
async def process_json():

    #data sent to the server
    input = request.get_json()
    #data from this server    
    processed_data = {
        "message": "Data received",
        "input_data": input,
    }
    #respond with json
    return jsonify(processed_data)


#run the internal server
if __name__ == "__main__":
    app.run()