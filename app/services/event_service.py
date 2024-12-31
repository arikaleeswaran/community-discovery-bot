import requests

def fetch_events(location, interests):
    api_key = 'YOUR_API_KEY'
    url = f"https://api.eventbriteapi.com/v3/events/search/?location.address={location}&q={interests}&token={api_key}"
    response = requests.get(url)
    return response.json()['events']
