from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/googleea2cd7e0a312099b.html')
def google_search_console():
    """Return a google_search_console verification code"""
    return '<html><head></head><body>google-site-verification: googleea2cd7e0a312099b.html</body></html>'

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
