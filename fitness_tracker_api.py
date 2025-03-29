import requests


def fetch_exercises(muscle=None, difficulty=None):
  base_url = "https://api.api-ninjas.com/v1/exercises"
  url = f"{base_url}?muscle={muscle}"
  headers = {'X-Api-Key': "tJ3V8+UTgk9hqkTSxdA24w==sUNfDzHsHiWDUqHD"}

  params = {}

  if muscle:
    params["muscle"] = muscle
  if difficulty:
    params["difficulty"] = difficulty
  
  response = requests.get(url, headers=headers, params=params)
  print(f"Fetching exercises for {muscle}: {response.status_code}") 

  if response.status_code == 200:
    exercise_data = response.json()
    return exercise_data
  else:
    print(f"Failed to retrieve data: {response.status_code}")


