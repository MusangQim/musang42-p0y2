def input_temperature(temp_str: str) -> int:
    try:
        return int(temp_str)
    except Exception as error:
        print(f"Caught input_temperature error: {error}")
        return 0


def test_temperature() -> None:
    print("Input data is '25'")
    input_temperature("25")
    print("Temperature is now 25°C")
    print()
    print("Input data is 'abc'")
    input_temperature("abc")


def main():
    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
