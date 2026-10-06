from logic_gate import LogicGate
INPUTS = ((0, 0), (0, 1), (1, 0), (1, 1))
# Truth tables here are form our lecture 
EXPECTED = {
    "and_gate": (0, 0, 0, 1),
    "nand_gate": (1, 1, 1, 0),
    "or_gate": (0, 1, 1, 1),
    "nor_gate": (1, 0, 0, 0),
    "xor_gate": (0, 1, 1, 0),
}
def show_gate(name, fn):
    print(name)
    print("x1 x2 | y")
    print("---------")
    outputs = []
    for x1, x2 in INPUTS:
        y = fn(x1, x2)
        outputs.append(y)
        print(f" {x1}  {x2} | {y}")
    print()
    return tuple(outputs)
def main():
   # Runs all the gates and stops if a table doest match
    gate = LogicGate()
    functions = (
        ("and_gate", gate.and_gate),

        ("nand_gate", gate.nand_gate),

        ("or_gate", gate.or_gate),

        ("nor_gate", gate.nor_gate),

        ("xor_gate", gate.xor_gate),
    )
    for name, func in functions:
        outputs = show_gate(name, func)
        if outputs != EXPECTED[name]:
            raise AssertionError(f"{name} returned {outputs}, expected {EXPECTED[name]}")

    print("All gates match thetruth tables")

if __name__ == "__main__":
    main()
