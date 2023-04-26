# Graph-Problem
Implementation for Dijkstra Algorithm

When traveling in the vast land of Singapore, drivers need to abide by
the rule that fuel tanks must be at least ¾ full when driving out from
one city. However, due to the great difference in fuel prices in various
cities, drivers need to plan their route and refuel in some intermediate
cities along the way when going from one city to another, so as to
spend as little money as possible.
To simply this problem, we make the following assumptions:
1. The map of Singapore models each city as a node. Each node is
connected to not more than 8 other cities by an express way. Each
express way is modeled by an edge with length measured by km.
2. There is only one fuel station in each city, and the traveling within one city does not cost any
fuel. It is only required that when driving onto an expressway, the fuel tank must be at least ¾
full. There is no fuel station along the expressways, meaning you can only refuel in cities.
3. The average fuel consumption rate is 10 km for 1 liter of fuel, so the fuel tank is measured by
a unit of 1/10 liter, such that each unit of fuel allows a car (regardless of its weight, engine
capacity, and drivetrain) to travel 1 km.
4. Each query contains a pair of cities s and t, the expected output is the minimum amount spent
on fuel in cents. If the city t is not reachable from s no matter how you design your refuel plan,
output “impossible”.

Each input starts with two integers n (n ≤ 100) and m (m ≤ 800), the number of cities (nodes) and
number of expressways (edges) respectively. The next lines are the fuel prices in cents at each city
arranged according to city index, e.g., the fuel price in city 0, city 1, … city n-1. The next m lines
describe the expressways by the two indices of a pair of cities and the length in km. All
expressways are two-ways and there is at most one expressway between a pair of cities. The next
line contains one integer on the number of queries below, and each query is specified by 3 integers
c, s and t where c (c ≤ 200) is the fuel tank capacity measured in 1/10 liters, s is the index of the
starting city and t is the index of destination city. For each query, output the minimum amount
spent on fuel in cents. To further simplify computations, the length of expressways are all integers,
and fuel tank capacity c is a multiple of 4 such that ¾ capacity is always an integer.
