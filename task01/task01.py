from pulp import *

# Create a maximization problem
prob = LpProblem("Production Optimization", LpMaximize)

# Define decision variables
l = LpVariable("Lemonade_units", lowBound=0, cat='Integer')  # Number of units of Lemonade
f = LpVariable("FruitJuice_units", lowBound=0, cat='Integer')  # Number of units of Fruit Juice

# Define objective function
prob += l + f, "Total_products"

# Define constraints
prob += 2*l + f <= 100, "Water_constraint"
prob += l <= 50, "Sugar_constraint"
prob += l <= 30, "LemonJuice_constraint"
prob += 2*f <= 40, "FruitPuree_constraint"

# Solve the problem
prob.solve()

# Print the solution status
print("Status:", LpStatus[prob.status])

# Print the optimal solution
print("Optimal Solution:")
for v in prob.variables():
    print(v.name, "=", v.varValue)
print("Total Products =", value(prob.objective))
