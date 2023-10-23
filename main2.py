import requests
import json

def is_water_enough(lat, lon, radius=30000):
    # Define the Overpass API URL
    overpass_url = "http://overpass-api.de/api/interpreter"


    overpass_query = f"""
    [out:json];
    (
      way["natural"="water"](around:{radius},{lat},{lon});
      relation["natural"="water"](around:{radius},{lat},{lon});
    );
    out count;
    """

    try:
        # Send the request
        response = requests.get(overpass_url, params={'data': overpass_query})

        # Check if the request was successful (status code 200)
        response.raise_for_status()


        data = response.json()


        return len(data['elements']) > 10

    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'An error occurred: {err}')


print(is_water_enough(51.5074, -0.1278))

