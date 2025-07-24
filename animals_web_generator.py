import json


def load_data(file_path):
    """Load data from a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as handle:
            return json.load(handle)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []


def serialize_animals_to_html(animal):
    """Generate HTML snippet for a single animal."""
    name = animal.get("name", "Unknown")
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet", "N/A")
    animal_type = characteristics.get("type", "N/A")
    locations = animal.get("locations", [])
    location_str = locations[0] if locations else "N/A"
    return f"""
    <li class="cards__item">
    <div class="card__title">{name}</div>
    <p class="card__text">
        <strong>Diet:</strong> {diet}<br/>
        <strong>Location:</strong> {location_str}<br/>
        <strong>Type:</strong> {animal_type}<br/>
    </p>
    </li>
    """


def get_animals_information():
    """Generate a string with information about animals."""
    output = ""
    for animal in animals_data:
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
