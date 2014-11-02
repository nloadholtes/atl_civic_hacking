"""
wwg_market.py - Nick Loadholtes <nick@ironboundsoftware.com> Oct 2014

This quick-and-dirty script was written to analyze some data provided at an ATLHack event
on "Food Security". The data was in spreadsheets from Wholesome Wave Georgia and it concerned
Farmer's Markets and EBT/SNAP transactions.

The functions below work on a subset of the spreadsheet data, simply copy/pasted into CSV format
so that it could be quickly/easily analyzed.

The commandline to run this is:

python wwg_market.py <path_to_the_csv_data>

"""
import sys
import csv
import argparse


def csv_to_dict(data, key_col):
    output = {}
    for row in data:
        if row[key_col] == '':
            continue
        key_data = output.get(row[key_col], [])
        key_data.append(row[key_col + 1:])
        output[row[key_col]] = key_data
    return output


def main(filename):
    print("opening: %s" % filename)
    cdata = csv.reader(open(filename, 'r'))
    data = []
    cdata.next()
    for row in cdata:
        data.append(row)
    vendors = csv_to_dict(data, 1)
    for vendor, day_data in vendors.items():
        t = analyze_paper_vs_swipe(day_data)
        print("%s avgerage of %.2f%% charged" % (vendor, t * 100))


def analyze_paper_vs_swipe(day_data):
    swipe_total = 0.0
    ebt_total = 0.0
    for day in day_data:
        ebt_total += _dollar_str_to_float(day[3])
        swipe_total += _dollar_str_to_float(day[7][1:])
    return swipe_total / ebt_total


def _dollar_str_to_float(dollar):
    return float(dollar.replace('$', '').replace(',', ''))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--filename', required=True, help='This is the CSV file to read in')
    main(ap.parse_args().filename)
