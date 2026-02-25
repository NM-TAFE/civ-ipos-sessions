from src.calculator import add


def main():
    # Integer
    print(add(2, 3))
    # Float
    print(add(3.5, 2.1))

    print(add(1 + 2j, 3 - 1j))


if __name__ == "__main__":
    main()
