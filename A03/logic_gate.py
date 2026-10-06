import numpy as np

class LogicGate:
    """Hass the five gate and each one takes two inputs and returns either 0 or 1."""
    def _perceptron(self, x1, x2, w1, w2, th):
        x = np.array([x1, x2])
        w = np.array([w1, w2])
        if np.sum(x * w) > th:
            return 1
        return 0
    def and_gate(self, x1, x2):
        return self._perceptron(x1, x2, 0.5, 0.5, 0.7)
    def nand_gate(self, x1, x2):
        return self._perceptron(x1, x2, -2, -2, -3)
    def or_gate(self, x1, x2):
        return self._perceptron(x1, x2, 0.5, 0.5, 0.0)
    def nor_gate(self, x1, x2):
        return self._perceptron(x1, x2, -0.5, -0.5, -0.5)
    def xor_gate(self, x1, x2):
        return self.and_gate(self.or_gate(x1, x2), self.nand_gate(x1, x2))

def _show(name, fn):
    # Print the four input pairs and the result for one gate.
    print(name)
    print("x1 x2 | y")
    print("--------------------")
    for x1 in (0, 1):
        for x2 in (0, 1):
            print(f" {x1}  {x2} | {fn(x1, x2)}")
    print()
def main():
    # Create one LogicGate and print a table for each gate in it
    gate = LogicGate()
    _show("and_gate", gate.and_gate)

    _show("nand_gate", gate.nand_gate)

    _show("or_gate", gate.or_gate)

    _show("nor_gate", gate.nor_gate)

    _show("xor_gate", gate.xor_gate)

if __name__ == "__main__":
    main()
