#!/usr/bin/env python3
"""Minimal G1 sorting example for stage 1."""

from agrokit.g1 import G1


def main() -> None:
    g1 = G1(sim=True)

    for fruit in g1.vision.detect(model="agro_yolo"):
        x, y, z = fruit.x, fruit.y, fruit.z
        g1.arm.move_to_point(x, y, z)
        g1.hand.set_gesture("PINCH", speed=0.3)

        tray = g1.trays.get(fruit.grade, g1.trays["C"])
        g1.arm.move_to_point(*tray)
        g1.hand.set_gesture("OPEN")

    print("[example] sorting demo complete")


if __name__ == "__main__":
    main()
