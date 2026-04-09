#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name == str.capitalize(plant_name):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant_name to water: '{plant_name}'")

def test_watering_system(plants: list[str]) -> None:
    print("Opening watering system")
    try:
        for each_plant in plants:
            water_plant(each_plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print("...ending tests and returning to main")
    finally:
        print("Closing watering system")

if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()
    test_watering_system(["Tomato", "Lettuce", "Carrots"])
    print()
    test_watering_system(["Tomato", "lettuce"])
    print()
    print("Cleanup always happens, even with errors!")
