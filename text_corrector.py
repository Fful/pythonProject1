from datetime import datetime


def corrector(a):
    try:
        return [a[0], datetime.strptime(a[1], '%Y/%m/%d'), float(a[2]), int(a[3])]
    except ValueError:
        return a


data_sorted = []
with open('temp_data_pipes_00a.txt') as data:
    for line in data:
        line_sorted = corrector(line.strip().split('|'))
        print(line_sorted)
        data_sorted.append(line_sorted)
