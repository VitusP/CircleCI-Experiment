import json
import os
import requests
import base64
from dotenv import load_dotenv
from flask import redirect, request, session

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..','web.env'))

# Spotify API credentials (Will need to be put in external file)
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
REDIRECT_URL = os.getenv('SPOTIFY_REDIRECT_URI')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

# Scope for Spotify API
SCOPE = 'user-read-private user-read-email'

# Spotify API endpoints
AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1'

def login():
    auth_url = f"{AUTHORIZE_URL}?response_type=code&client_id={CLIENT_ID}&scope={SCOPE}&redirect_uri={REDIRECT_URL}"
    return redirect(auth_url)

def callback():
    authorization_code = request.args.get('code')
    auth_header = base64.b64encode((CLIENT_ID + ':' + CLIENT_SECRET).encode('ascii')).decode('ascii')
    headers = {'Authorization': f'Basic {auth_header}'}
    data = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': REDIRECT_URL
    }

    response = requests.post(TOKEN_URL, headers=headers, data=data)
    token_data = json.loads(response.text)

    # Store the access token in the session for future use
    session['access_token'] = token_data['access_token']

    # Redirect to a route where you can make authorized API requests
    return redirect('/spotify/profile')

def get_user_profile():
    access_token = session.get('access_token')

    headers = {'Authorization': f'Bearer {access_token}'}
    try:
        response = requests.get(API_BASE_URL + '/me', headers=headers)
        return json.loads(response.text)
    except:
        return {'error': 'There was an error retrieving profile information.'}
    
def logout():
    session.clear()
    return redirect('/spotify')
