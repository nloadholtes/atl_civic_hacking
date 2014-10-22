import sys
import csv



def csv_to_dict(data, key_col):
    output = {}
    for row in data:
        key_data = output.get(row[key_col], [])
        key_data.append(row[key_col + 1:])
        output[row[key_col]] = key_data

    return output




def main(filename):
    print("opening: %s" % filename)
    cdata = csv.reader(open(filename, 'r'))
    data = []
    #toss headers
    headers = cdata.next()
    for row in cdata:
        data.append(row)
    print(data[0])
    print(csv_to_dict(data, 1))
    


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("A csv file is needed")
        sys.exit(-1)
    main(sys.argv[1])
