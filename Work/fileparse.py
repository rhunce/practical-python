# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(
    filename,
    select=None,
    types=None,
    has_headers=True,
    delimiter=",",
    silence_errors=False,
):
    """Parse a CSV file into a list of records."""
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        # Read the file headers
        headers = None
        if has_headers:
            headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        indices = None
        if has_headers:
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []

        records = []
        for idx, row in enumerate(rows, start=1):
            if not row:
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]

            # Perform type converstion of row values if types provided
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if silence_errors:
                        continue
                    print(f"Row {idx}: Could not convert {row}")
                    print(f"Reason: {e}")
                    continue

            # Make a dictionary, or tuple if not has_headers
            record = dict(zip(headers, row)) if has_headers else tuple(row)
            records.append(record)

    return records
