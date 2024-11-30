import os
import random
import csv
import math
import matplotlib.pyplot as plt


def generate_cities(num_cities, x_range=(0, 100), y_range=(0, 100), output_file="data/cities.csv"):
    """
    Generate random city coordinates and save them to a CSV file.

    Parameters:
        num_cities (int): Number of cities to generate.
        x_range (tuple): Range for x coordinates (min, max).
        y_range (tuple): Range for y coordinates (min, max).
        output_file (str): File path to save the generated cities.
    """
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Generate city data as a list of dictionaries
    cities = [{"ID": i, "x": random.randint(*x_range), "y": random.randint(*y_range)} for i in range(num_cities)]

    # Write the generated city data to a CSV file
    with open(output_file, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["ID", "x", "y"])
        writer.writeheader()
        writer.writerows(cities)

    print(f"Generated {num_cities} cities and saved to {output_file}")


def load_cities(input_file="data/cities.csv"):
    """
    Load city coordinates from a CSV file.

    Parameters:
        input_file (str): Path to the CSV file containing city data.

    Returns:
        list: A list of dictionaries containing city information.
    """
    # Ensure the file exists before loading
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"{input_file} not found. Please generate city data first.")

    # Read city data from CSV file
    with open(input_file, mode="r") as file:
        reader = csv.DictReader(file)
        cities = [{"ID": int(row["ID"]), "x": int(row["x"]), "y": int(row["y"])} for row in reader]

    return cities


def validate_cities(cities):
    """
    Validate the loaded city data for duplicates and consistency.

    Parameters:
        cities (list): List of city dictionaries with keys 'ID', 'x', and 'y'.

    Raises:
        ValueError: If duplicate city IDs are found.
    """
    ids = set()
    for city in cities:
        if city["ID"] in ids:
            raise ValueError(f"Duplicate city ID found: {city['ID']}")
        ids.add(city["ID"])
    print("City data validation passed!")


def calculate_distance(city1, city2, metric="euclidean"):
    """
    Calculate the distance between two cities.

    Parameters:
        city1 (dict): First city with keys 'x' and 'y'.
        city2 (dict): Second city with keys 'x' and 'y'.
        metric (str): Distance metric to use ('euclidean' or 'manhattan').

    Returns:
        float: The distance between the two cities.
    """
    if metric == "euclidean":
        return math.sqrt((city1["x"] - city2["x"]) ** 2 + (city1["y"] - city2["y"]) ** 2)
    elif metric == "manhattan":
        return abs(city1["x"] - city2["x"]) + abs(city1["y"] - city2["y"])
    else:
        raise ValueError(f"Unsupported metric: {metric}")


def calculate_route_distance(route, cities, metric="euclidean"):
    """
    Calculate the total distance of a given route.

    Parameters:
        route (list): List of city indices in the order of travel.
        cities (list): List of city dictionaries with keys 'x' and 'y'.
        metric (str): Distance metric to use ('euclidean' or 'manhattan').

    Returns:
        float: Total distance of the route.
    """
    distance = 0.0
    for i in range(len(route)):
        city1 = cities[route[i]]
        city2 = cities[route[(i + 1) % len(route)]]  # Wrap around to the start
        distance += calculate_distance(city1, city2, metric)
    return distance


def generate_random_route(num_cities):
    """
    Generate a random route by shuffling city indices.

    Parameters:
        num_cities (int): Number of cities.

    Returns:
        list: A random permutation of city indices.
    """
    route = list(range(num_cities))
    random.shuffle(route)
    return route


def save_route(route, output_file="data/best_route.csv"):
    """
    Save a specific route to a CSV file.

    Parameters:
        route (list): List of city indices in the order of travel.
        output_file (str): File path to save the route.
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Write the route to a CSV file
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["City ID"])
        for city_id in route:
            writer.writerow([city_id])

    print(f"Route saved to {output_file}")


def plot_cities(cities, title="City Map"):
    """
    Plot cities on a 2D map.

    Parameters:
        cities (list): List of city dictionaries with keys 'x' and 'y'.
        title (str): Title of the plot.
    """
    x_coords = [city["x"] for city in cities]
    y_coords = [city["y"] for city in cities]

    plt.figure(figsize=(8, 8))
    plt.scatter(x_coords, y_coords, c="blue", label="Cities")
    for city in cities:
        plt.annotate(city["ID"], (city["x"], city["y"]), textcoords="offset points", xytext=(5, 5), ha="center")
    plt.title(title)
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_route(route, cities, title="TSP Route"):
    """
    Plot a specific TSP route by connecting cities in order.

    Parameters:
        route (list): List of city indices in the order of travel.
        cities (list): List of city dictionaries with keys 'x' and 'y'.
        title (str): Title of the plot.
    """
    x_coords = [cities[city_id]["x"] for city_id in route] + [cities[route[0]]["x"]]
    y_coords = [cities[city_id]["y"] for city_id in route] + [cities[route[0]]["y"]]

    plt.figure(figsize=(8, 8))
    plt.plot(x_coords, y_coords, marker="o", linestyle="-", color="blue", label="Route")
    for city_id in route:
        plt.annotate(city_id, (cities[city_id]["x"], cities[city_id]["y"]), textcoords="offset points", xytext=(5, 5), ha="center")
    plt.title(title)
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.grid(True)
    plt.show()
