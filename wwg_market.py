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
    headers = cdata.next()
    print(headers)
    for row in cdata:
        data.append(row)
    print(data[0])
    vendors = csv_to_dict(data, 1)
    # import ipdb; ipdb.set_trace()
    
    for vendor, day_data in vendors.items():
        t = analyze_paper_vs_swipe(day_data)
        print("%s saw %s  charged" % (vendor, t))


def analyze_paper_vs_swipe(day_data):
    swipe_total = 0.0
    ebt_total = 0.0
    for day in day_data:
        ebt_total += float(day[3][1:])
        swipe_total += float(day[7][1:])
    return float(swipe_total) / ebt_total



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("A csv file is needed")
        sys.exit(-1)
    main(sys.argv[1])
