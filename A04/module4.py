import numpy as np
from multilayer_perceptron import MultilayerPerceptron

# Example inputs, 3 values each because the input layer has 3 neurons.
INPUTS = (
    (0.0, 0.0, 0.0),
    (1.0, 0.5, -1.0),
    (0.2, -0.7, 0.9),
    (-1.0, 2.0, 0.5),
    (3.0, -2.0, 1.0),
)
def main():
    mlp = MultilayerPerceptron()
    for x in INPUTS:
        x = np.array(x)
        y = mlp.forward(x)
        print("input:", x, "-> output:", np.round(y, 4))
        # Output layer has 2 neurons and relu never goes below 0.
        if y.shape != (2,) or np.any(y < 0):
            raise AssertionError(f"bad output {y} for input {x}")

    X = np.array(INPUTS)
    Y = mlp.forward(X)
    print()
    print("batch outputshape:", Y.shape)
    for x, y in zip(INPUTS, Y):
        if not np.allclose(y, mlp.forward(np.array(x))):
            raise AssertionError(f"batch output doesn't match for input {x}")

    print("Aall of the forward propagation checks passed")

if __name__ == "__main__":
    main()
