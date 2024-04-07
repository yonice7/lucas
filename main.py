import os
import re
import pandas


def main():
    b = selected_banks()
    return b


def pdf_or_csv():
    return {'zinli': 'pdf', 'fiwind': 'csv', 'mp': 'csv', 'brubank': 'pdf', 'littio': 'pdf', 'lemon': 'csv'}


def bank_list():
    # ['brubank', 'littio', 'belo'] -- this will work for zinli, fiwind and mp for the moment
    return ['zinli', 'fiwind', 'mp']


def selected_banks():
    return [b for b in bank_list() if input(f"Do you want to analyze {b}? (Y/N) ").lower() == "y"]


if __name__ == "__main__":
    main()
