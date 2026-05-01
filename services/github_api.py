import requests

def get_github_user_data(token):
    """Fetches the authenticated user's profile data."""
    headers = {'Authorization': f'token {token}'}
    response = requests.get('https://api.github.com/user', headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

def get_github_repos(token):
    """Fetches the authenticated user's repositories."""
    headers = {'Authorization': f'token {token}'}
    # sort by updated, fetch up to 30 recent repos
    response = requests.get('https://api.github.com/user/repos?sort=updated&per_page=30', headers=headers)
    if response.status_code == 200:
        return response.json()
    return []
