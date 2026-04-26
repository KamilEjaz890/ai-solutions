from github import Github, Auth
from dotenv import load_dotenv
import os

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_REPO_NAME = os.getenv("GITHUB_REPO_NAME")

print(f"Username: '{GITHUB_USERNAME}'")
print(f"Repo name: '{GITHUB_REPO_NAME}'")
print(f"Token starts with: '{GITHUB_TOKEN[:10]}...'")

try:
    g = Github(auth=Auth.Token(GITHUB_TOKEN))
    user = g.get_user()
    print(f"\nLogged in as: {user.login}")
    print(f"Looking for repo: {GITHUB_USERNAME}/{GITHUB_REPO_NAME}")
    
    # List all your repos
    print("\nYour repos:")
    for repo in user.get_repos():
        print(f"  - {repo.name}")

except Exception as e:
    print(f"Error: {e}")