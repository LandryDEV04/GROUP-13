# Identity Card Generator (CLI)

A small interactive Python program that gathers personal information, validates inputs (dates, height, gender, etc.), and outputs formatted text-based identity cards.

## Features

- Guided data collection for a person (name, birth date, address, and more).
- Strict validation:
  - birth years within a sensible range (1900 → current year),
  - months accepted as numbers or names (full/abbreviation),
  - days checked against the calendar (leap years handled),
  - positive height only and gender limited to `M` or `F`.
- Unique ID generation derived from the name and birth date.
- Detailed ASCII rendering of each card, with a session history.

## Requirements

- Python 3.9 or newer (standard library only).

## Installation

```bash
git clone <your-repo-or-copy>
cd Project13
```

## Usage

```bash
python part2.py
```

From the main menu:

1. `1 • Create cards` starts the collection process for N cards.
2. `2 • Show all cards` reprints the cards generated during the session.
3. `3 • Quit` exits the program.

## Structure

- `part2.py`: hosts the `Person`, `IDCard`, and `IDCardGenerator` classes plus the CLI loop (`main()`).
- `README.md`: this document.

## Possible Improvements

- Persist cards to disk (JSON/CSV) to keep them between sessions.
- Add unit tests by decoupling validation logic from console I/O.
- Extend validation (phone formats, address checks, ID uniqueness).

