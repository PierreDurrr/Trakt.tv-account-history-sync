import requests
import json

# 🚀 Replace with your API credentials
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"

# Trakt API URLs
TRAKT_BASE_URL = "https://api.trakt.tv"
TOKEN_URL = f"{TRAKT_BASE_URL}/oauth/token"

def authenticate_trakt():
    """ Authenticate with Trakt and get an access token """
    print("Go to this URL and authorize the app:")
    print(f"https://trakt.tv/oauth/authorize?response_type=code&client_id={CLIENT_ID}&redirect_uri=urn:ietf:wg:oauth:2.0:oob")

    auth_code = input("Enter the code from Trakt: ").strip()

    data = {
        "code": auth_code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": "urn:ietf:wg:oauth:2.0:oob",
        "grant_type": "authorization_code"
    }

    response = requests.post(TOKEN_URL, json=data)

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print("❌ Authentication failed:", response.json())
        exit()


def get_watched_history(token):
    """ Get full watched history from Trakt (all time) """
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "trakt-api-version": "2",
        "trakt-api-key": CLIENT_ID
    }

    history = []
    page = 1

    while True:
        response = requests.get(f"{TRAKT_BASE_URL}/sync/history?page={page}&limit=1000", headers=headers)

        if response.status_code == 200:
            page_data = response.json()
            if not page_data:
                break  # No more history, exit loop

            history.extend(page_data)
            page += 1
        else:
            print("❌ Failed to get history:", response.json())
            break

    return history

def sync_history(token, history):
    """ Sync history to another Trakt account """
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "trakt-api-version": "2",
        "trakt-api-key": CLIENT_ID
    }

    payload = {"movies": [], "episodes": []}

    for item in history:
        if item["type"] == "movie":
            payload["movies"].append({"ids": item["movie"]["ids"]})
        elif item["type"] == "episode":
            payload["episodes"].append({"ids": item["episode"]["ids"]})

    response = requests.post(f"{TRAKT_BASE_URL}/sync/history", headers=headers, json=payload)

    if response.status_code == 201:
        print("✅ History synced successfully!")
    else:
        print("❌ Failed to sync history:", response.json())

# 🔄 Authenticate for Account 1 (source)
print("🔑 Logging into Account 1...")
token1 = authenticate_trakt()

# 📥 Get watched history from Account 1
print("📥 Fetching watched history...")
history = get_watched_history(token1)

# 🔄 Authenticate for Account 2 (destination)
print("🔑 Logging into Account 2...")
token2 = authenticate_trakt()

# 📤 Sync history to Account 2
print("📤 Syncing history to Account 2...")
sync_history(token2, history)
