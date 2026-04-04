def input_temperature(temp_str: str) -> int:
    try:
        return int(temp_str)
    except Exception as error:
        print(f"Caught input_temperature error: {error}")


def test_temperature() -> None:
    number_input = input_temperature("25")
    print(f"Input data is '{number_input}'")
    print(f"Temperature is now {number_input}°C")
    print()
    print("Input data is 'abc'") 
    str_input = input_temperature("abc")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")
