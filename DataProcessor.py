import csv


def read_csv_50(file_path):
    with open(file_path, 'rb') as inp, open('expedia_50_1.csv', 'wb') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[21] == "50" and row[18] == "1":
                writer.writerow(row)


def read_csv_header(file_path):
    with open(file_path, 'rb') as inp:
        t = False
        for row in csv.reader(inp):
            print row
            if t:
                break
            t = True

def transform_data(file_path):
    with open(file_path, 'rb') as inp, open('TExpedia_50_1.csv', 'wb') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[21] == "50":  # and row[18] == "1"
                new_row = row
                new_row[11] = date_to_int(new_row[11])
                new_row[12] = date_to_int(new_row[12])
                del new_row[21]
                del new_row[20]
                del new_row[19]
                del new_row[17]
                del new_row[9]
                del new_row[8]
                del new_row[6]
                del new_row[2]
                del new_row[1]
                del new_row[0]
                writer.writerow(new_row)


def date_to_int(dt_str):
    try:
        dts = dt_str.split("-")
        dts = map(int, dts)
        return 10000*dts[0] + 100*dts[1] + dts[2]
    except:
        return '00000000'


if __name__ == "__main__":
    # read_csv_50("../Datasets/train.csv")
    # read_csv_header('../Datasets/test.csv')
    transform_data("expedia_50_1.csv")
    pass
