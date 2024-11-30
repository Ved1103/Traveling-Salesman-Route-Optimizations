import random
import numpy as np
from utils import calculate_route_distance
from optimisations import two_opt, simulated_annealing, hybrid_optimization, BlackHoleOptimization, AntColonyOptimization

# --- City Generation ---
def generate_random_cities(num_cities, x_range=(0, 100), y_range=(0, 100)):
    """
    Generate random coordinates for cities within the given x and y range.
    """
    cities = []
    for _ in range(num_cities):
        x = random.randint(x_range[0], x_range[1])
        y = random.randint(y_range[0], y_range[1])
        cities.append((x, y))
    return cities

# --- Main Logic ---
def main():
    # Number of cities and their coordinates
    num_cities = 10
    cities = generate_random_cities(num_cities)

    # Generate an initial random route
    initial_route = random.sample(range(num_cities), num_cities)

    # Print the initial route and distance
    print("Initial Route:", initial_route)
    print("Initial Distance:", calculate_route_distance(initial_route, cities))

    # --- Apply 2-opt Optimization ---
    print("\n--- Applying 2-opt Optimization ---")
    optimized_route_2opt = two_opt(initial_route, cities)
    print("Optimized Route (2-opt):", optimized_route_2opt)
    print("Optimized Distance (2-opt):", calculate_route_distance(optimized_route_2opt, cities))

    # --- Apply Simulated Annealing Optimization ---
    print("\n--- Applying Simulated Annealing ---")
    optimized_route_sa = simulated_annealing(initial_route, cities)
    print("Optimized Route (Simulated Annealing):", optimized_route_sa)
    print("Optimized Distance (Simulated Annealing):", calculate_route_distance(optimized_route_sa, cities))

    # --- Apply Hybrid Optimization (2-opt + Simulated Annealing) ---
    print("\n--- Applying Hybrid Optimization ---")
    optimized_route_hybrid = hybrid_optimization(initial_route, cities)
    print("Optimized Route (Hybrid):", optimized_route_hybrid)
    print("Optimized Distance (Hybrid):", calculate_route_distance(optimized_route_hybrid, cities))

    # --- Apply Black Hole Optimization ---
    print("\n--- Applying Black Hole Optimization ---")
    bho = BlackHoleOptimization(cities)
    best_route_bho, best_distance_bho = bho.optimize()
    print("Optimized Route (Black Hole Optimization):", best_route_bho)
    print("Optimized Distance (Black Hole Optimization):", best_distance_bho)

    # --- Apply Ant Colony Optimization ---
    print("\n--- Applying Ant Colony Optimization ---")
    aco = AntColonyOptimization(cities)
    best_route_aco, best_distance_aco = aco.optimize()
    print("Optimized Route (Ant Colony Optimization):", best_route_aco)
    print("Optimized Distance (Ant Colony Optimization):", best_distance_aco)

if __name__ == "__main__":
    main()
