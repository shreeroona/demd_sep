from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
# Function that would be executed when the above URL is hit.

def welcome():
    return f"testing heroku"

# Defining second url
@app.route('/name/<your_name>')
# Function that should be executed when this URL is hit
def names(your_name):
    return f"Welcome to Praxis {your_name}"

if __name__ == "__main__":
    # Use debug only when required. With debug no need to stop the server every time.
    app.run()