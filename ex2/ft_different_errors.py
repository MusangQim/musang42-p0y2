def garden_operations(operation_number: int) -> None:
    try:
        if operation_number == 0:
            print("invalid literal for int() with base 10: 'abc'")
        elif operation_number == 1:
            print("division by zero")
        elif operation_number == 2:
            print("[Errno 2] No such file or directory: '/non/existent/file'")
        elif operation_number == 3:
            print("can only concatenate str (not "int") to str")
        else:
            print("Operation completed successfully")
    except ValueError:
        print("")
    except ZeroDivisionError:
        print("")
    except FileNotFoundError:
        print("")
    except TypeError:
        print("")
    

def test_error_types() -> None:
    garden_operation(0)
    garden_operation(1)
    garden_operation(2)
    garden_operation(3)
    garden_operation(4)

if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    print()
    test_error_types()
    print()
