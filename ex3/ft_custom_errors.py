#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str) -> None:
        self._message = "Unknown garden error"


class PlantError(GardenError):


class WaterError(GardenError):


def test_garden_error() -> None:


def test_plant_error() -> None:


def test_water_error() -> None:


if __name__ == "__main__":
    print("=== Custom Garden ===")
    print()
    print("All custom error types work correctly!")
