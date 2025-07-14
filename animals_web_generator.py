import json

def load_data(file_path):
    """Load data from a JSON file."""
    with open(file_path, 'r') as handle:
        return json.load(handle)
    

def get_animals_information():
    """Generate a string with information about animals."""
    output = ""
    for animal in animals_data:
        if all(k in animal for k in ['name', 'locations', 'characteristics']) and \
           all(k in animal['characteristics'] for k in ['diet', 'type']):
              output += (
                  f"Name: {animal['name']}\n"
                  f"Diet: {animal['characteristics']['diet']}\n"
                  f"Location: {', '.join(animal['locations'])}\n"
                  f"Type: {animal['characteristics']['type']}\n\n"
              )
        else:
            continue
    return output


def read_animals_html(file_path):
    """Read the animals HTML file and return its content."""
    with open(file_path, 'r') as file:
        return file.read()


def write_animals_html(file_path, content):
    """Write content to the animals HTML file."""
    with open(file_path, 'w') as file:
        file.write(content)


animals_data = load_data('animals_data.json')
animals_template_html = read_animals_html('animals_template.html')
animals_html = animals_template_html.replace("__REPLACE_ANIMALS_INFO__", get_animals_information())
write_animals_html('animals.html', animals_html)