Here’s an example of a README file for your project:

---

# Star Wars API Character Search Tool

This is a Python command-line tool that lets you search for information about Star Wars characters using the [Star Wars API (SWAPI)](https://swapi.dev/). The tool includes a caching mechanism to store and visualize previous searches, along with optional homeworld data.

---

## Features

- **Character Search:** Look up information about Star Wars characters such as name, height, mass, and birth year.
- **Homeworld Details:** Include additional information about the character's homeworld (population, orbital period, and rotation period).
- **Caching:** Stores previous search results for faster retrieval and offline access.
- **Cache Management:**
  - Clear the cache.
  - Visualize cached searches using a horizontal bar plot.

---

## Prerequisites

Before running this tool, ensure you have the following installed:

- Python 3.7+
- Required Python packages: `matplotlib`, `argparse`, and `requests`

Install the dependencies using:
```bash
pip install -r requirements.txt
```

---

## Usage

Run the script from the command line using the following options:

### Character Search

```bash
python star_wars_search.py search <character_name> --world
```

- Replace `<character_name>` with the full or partial name of the character you want to search.
- Use the `--world` flag to include homeworld details.

Example:
```bash
python star_wars_search.py search "Luke Skywalker" --world
```

### Cache Management

#### Clear the Cache
```bash
python star_wars_search.py cache --clean
```

#### Visualize the Cache
```bash
python star_wars_search.py cache --visualize
```

---

## Example Output

### Search Result
```plaintext
Name: Luke Skywalker
Height: 172 cm
Mass: 77 kg
Birth Year: 19BBY

Homeworld
----------------
Name: Tatooine
Population: 200000
On Tatooine, 1 year on Earth is 1.09 years and 1 day is 0.83 days.
```

### Cache Visualization
A bar chart will be displayed showing the cached searches with timestamps and a summary of the character names.

---

## Code Structure

- **`search_cache.json`:** File used to store cached search results.
- **Functions:**
  - `search`: Fetch character details from SWAPI.
  - `fetch_homeworld`: Retrieve homeworld details from SWAPI.
  - `clean`: Clear the cache.
  - `visualize_cache`: Generate a bar chart of cached searches.
- **Command-line Arguments:** Managed using `argparse` for flexible functionality.

---

## Contributions

Contributions are welcome! Feel free to fork this repository and submit pull requests for new features or bug fixes.

---

## License

This project is licensed under the [MIT License](https://github.com/369x7000/existanze_swapi/blob/main/LICENSE).


---

## Acknowledgments

- [SWAPI](https://swapi.dev/) for providing the Star Wars data.
- Python libraries: `requests`, `argparse`, `matplotlib`.
