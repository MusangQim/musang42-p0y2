def garden_operations(operation_number: int) -> None:
    try:
        if operation_number == 0:
            int("abc")
        elif operation_number == 1:
            _ = 1 / 0
        elif operation_number == 2:
            open("/non/existent/file")
        elif operation_number == 3:
            _ = "hello" + 1
        else:
            print("Operation completed successfully")
    except ValueError as a:
        print(f"Caught ValueError: {a}")
    except ZeroDivisionError as b:
        print(f"Caught ZeroDivisionError: {b}")
    except FileNotFoundError as c:
        print(f"Caught FileNotFoundError: {c}")
    except TypeError as d:
        print(f"Caught TypeError: {d}")


def test_error_types() -> None:
    print("Testing operation 0...")
    garden_operations(0)
    print("Testing operation 1...")
    garden_operations(1)
    print("Testing operation 2...")
    garden_operations(2)
    print("Testing operation 3...")
    garden_operations(3)
    print("Testing operation 4...")
    garden_operations(4)


def main():
    print("=== Garden Error Types Demo ===")
    print()
    test_error_types()
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    main()
