import re, csv

def verifyMAC(mac):
    if re.match('^([0-9A-F]{2}[:]){5}([0-9A-F]{2})$',mac) is not None:
        return(mac)
    if re.match('^([0-9A-F]{2}[-]){5}([0-9A-F]{2})$',mac) is not None:
        mac = mac.replace('-',':')
        return(mac)
    else:
        raise ValueError

def convertMAC(number):
    if len(number)==12:
        print(number)
        mac = number[0:2] + ':' + number[2:4] + ':' + number[4:6] + ':' + number[6:8] + ':' + number[8:10] + ':' + number[10:12]
        print(mac)
        return(mac)
    else:
        raise ValueError

def verifyIP(ip):
    if re.match('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}$',ip) is not None:
        return(ip)
    else:
        raise ValueError

def generateDHCPEntry(mac, name, ip):
    # Future: Parse from Config
    dhcpEntry = 'host ' + name + ' { hardware ethernet ' + mac + '; fixed-address ' + ip + '; }\n'
    return(dhcpEntry)

entry = ''

with open('/home/markus/skripting/csvtodhcppxe/test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            mac = verifyMAC(row[4])
            ip = verifyIP(row[1])
            name = row[0]
            entry += generateDHCPEntry(mac, name, ip)
            line_count += 1
    print(entry)
    print(f'Processed {line_count} lines.')