import numpy as np

class MultilayerPerceptron:
    """3 inputs -> 5 -> 5 -> 2 -> 2 outputs. sigmoid on layers 1-3, relu on layer 4."""
    def __init__(self):
        self.network = network = {}
        # input (3) -> layer 1 (5): 3x5
        network["w1"] = np.array([[0.3, 0.9, 1.5, -0.6, 1.2],
                                  [0.6, -1.2, 1.8, 0.3, -0.9],
                                  [-1.5, 0.6, 0.3, 0.9, 0.6]])
        network["b1"] = np.array([0.1, 0.2, -0.1, 0.1, 0.0])
        # layer 1 (5) -> layer 2 (5): 5x5
        network["w2"] = np.array([[0.6, -0.3, 1.2, 0.9, -0.6],
                                  [1.5, 0.6, -0.9, 0.3, 1.2],
                                  [-1.2, 0.9, 0.6, -0.3, 0.3],
                                  [0.3, 1.2, 0.3, 0.6, -0.9],
                                  [0.9, -0.6, 1.5, -1.2, 0.6]])
        network["b2"] = np.array([0.1, -0.1, 0.2, 0.0, 0.1])
        # layer 2 (5) -> layer 3 (2): 5x2
        network["w3"] = np.array([[1.2, -1.6],
                                  [-0.8, 2.0],
                                  [1.6, 0.4],
                                  [0.4, -1.2],
                                  [-2.0, 0.8]])
        network["b3"] = np.array([0.1, -0.2])
        # layer 3 (2) -> layer 4 / output (2): 2x2
        network["w4"] = np.array([[2.0, -1.5],
                                  [-1.5, 2.0]])
        network["b4"] = np.array([0.0, -0.1])
    def sigmoid(self, s):
        return 1 / (1 + np.exp(-s))
    def relu(self, s):
        return np.maximum(0, s)
    def forward(self, x):
        # layer 1 with sigmoid
        a1 = np.dot(x, self.network["w1"]) + self.network["b1"]
        z1 = self.sigmoid(a1)
        # layer 2 with sigmoid
        a2 = np.dot(z1, self.network["w2"]) + self.network["b2"]
        z2 = self.sigmoid(a2)
        # layer 3 with sigmoid
        a3 = np.dot(z2, self.network["w3"]) + self.network["b3"]
        z3 = self.sigmoid(a3)
        # layer 4 (output) with relu
        a4 = np.dot(z3, self.network["w4"]) + self.network["b4"]
        y = self.relu(a4)
        return y
