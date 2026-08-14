#!/usr/bin/env python3
"""Minimal Go2 scouting example for stage 1."""

from agrokit.go2 import Go2

DISEASES = {"powdery_mildew", "leaf_rust"}


def main() -> None:
    go2 = Go2(sim=True)

    for row in go2.field.rows:
        go2.nav.follow_row(row, speed=0.4)

        for det in go2.vision.detect(model="agro_yolo"):
            if det.label in DISEASES:
                go2.report.add_finding(det.label, go2.nav.pose, det.score)

    go2.report.export("field_report.json")


if __name__ == "__main__":
    main()
