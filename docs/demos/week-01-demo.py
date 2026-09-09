"""Week 1 Demo: Simulate rolling a six-sided die ten times.

Run this script from a terminal:
    python week-01-demo.py
"""

import random


def roll_dice(num_rolls: int = 10, sides: int = 6) -> list[int]:
    """Simulate rolling a die and return the list of results."""
    return [random.randint(1, sides) for _ in range(num_rolls)]


def main() -> None:
    rolls = roll_dice(num_rolls=10)
    average = sum(rolls) / len(rolls)
    print(f"Rolls: {rolls}")
    print(f"Average: {average:.2f}")


if __name__ == "__main__":
    main()