def lagrange_interpolation(points):
    assert points, "The tuple of points cannot be empty."
    assert isinstance(points, tuple) and isinstance(points[0], tuple), "The points must be input as a tuple of tuples."
    coefficients = [(0, 0) for _ in range(len(points))]
    for i in range(len(points)):
        x_value = points[i][0]
        numerators = []
        denominator = 1
        for j in range(len(points)):
            if j != i:
                denominator *= (x_value - points[j][1])

    
