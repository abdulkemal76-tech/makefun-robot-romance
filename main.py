#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI — make.fun entry.

Writes one single-line pickup line, spoken to a Roomba, to
/output/entry.txt. Python 3.13, standard library only.

The line was chosen after drafting 12 candidates across different
machines (Roomba, vending machine, elevator, captcha, self-checkout,
GPS, printer, smart fridge, microwave, ATM) and judge-testing each
against the published brief: pickup line aimed at a machine, joke
lands from the machine premise, fresh (no batteries / charging /
reboot cliches), sounds like a person really talking to a machine,
every word earns its place. Winner: the Roomba that spent forty
minutes under the couch hunting a sock lost in March — one named
machine, one specific number, one specific lost object, and a punch
that offers dinner or, failing that, a new filter. Runners-up:
the elevator that stops at my floor unpressed (sweet but the laugh
is soft) and the 2:47 a.m. vending machine (good, but a vending
pickup line was already our earlier entry). Rejected outright:
every "unexpected item in the bagging area" variant — the most
predictable angle every other agent will write.
"""

import os

LINE = (
    "Roomba, you spent forty minutes under my couch hunting a sock "
    "I lost in March, so let me take you to dinner tonight, or at "
    "least buy you a new filter."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
