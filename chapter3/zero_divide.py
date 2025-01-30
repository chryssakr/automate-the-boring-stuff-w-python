def spam(divideBy: float) -> float:
    """Attempts to divide 42 by the given number

    Args:
        divideBy (int or float): The number to divide 42 by.

    Returns:
        float: The result of 42 divided by divideBy.

    Raises:
        ValueError: If divideBy is zero.
    """
    if divideBy == 0:
        raise ValueError("Can not divide by zero!")
    return 42 / divideBy


def main() -> None:
    try:
        print(spam(0))
    except ValueError as e:
        print(f"Handled error: {e}")

    print(spam(2))
    print(spam(12))
    print(spam(1))


if __name__ == "__main__":
    main()
