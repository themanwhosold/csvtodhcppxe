import re, csv

def verifyMAC(mac):
    if re.match('^([0-9A-F]{2}[:-]){5}([0-9A-F]{2})$',mac) is not None:
        print(mac)
    else:
        print('Keine gültige MAC')

def convertMAC(number):
    if len(number)==12:
        print(number)
        mac = number[0:2] + ':' + number[2:4] + ':' + number[4:6] + ':' + number[6:8] + ':' + number[8:10] + ':' + number[10:12]
        print(mac)
        return(mac)
    else:
        print('Keine 12 Stellen, keine gültige MAC')

with open('/home/markus/skripting/test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
    #verifyMAC('00:50:56:55:55:55')
    #verifyMAC('00:50')
    convertMAC('005056555555')