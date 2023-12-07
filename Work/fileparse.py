# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=","):
    """Parse a CSV file into a list of records."""

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
        for row in rows:
            if not row:
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]

            # Perform type converstion of row values if types provided
            if types:
                row = [func(val) for func, val in zip(types, row)]

            # Make a dictionary, or tuple if not has_headers
            record = dict(zip(headers, row)) if has_headers else tuple(row)

            records.append(record)

    return records
