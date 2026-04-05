def input_temperature(temp_str: str) -> int:
    try:
        tempinput = int(temp_str)
        if tempinput < 0:
            raise ValueError(f"{tempinput}°C is too cold for plants (min 0°C)")
        elif tempinput > 40:
            raise ValueError(f"{tempinput}°C is too hot for plants (max 40°C)")
        return tempinput
    except Exception as error:
        print(f"Caught input_temperature error: {error}")


def test_temperature() -> None:
    print("Input data is '25'")
    num_input = input_temperature('25')
    if num_input is not None:
        print(f"Temperature is now {num_input}°C")
    print()
    print("Input data is 'abc'")
    input_temperature('abc')
    print()
    print("Input data is '100'")
    input_temperature('100')
    print()
    print("Input data is '-50'")
    input_temperature('-50')


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")
