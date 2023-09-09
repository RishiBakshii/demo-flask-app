from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route and a function to handle it
@app.route('/')
def hello_world():
    return 'Hello, World! This is a demo Flask app.'

if __name__ == '__main__':
    # Run the app on a development server
    app.run(debug=True)
