from flask import Flask
from flask import render_template
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/about')
def about():
    """Return a friendly HTTP greeting."""
    return '<script type="text/javascript" src="https://platform.linkedin.com/badges/js/profile.js" async defer></script>  <div class="LI-profile-badge"  data-version="v1" data-size="medium" data-locale="en_US" data-type="horizontal" data-theme="dark" data-vanity="i-chien-tony-lin-b49ba012"><a class="LI-simple-link" href=\'https://tw.linkedin.com/in/i-chien-tony-lin-b49ba012?trk=profile-badge\'>I-Chien (Tony) Lin</a></div>'

@app.route('/googleea2cd7e0a312099b.html')
def google_search_console():
    """Return a google_search_console verification code"""
    return 'google-site-verification: googleea2cd7e0a312099b.html'

@app.route('/visualization_overview')
def visualization_overview():
    return render_template('visualization_overview.html')

@app.route('/social_community_graph')
def social_community_graph():
    """Demonstrating social community graphs."""
    return render_template('social_community_graph.html')

@app.route('/social_community_graph/vis_network')
def social_community_graph_vis_network():
    """Demonstrating social community graphs."""
    return render_template('social_community_graph_vis_network.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
