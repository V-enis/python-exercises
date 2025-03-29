import requests

base_url = "https://api.api-ninjas.com/v1/exercises"

def get_exercise_info(muscle):
  url = f"{base_url}?muscle={muscle_name}"
  response = requests.get(url, headers={'X-Api-Key': 'tJ3V8+UTgk9hqkTSxdA24w==sUNfDzHsHiWDUqHD'})

  if response.status_code == 200:
    exercise_data = response.json()
    return exercise_data
  else:
    print(f"Failed to retrieve data: {response.status_code}")

muscle_name = "biceps"
exercise_info = get_exercise_info(muscle_name)

if exercise_info:
  print(f"{exercise_info[0]["name"]}")

