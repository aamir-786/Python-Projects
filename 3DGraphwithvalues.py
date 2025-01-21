import numpy as np
from scipy.optimize import curve_fit, minimize
import matplotlib.pyplot as plt

# Define curve 1: A(x + y) = z
def curve1(vars, A):
    x, y = vars
    return A * (x + y)

# Define curve 2: A(x + y) + B*sin(x) = z
def curve2(vars, A, B):
    x, y = vars
    return A * (x + y) + B * np.sin(x)

# Function to fit the curve and store parameters
def fit_curve(points, curve_func, initial_guess):
    x_data = np.array([p[0] for p in points])
    y_data = np.array([p[1] for p in points])
    z_data = np.array([p[2] for p in points])

    # Use scipy's curve_fit with multiple independent variables
    params, _ = curve_fit(curve_func, (x_data, y_data), z_data, p0=initial_guess)
    return params

# Function to predict x for the next point that minimizes residuals
def predict_next_x(y, curve_func, params):
    def residual(x):
        z_pred = curve_func((x, y), *params)
        return z_pred**2  # Minimize residual

    result = minimize(residual, x0=0)  # Initial guess for x
    return result.x[0]

# Main iterative process
def iterative_fit(points, num_iterations):
    if len(points) < 1:
        raise ValueError("At least one point is required to start.")

    stored_params = []

    for i in range(num_iterations):
        if len(points) < 4:
            # Fit to curve 1
            initial_guess = [1.0] if not stored_params else stored_params[-1]
            params = fit_curve(points, curve1, initial_guess)
            stored_params.append(params)

            # Predict next point
            y_next = points[-1][1] + 1
            x_next = predict_next_x(y_next, curve1, params)
            z_next = params[0] * (x_next + y_next)
            points.append((x_next, y_next, z_next))

        else:
            # Fit to curve 2
            initial_guess = [stored_params[-1][0], 1.0] if len(stored_params[-1]) == 1 else stored_params[-1]
            params = fit_curve(points, curve2, initial_guess)
            stored_params.append(params)

            # Predict next point
            y_next = points[-1][1] + 1
            x_next = predict_next_x(y_next, curve2, params)
            z_next = params[0] * (x_next + y_next) + params[1] * np.sin(x_next)
            points.append((x_next, y_next, z_next))

    return points, stored_params

# Function to test the iterative process
def test_values():
    # Test case 1: Points ((1, 0, 2), (1, 1, 3))
    print("Test Case 1:\n")
    points = [(1, 0, 2), (1, 1, 3)]
    num_iterations = 8

    # Run the iterative process
    final_points, parameters = iterative_fit(points, num_iterations)

    # Print results
    print("Final Points:")
    for p in final_points:
        print(p)

    print("\nStored Parameters:")
    for params in parameters:
        print(params)

    # Visualize the process
    x_points = [p[0] for p in final_points]
    y_points = [p[1] for p in final_points]
    z_points = [p[2] for p in final_points]

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_points, y_points, z_points, color='blue', label='Generated Points')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Generated Points in 3D Space - Test Case 1')
    plt.legend()
    plt.show()

    # Test case 2: Points ((6, 0, 5), (9, 1, 7), (3, 2, 4))
    print("\nTest Case 2:\n")
    points = [(6, 0, 5), (9, 1, 7), (3, 2, 4)]
    num_iterations = 8

    # Run the iterative process
    final_points, parameters = iterative_fit(points, num_iterations)

    # Print results
    print("Final Points:")
    for p in final_points:
        print(p)

    print("\nStored Parameters:")
    for params in parameters:
        print(params)

    # Visualize the process
    x_points = [p[0] for p in final_points]
    y_points = [p[1] for p in final_points]
    z_points = [p[2] for p in final_points]

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_points, y_points, z_points, color='green', label='Generated Points')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Generated Points in 3D Space - Test Case 2')
    plt.legend()
    plt.show()

# Run the test
test_values()
