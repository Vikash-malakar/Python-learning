import ast
import operator


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg
}


def calculate(node):
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value

        raise ValueError("Invalid number")

    if isinstance(node, ast.BinOp):
        left = calculate(node.left)
        right = calculate(node.right)

        operation = OPERATORS.get(type(node.op))

        if operation is None:
            raise ValueError("Unsupported operator")

        return operation(left, right)

    if isinstance(node, ast.UnaryOp):
        value = calculate(node.operand)

        operation = OPERATORS.get(type(node.op))

        if operation is None:
            raise ValueError("Unsupported operator")

        return operation(value)

    raise ValueError("Invalid expression")


def main():
    print("\n" + "=" * 50)
    print("        🧮 MATH EXPRESSION CALCULATOR")
    print("=" * 50)

    print("\nExample:")
    print("10 + 20 * 5")
    print("(100 - 20) / 4")
    print("2 ** 5")

    expression = input("\nEnter expression: ").strip()

    try:
        tree = ast.parse(
            expression,
            mode="eval"
        )

        result = calculate(tree.body)

        print(f"\n✅ Result: {result}")

    except ZeroDivisionError:
        print("❌ Cannot divide by zero.")

    except Exception:
        print("❌ Invalid expression.")


if __name__ == "__main__":
    main()