import os
from flask import Flask, render_template, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
from services.github_api import get_github_user_data, get_github_repos

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
# Secret key is required for Flask sessions
app.secret_key = os.getenv("SECRET_KEY", "fallback_secret_key")

# OAuth Configuration
oauth = OAuth(app)
github = oauth.register(
    name='github',
    client_id=os.getenv("GITHUB_CLIENT_ID"),
    client_secret=os.getenv("GITHUB_CLIENT_SECRET"),
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'read:user user:email'},
)

@app.route('/')
def index():
    # If user is already logged in, redirect to dashboard
    if 'github_token' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/login')
def login():
    # Redirect user to GitHub for authorization
    redirect_uri = url_for('auth', _external=True)
    return github.authorize_redirect(redirect_uri)

@app.route('/auth')
def auth():
    # Handle the callback from GitHub and store the token
    token = github.authorize_access_token()
    session['github_token'] = token
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    if 'github_token' not in session:
        return redirect(url_for('index'))
    
    token = session['github_token']['access_token']
    
    # Fetch user data and repositories using our service functions
    user_data = get_github_user_data(token)
    repos = get_github_repos(token)
    
    if not user_data:
        session.pop('github_token', None)
        return redirect(url_for('index'))
        
    return render_template('dashboard.html', user=user_data, repos=repos)

@app.route('/logout')
def logout():
    # Clear the session securely
    session.pop('github_token', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
