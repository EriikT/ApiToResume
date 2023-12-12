import requests

url = 'http://erikcodingapi.pythonanywhere.com/'  # Replace with the correct URL of your Flask application
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON content from the response
    data_set = response.json()

    # Access the 'work_experience' key and print the position
    for experience in data_set.get('work_experience', []):
        print("Position:", experience.get('position'))
else:
    print("Error:", response.status_code)