import numpy as np
from scipy.integrate import quad

# Define the function
def f(x):
    return x ** 2

# Define the boundaries of integration
a = 0 # Lower bound
b = 2 # Upper bound

# Analytical calculation of the integral
integral_analytical, _ = quad(f, a, b)
print("Analytical value of the integral:", integral_analytical)

# Estimate the integral using Monte Carlo method for n = 10000
n = 10000
x_random = np.random.uniform(a, b, n)
y_random = np.random.uniform(0, f(b), n)
points_under_curve = sum(y_random <= f(x_random))
rectangle_area = (b - a) * f(b)
integral_monte_carlo_10000 = rectangle_area * (points_under_curve / n)
print("Estimated value of the integral using Monte Carlo method (n = 10000):", integral_monte_carlo_10000)

# Estimate the integral using Monte Carlo method for n = 100000
n = 100000
x_random = np.random.uniform(a, b, n)
y_random = np.random.uniform(0, f(b), n)
points_under_curve = sum(y_random <= f(x_random))
rectangle_area = (b - a) * f(b)
integral_monte_carlo_100000 = rectangle_area * (points_under_curve / n)
print("Estimated value of the integral using Monte Carlo method (n = 100000):", integral_monte_carlo_100000)

# Compare the results
error_10000 = abs(integral_analytical - integral_monte_carlo_10000)
error_100000 = abs(integral_analytical - integral_monte_carlo_100000)
print("Absolute error between analytical and Monte Carlo results (n = 10000):", error_10000)
print("Absolute error between analytical and Monte Carlo results (n = 100000):", error_100000)

# Conclusion
if error_10000 < 0.01:  # Adjust threshold as needed
    print("The Monte Carlo method provides an accurate estimation of the integral for n = 10000.")
else:
    print("The Monte Carlo method may need more samples for n = 10000 to achieve accurate estimation.")

if error_100000 < 0.01:  # Adjust threshold as needed
    print("The Monte Carlo method provides an accurate estimation of the integral for n = 100000.")
else:
    print("The Monte Carlo method may need more samples for n = 100000 to achieve accurate estimation.")
