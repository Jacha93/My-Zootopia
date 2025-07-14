import json


def load_data(file_path):
    """Load data from a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as handle:
        return json.load(handle)


def serialize_animals_to_html(animal):
    """Generate HTML snippet for a single animal."""
    return (
        '<li class="cards__item">'
        f'<div class="card__title">{animal["name"]}</div>\n'
        '<p class="card__text">'
        f'<strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'
        f'<strong>Location:</strong> {", ".join(animal["locations"])}<br/>\n'
        f'<strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'
        '</p>'
        '</li>'
    )


def get_animals_information():
    """Generate a string with information about animals."""
    output = ""
    for animal in animals_data:
        if all(k in animal for k in ['name', 'locations', 'characteristics']) and \
           all(k in animal['characteristics'] for k in ['diet', 'type']):
            output += serialize_animals_to_html(animal)
    return output


def read_animals_html(file_path):
    """Read the animals HTML file and return its content."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_animals_html(file_path, content):
    """Write content to the animals HTML file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


if __name__ == "__main__":
    animals_data = load_data('animals_data.json')
    animals_template_html = read_animals_html('animals_template.html')
    animals_html = animals_template_html.replace(
        "__REPLACE_ANIMALS_INFO__", get_animals_information()
    )
    write_animals_html('animals.html', animals_html)
