import sys
import re

#поиск двоичного числа кратного 3ем
for line in sys.stdin:
    line = line.rstrip()
    if re.findall(r'^(0|(1(01*0)*1))*$', line):
        print(line)
