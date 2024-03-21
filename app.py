#!/usr/bin/python3
""" Script that is the main entry point of the Flask application """

# Import necessary modules from Flask
from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)


# Define routes for different endpoints
@app.route('/')
def index():
    """
    Renders the index page.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('index.html')


@app.route('/deploy')
def deploy():
    """
    Renders the deploy page.

    Returns:
        str: Rendered HTML template for the deploy page.
    """
    return render_template('deploy.html')


@app.route('/monitor')
def monitor():
    """
    Renders the monitor page.

    Returns:
        str: Rendered HTML template for the monitor page.
    """
    return render_template('monitor.html')


@app.route('/scale')
def scale():
    """
    Renders the scale page.

    Returns:
        str: Rendered HTML template for the scale page.
    """
    return render_template('scale.html')


@app.route('/docs')
def documentation():
    """
    Renders the documentation page.

    Returns:
        str: Rendered HTML template for the documentation page.
    """
    return render_template('documentation.html')


# Check if the script is being run directly
if __name__ == '__main__':
    """
    Run the Flask application with host set to 0.0.0.0 and port set to 5000.
    """
    app.run(host='0.0.0.0', port=5000)
