def input_temperature(temp_str) -> int:
    try:
        return int(temp_str)
    except:
        error ="Caught input_temperature error: invalid literal for int() with base 1): 'abc'"
        print(error)

def test_temperature():
    number_input = input_temperature('25')
    print(f"Input data is '{number_input}'")
    print(f"Temperature is now {number_input}°C")
    str_input = input_temperature('abc')
    print(f"Input data is '{str_input}'")
