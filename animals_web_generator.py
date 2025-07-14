import json

def load_data(file_path):
    """Load data from a JSON file."""
    with open(file_path, 'r') as handle:
        return json.load(handle)
    

def get_animals_information():
    for animal in animals_data:
        if all(k in animal for k in ['name', 'locations', 'characteristics']) and \
           all(k in animal['characteristics'] for k in ['diet', 'type']):
              print(f"Name: {animal['name']}, Diet: {animal['characteristics']['diet']}, Location: {animal['locations']}, Type: {animal['characteristics']['type']}\n")
        else:
            continue


animals_data = load_data('animals_data.json')
get_animals_information()