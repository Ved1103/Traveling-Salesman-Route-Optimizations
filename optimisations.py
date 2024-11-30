import random
import math
import numpy as np
from utils import calculate_route_distance

# --- 2-opt optimization ---
def two_opt(route, cities):
    """
    Apply the 2-opt optimization technique to a given route to improve it.
    The 2-opt method removes crossing paths by reversing segments of the route.
    """
    best_route = route
    best_distance = calculate_route_distance(best_route, cities)

    for i in range(len(route) - 1):
        for j in range(i + 2, len(route)):
            # Create a new route by reversing the segment between i and j
            new_route = route[:i] + route[i:j+1][::-1] + route[j+1:]

            # Calculate the new distance
            new_distance = calculate_route_distance(new_route, cities)

            # If the new route is better, update the best_route and best_distance
            if new_distance < best_distance:
                best_route = new_route
                best_distance = new_distance

    return best_route


# --- Simulated Annealing ---
def simulated_annealing(route, cities, initial_temperature=1000, cooling_rate=0.995, max_iterations=1000):
    """
    Apply Simulated Annealing to find a better solution.
    Simulated Annealing uses random swaps to explore the solution space and escapes local minima by allowing worse solutions at a decreasing temperature.
    """
    current_route = route
    current_distance = calculate_route_distance(current_route, cities)
    best_route = current_route
    best_distance = current_distance

    temperature = initial_temperature
    iteration = 0

    while iteration < max_iterations and temperature > 1:
        # Randomly select two cities to swap
        new_route = current_route[:]
        i, j = random.sample(range(len(route)), 2)
        new_route[i], new_route[j] = new_route[j], new_route[i]

        # Calculate the new distance after the swap
        new_distance = calculate_route_distance(new_route, cities)

        # If the new route is better, accept it
        if new_distance < current_distance:
            current_route = new_route
            current_distance = new_distance

            # If the new route is the best so far, update the best_route and best_distance
            if new_distance < best_distance:
                best_route = new_route
                best_distance = new_distance
        else:
            # Accept the new route with a probability based on temperature
            acceptance_prob = math.exp((current_distance - new_distance) / temperature)
            if random.random() < acceptance_prob:
                current_route = new_route
                current_distance = new_distance

        # Cool down the temperature
        temperature *= cooling_rate
        iteration += 1

    return best_route


# --- Hybrid Optimization ---
def hybrid_optimization(route, cities):
    """
    Combine 2-opt and Simulated Annealing to optimize the route further.
    First, apply 2-opt to improve the route, then use Simulated Annealing to explore the solution space and escape local minima.
    """
    print("Applying 2-opt optimization...")
    route = two_opt(route, cities)
    print("2-opt completed. Now applying Simulated Annealing...")

    route = simulated_annealing(route, cities)
    print("Simulated Annealing completed.")

    return route


# --- Black Hole Optimization ---
class BlackHoleOptimization:
    def __init__(self, cities, population_size=50, max_iterations=1000):
        self.cities = cities
        self.population_size = population_size
        self.max_iterations = max_iterations
        self.best_route = None
        self.best_distance = float('inf')
        self.black_hole = None
    
    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            route = random.sample(range(len(self.cities)), len(self.cities))
            population.append(route)
        return population

    def update_black_hole(self, population):
        for route in population:
            distance = calculate_route_distance(route, self.cities)
            if distance < self.best_distance:
                self.best_distance = distance
                self.best_route = route
                self.black_hole = route
    
    def gravitational_pull(self, population):
        new_population = []
        for route in population:
            new_route = []
            for i, city in enumerate(route):
                # Pull particles closer to the black hole by a gravity-like force
                if random.random() < 0.5:  
                    new_route.append(self.black_hole[i])  
                else:
                    new_route.append(city)
            new_population.append(new_route)
        return new_population

    def optimize(self):
        population = self.initialize_population()
        
        for iteration in range(self.max_iterations):
            self.update_black_hole(population)
            population = self.gravitational_pull(population)
        
        return self.best_route, self.best_distance


# --- Ant Colony Optimization ---
class AntColonyOptimization:
    def __init__(self, cities, num_ants=50, max_iterations=1000, alpha=1, beta=2, evaporation_rate=0.5, Q=100):
        self.cities = cities
        self.num_ants = num_ants
        self.max_iterations = max_iterations
        self.alpha = alpha  # Pheromone importance
        self.beta = beta    # Distance priority
        self.evaporation_rate = evaporation_rate
        self.Q = Q          # Constant to control pheromone intensity
        self.pheromones = np.ones((len(cities), len(cities)))  # Initialize pheromone matrix
        self.best_route = None
        self.best_distance = float('inf')

    def calculate_probabilities(self, ant, visited):
        probabilities = []
        current_city = ant[-1]
        total_pheromone = 0
        for i in range(len(self.cities)):
            if i not in visited:
                pheromone = self.pheromones[current_city][i] ** self.alpha
                distance = calculate_route_distance([current_city, i], self.cities) ** (-self.beta)
                total_pheromone += pheromone * distance
                probabilities.append(pheromone * distance)
            else:
                probabilities.append(0)
        
        # Normalize probabilities
        if total_pheromone > 0:
            probabilities = [p / total_pheromone for p in probabilities]
        return probabilities
    
    def simulate_ants(self):
        all_ants = []
        for _ in range(self.num_ants):
            ant = [random.randint(0, len(self.cities) - 1)]  # Random starting city
            visited = set(ant)
            
            while len(visited) < len(self.cities):
                probabilities = self.calculate_probabilities(ant, visited)
                next_city = random.choices(range(len(self.cities)), weights=probabilities)[0]
                ant.append(next_city)
                visited.add(next_city)
            
            all_ants.append(ant)
        return all_ants
    
    def update_pheromones(self, all_ants):
        # Evaporate pheromones
        self.pheromones *= (1 - self.evaporation_rate)
        
        for ant in all_ants:
            route_distance = calculate_route_distance(ant, self.cities)
            pheromone_deposit = self.Q / route_distance
            
            for i in range(len(ant) - 1):
                self.pheromones[ant[i]][ant[i+1]] += pheromone_deposit

    def optimize(self):
        for iteration in range(self.max_iterations):
            all_ants = self.simulate_ants()
            self.update_pheromones(all_ants)
            
            for ant in all_ants:
                route_distance = calculate_route_distance(ant, self.cities)
                if route_distance < self.best_distance:
                    self.best_distance = route_distance
                    self.best_route = ant
        
        return self.best_route, self.best_distance
