import requests


base_url = 'https://api.wcs.org/'

# Define the endpoints for species distribution and human-wildlife conflict
species_distribution_endpoint = 'species_distribution'
human_wildlife_conflict_endpoint = 'human_wildlife_conflict'

# Make a request to the species distribution endpoint for tigers
response = requests.get(f'{base_url}{species_distribution_endpoint}', params={'species': 'tiger'})
species_distribution_data = response.json()

# Make a request to the human-wildlife conflict endpoint for the area of interest
response = requests.get(f'{base_url}{human_wildlife_conflict_endpoint}', params={'area': 'your_area_of_interest'})
human_wildlife_conflict_data = response.json()

# Determine if the area is suitable for tigers
is_suitable = (species_distribution_data['is_present'] and not human_wildlife_conflict_data['is_conflict'])

print(is_suitable)
