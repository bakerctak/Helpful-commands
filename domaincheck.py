# python3
# sudo pip3 install python-whois
# Requires a file in the same directory named domains.txt that contains one domain per line
# Note: whois doesn't play well with .XX domains where XX is the country code. It will say it's not registered. Just check them manually

import whois
import time

with open('domains.txt') as fp:
    line = fp.readline()
    while line:
        line = line.strip()
        w = whois.whois(line)
        if w:
            try:
                print(line + "," + w.registrar)
            except:
                print(line + " IS NOT REGISTERED")

        line = fp.readline()
        time.sleep(5)
