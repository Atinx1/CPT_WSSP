import requests

def get_prey_availability(lat, lon, radius=10000):
    # Define the GBIF API URL for species occurrence data
    gbif_api_url = f'https://api.gbif.org/v1/occurrence/search'

    # Define the parameters for the API request
    params = {
        'decimalLatitude': lat,
        'decimalLongitude': lon,
        'radius': radius,
        'taxonKey': 7707725,  # Taxon key for mammals (you may need to adjust this for specific prey species)
        'limit': 100  # Adjust as needed
    }

    response = requests.get(gbif_api_url, params=params)

    if response.status_code == 200:
        prey_data = response.json()
        return len(prey_data['results']) > 10  # Example threshold for prey availability
    else:
        print(f"Error accessing GBIF API. Status code: {response.status_code}")
        return False

# Example usage:
latitude = 12.9716
longitude = 77.5946

if get_prey_availability(latitude, longitude):
    print("Prey availability is good enough for tigers to make their habitats.")
else:
    print("Prey availability is not sufficient for tigers to make their habitats.")
