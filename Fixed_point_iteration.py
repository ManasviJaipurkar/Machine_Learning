import math
def f(x):
    return math.cos(x)
x = 0.5

for i in range(10):
    x_new = f(x)
    print(f"step{i+1} : x ={x}")
    x = x_new
    
print(f"After 10 steps: x~~ {x}")
print(f"Check cos({x}) = {math.cos(x)}") 

diff = x_new - x
print(diff)



# 2^x - 5x + 2
# x = g(x)

import math
def f(x):
    return 2**x - 5*x + 2

def g(x):
    return (2**x + 2)/ 5

x = 2.0

for i in range(10):
    x_new = g(x)
    print(x)
    error = (x_new - x)
    x = x_new
print("Error is", error)
print(f"final approximation: x = {x}")

import math

def f(x):
    return 2**x - 5*x + 2

def g(x):
    return (2**x + 2) / 5

# Initialize x with x0
x = 2.0

print(f"Initial value: x = {x}")

for i in range(10):
    x_new = g(x)
    error = abs(x_new - x)  
    print(f"Iteration {i+1}: x = {x_new}, error = {error}")
    x = x_new  

print(f"\nFinal approximation: x = {x}")
print(f"f(x) = {f(x)}")


## x^3 - 2x - 5 = 0

def f(x):
    return x**3 - 2*x - 5

def g(x):
    return (2*x - 5)*(1/3)

# Initialize with x0
x = 2.0

print(f"Initial value: x = {x}")
print()

for i in range(10):
    x_new = g(x)
    error = x_new - x  # Compare to previous x value, not initial x0
    print(f"Step {i+1}: x = {x_new:.10f}, Error = {error:.10f}")
    x = x_new  # Update x for next iteration

print(f"\nFinal approximation is: {x:.10f}")
print(f"f(x) = {f(x):.10f}")
