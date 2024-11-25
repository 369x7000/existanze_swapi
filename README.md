# Star Wars SWAPI

This Python application allows users to interact with the **Star Wars API (SWAPI)** to search for information about Star Wars characters, including optional details about their homeworld. The tool also supports caching search results locally and visualizing them.

## Features

- **Character Search**: Look up information about Star Wars characters.
- **Homeworld Information**: Include optional details about a character's homeworld.
- **Caching**: Saves search results locally to reduce redundant API calls.
- **Cache Management**:
  - Clear cached results.
  - Visualize cached results with a bar plot.

## Prerequisites

Before using the tool, ensure you have the following installed:

- Python 3.7 or later
- `requests`
- `matplotlib`

You can install the required packages using `pip`:

```bash
pip install requests matplotlib
```

## How to Use

### Clone the Repository

```bash
git clone https://github.com/369x7000/existanze_swapi.git
cd existanze_swapi
```

### Run the Application

The tool is command-line based. Use the following commands to perform various actions:

#### 1. Search for a Character

```bash
python main.py search <character_name> [--world]
```

- Replace `<character_name>` with the name of the character (e.g., `Luke Skywalker`).
- Use the `--world` flag to include homeworld details.

**Example:**
```bash
python main.py search 'Luke Skywalker' --world
```

#### 2. Manage the Cache

- **Clear the Cache:**

```bash
python main.py cache --clean
```

- **Visualize the Cache:**

```bash
python main.py cache --visualize
```

### Examples of Outputs

#### Character Search
```plaintext
Name: Luke Skywalker
Height: 172 cm
Mass: 77 kg
Birth Year: 19BBY

Homeworld
----------------
Name: Tatooine
Population: 200000
On Tatooine, 1 year on Earth is 0.95 years and 1 day is 1.01 days.
```

#### Cache Visualization
Displays a horizontal bar plot of cached searches, ordered by time, with details and timestamps.

## Project Structure

```
.
├── main.py          # Main script for the application
├── search_cache.json # Local cache file (auto-created)
└── README.md         # Documentation
```

## Limitations

- Requires internet access to fetch data from the SWAPI.
- The homeworld visualization is dependent on the structure and availability of API data.

## Future Enhancements

- Add support for more Star Wars data, such as starships or vehicles.
- Improve the visualization for cached data with additional insights.

## License

This project is licensed under the [MIT License](https://github.com/369x7000/existanze_swapi/blob/main/MIT%20License).

## Acknowledgments

- [Star Wars API (SWAPI)](https://www.swapi.tech) for the data.
