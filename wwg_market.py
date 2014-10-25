import sys
import csv


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
    if len(sys.argv) < 2:
        print("A csv file is needed")
        sys.exit(-1)
    main(sys.argv[1])
