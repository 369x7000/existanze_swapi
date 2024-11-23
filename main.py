import requests
import argparse
import json
from datetime import datetime
import matplotlib.pyplot as plt


CACHE_FILE = "search_cache.json"
#load existing cache
try:
    with open(CACHE_FILE, "r") as f:
        search_cache = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    search_cache = {}

def save_cache():
    #save
    with open(CACHE_FILE, "w") as f:
        json.dump(search_cache, f, indent=4)

def clean():
    #clear and delete
    global search_cache
    search_cache = {}
    try:
        with open(CACHE_FILE, "w") as f:
            f.write("{}")
    except Exception as e:
        print(f"Error while clearing the cache: {e}")
    finally:
        print("Cache cleared successfully.")

def visualize_cache():
    #boxplot
    if not search_cache:
        print("No cached searches to visualize.")
        return

    timestamps = []
    results = []
    details = []

    for character_name, data in search_cache.items():
        timestamps.append(data["timestamp"])
        results.append(character_name)
        details.append(data["data"].split("\n")[0])  # First line (character name)

    #create plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(results, range(len(results)), align='center', color='skyblue')

    #labels/timestamps
    for i, (timestamp, detail) in enumerate(zip(timestamps, details)):
        ax.text(i, i, f"{detail}\n({timestamp})", ha='center', va='bottom', fontsize=8)

    #format
    ax.set_title("Cached Searches")
    ax.set_xlabel("Searches (Ordered by Time)")
    ax.set_ylabel("Character Names")
    ax.invert_yaxis()  # Show most recent at the top
    plt.tight_layout()
    plt.show()

def search(character_name, include_world=False):
    #search char
    if character_name in search_cache:
        cached_result = search_cache[character_name]
        print(f"Cached result from {cached_result['timestamp']}:")
        print(cached_result['data'])
        if include_world and "homeworld" in cached_result:
            print("\nHomeworld")
            print("----------------")
            print(cached_result["homeworld"])
        return

    base_url = "https://www.swapi.tech/api/people/"
    try:
        response = requests.get(base_url, params={"name": character_name})
        response.raise_for_status()

        data = response.json()

        if data.get('result'):
            result_output = []
            homeworld_info = None
            for result in data['result']:
                properties = result['properties']
                char_info = (
                    f"Name: {properties['name']}\n"
                    f"Height: {properties['height']} cm\n"
                    f"Mass: {properties['mass']} kg\n"
                    f"Birth Year: {properties['birth_year']}\n"
                )
                result_output.append(char_info)
                if include_world and properties.get('homeworld'):
                    homeworld_info = fetch_homeworld(properties['homeworld'])
                    char_info += f"\nHomeworld ----------------\n{homeworld_info}"

            search_cache[character_name] = {
                "timestamp": str(datetime.now()),
                "data": "\n".join(result_output),
                "homeworld": homeworld_info if include_world else None,
            }
            save_cache()
            print("\n".join(result_output))
        else:
            print("The force is not strong within you. No results found.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to the API: {e}")
    except KeyError as e:
        print(f"Unexpected response format: {e}")

def fetch_homeworld(homeworld_url):
    #convert to our earth years/days
    try:
        response = requests.get(homeworld_url)
        response.raise_for_status()

        world_data = response.json().get('result', {}).get('properties', {})

        if world_data:
            orbital_period = float(world_data['orbital_period'])
            rotation_period = float(world_data['rotation_period'])
            homeworld_info = (
                f"Name: {world_data['name']}\n"
                f"Population: {world_data['population']}\n"
                f"On {world_data['name']}, 1 year on Earth is {orbital_period / 365:.2f} years "
                f"and 1 day is {rotation_period / 24:.2f} days."
            )
            return homeworld_info
        else:
            return "Homeworld information unavailable."
    except requests.exceptions.RequestException as e:
        return f"Failed to fetch homeworld data: {e}"
    except KeyError as e:
        return f"Unexpected response format for homeworld: {e}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Star Wars API character search tool.")
    subparsers = parser.add_subparsers(dest="action", required=True)

    #search
    search_parser = subparsers.add_parser("search", help="Search for a Star Wars character.")
    search_parser.add_argument("character_name", type=str, help="Full or partial name of the character to search.")
    search_parser.add_argument("--world", action="store_true", help="Include details about the character's homeworld.")

    #cache
    cache_parser = subparsers.add_parser("cache", help="Manage the cache.")
    cache_parser.add_argument("--clean", action="store_true", help="Clear the cache.")
    cache_parser.add_argument("--visualize", action="store_true", help="Visualize the cache.")

    args = parser.parse_args()

    if args.action == "search":
        search(args.character_name, include_world=args.world)
    elif args.action == "cache":
        if args.clean:
            clean()
        elif args.visualize:
            visualize_cache()
