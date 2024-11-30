# TSP-Optimization

## Project Overview
![TSP Optimization Animation](https://blog.optibus.com/hs-fs/hubfs/Travelling%20Salesman%20III%20(GIF)%20(1).gif?width=1920&height=1080&name=Travelling%20Salesman%20III%20(GIF)%20(1).gif)

# TSP Optimization Project

## Overview

This project implements multiple algorithms to solve the **Traveling Salesman Problem (TSP)**. The main objective of TSP is to find the shortest possible route that visits a given set of cities and returns to the origin city. The project leverages several optimization techniques to improve the route calculation, including **Simulated Annealing**, **2-opt optimization**, **Black Hole Optimization**, and **Ant Colony Optimization**. Each technique is explained and applied in the context of solving the TSP.

## Table of Contents

- [Project Description](#project-description)
- [Algorithms Used](#algorithms-used)
  - [2-opt Optimization](#2-opt-optimization)
  - [Simulated Annealing](#simulated-annealing)
  - [Hybrid Optimization](#hybrid-optimization)
  - [Black Hole Optimization](#black-hole-optimization)
  - [Ant Colony Optimization](#ant-colony-optimization)
- [Project Structure](#project-structure)


---

## Project Description

The Traveling Salesman Problem (TSP) is a classic problem in computer science, combinatorial optimization, and operations research. This project provides several optimization methods to find near-optimal solutions to the TSP. The project is designed to explore the following optimization techniques:

- **2-opt Optimization**: A local search method that aims to improve a given solution by reversing sections of the route to eliminate any intersecting paths.
- **Simulated Annealing**: A probabilistic optimization algorithm inspired by the annealing process in metallurgy. It allows for occasional uphill moves to escape local minima.
- **Hybrid Optimization**: A combination of 2-opt and Simulated Annealing to refine solutions by applying both local and global optimization techniques.
- **Black Hole Optimization**: A population-based search method that simulates the process of gravitational attraction to find the optimal solution.
- **Ant Colony Optimization**: A nature-inspired heuristic based on the behavior of ants searching for food, where pheromones guide the search process.

This project aims to provide a well-structured solution to the TSP using Python, and it is highly extensible to accommodate additional optimization algorithms.

---

## Algorithms Used

### 2-opt Optimization

2-opt is a local search algorithm that removes intersecting paths by reversing segments of the route. The algorithm starts with an initial solution and iteratively swaps pairs of cities to reduce the total distance of the route. This method is particularly effective at refining solutions and is used as a first step in the hybrid optimization algorithm.

**Key Concepts**:
- Swap two cities in the route.
- Reverse the order of the cities between the swapped cities to eliminate crossovers.
- Recalculate the total distance and repeat until no further improvement is possible.

### Simulated Annealing

Simulated Annealing is inspired by the physical process of annealing, where a metal is heated and then slowly cooled to remove defects. This algorithm mimics this process by accepting worse solutions with a decreasing probability as the algorithm progresses. This enables the algorithm to escape local minima and explore more potential solutions.

**Key Concepts**:
- Randomly swap two cities in the route.
- Accept the new route if it improves the solution.
- Accept worse solutions with a decreasing probability as the temperature cools.

### Hybrid Optimization

The Hybrid Optimization algorithm combines 2-opt and Simulated Annealing to take advantage of both local and global search methods. The process begins by applying 2-opt to improve the initial route, followed by Simulated Annealing to escape local minima and fine-tune the solution.

### Black Hole Optimization

Black Hole Optimization is a population-based metaheuristic inspired by the behavior of gravitational forces around a black hole. It simulates particles (routes) being attracted to a central black hole (the best route). As the algorithm iterates, the routes are pulled towards the black hole, refining the solutions.

**Key Concepts**:
- Initialize a population of routes.
- Each route is influenced by the "gravitational pull" of the best route.
- After several iterations, the best route converges to the optimal solution.

### Ant Colony Optimization

Ant Colony Optimization is a swarm intelligence-based algorithm that simulates the behavior of ants foraging for food. The ants leave pheromone trails that influence the paths of other ants. The algorithm uses a pheromone matrix to guide the search for the best route.

**Key Concepts**:
- Initialize a population of ants.
- Ants construct routes based on pheromone levels and distance.
- Pheromone levels are updated after each iteration, guiding future ants towards shorter routes.

---




### Project Structure
```bash
TSP-Optimization/
├── data/                  
│   └── cities.csv        
├── .gitignore             
├── LICENSE                
├── README.md              
├── main.py                
├── optimisations.py       
├── requirements.txt       
├── tsp.py                 
└── utils.py               
```



