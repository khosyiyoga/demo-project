import re
import csv
from collections import Counter


def log_read(logfile):
    with open(logfile) as f:

        myregex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

        log = f.read()

        my_iplist = re.findall(myregex, log)

        return my_iplist


def log_read_sqli(logfile):
    with open(logfile) as f:
        reader = csv.reader(x.replace('\0', '') for x in f)
        loglist = list(reader)

    newlist = []

    r = re.compile(".*select.*", re.IGNORECASE)
    for x in loglist:

        filteredlist = list(filter(r.match, x))

        for y in filteredlist:
            newlist.append(x)

    write_csv_sqli(newlist)


def log_read_rfi(logfile):
    with open(logfile) as f:
        reader = csv.reader(x.replace('\0', '') for x in f)
        loglist = list(reader)

    newlist = []

    r = re.compile(".*file=.*", re.IGNORECASE)
    for x in loglist:

        filteredlist = list(filter(r.match, x))

        for y in filteredlist:
            newlist.append(x)

    write_csv_rfi(newlist)


def log_read_webshell(logfile):
    with open(logfile) as f:
        reader = csv.reader(x.replace('\0', '') for x in f)
        loglist = list(reader)

    newlist = []

    r = re.compile(".*passwd.*", re.IGNORECASE)
    for x in loglist:

        filteredlist = list(filter(r.match, x))

        for y in filteredlist:
            newlist.append(x)

    write_csv_webshell(newlist)


def log_read_ip(logfile):
    with open(logfile) as f:
        reader = csv.reader(x.replace('\0', '') for x in f)
        loglist = list(reader)

    iplist = ip_count(log_read(logfile))

    for item in iplist:

        newlist = []
        if item[0:3] == '172':
            continue
        else:
            r = re.compile(".*"+item+".*")
            for x in loglist:
                filteredlist = list(filter(r.match, x))
                for y in filteredlist:
                    newlist.append(x)

        write_csv_ipactivity(newlist, item)


def ip_count(my_iplist):
    return Counter(my_iplist)


def write_csv_ipactivity(ipactivitylist, ipaddress):

    with open('D:\\Documents\\Python Exercise\\pythonProject1\\IPActivity\\' + ipaddress+'.csv', 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        writer.writerows(ipactivitylist)


def write_csv_sqli(ipactivitylist):

    with open('D:\\Documents\\Python Exercise\\pythonProject1\\IPActivitySQLi\\sqli.csv', 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)
        writer.writerows(ipactivitylist)


def write_csv_rfi(ipactivitylist):

    with open('D:\\Documents\\Python Exercise\\pythonProject1\\IPActivityRFI\\rfi.csv', 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)
        writer.writerows(ipactivitylist)


def write_csv_webshell(ipactivitylist):

    with open('D:\\Documents\\Python Exercise\\pythonProject1\\IPActivityWebShell\\webshell.csv', 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)
        writer.writerows(ipactivitylist)


def write_csv_ipfrequency(ip_count):
    with open('IP-Frequency.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        header = ['IP Address', 'Frequency']

        writer.writerow(header)

        for item in ip_count:
            if item[0:3] == '172':
                continue
            else:
                writer.writerow((ip_count, ip_count[item]))


def write_csv_ipunique(ip_count):
    with open('IP-Unique.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        header = ['IP Address']

        writer.writerow(header)

        for item in ip_count:
            if item[0:3] == '172':
                continue
            else:
                writer.writerow([item])


# Create entry point of our code
if __name__ == '__main__':
    log_read_ip("CTF1.log")
    log_read_sqli("CTF1.log")
    log_read_rfi("CTF1.log")
    log_read_webshell("CTF1.log")
    write_csv_ipfrequency(ip_count(log_read("CTF1.log")))
    write_csv_ipunique(ip_count(log_read("CTF1.log")))
