#!/usr/bin/env python3

import sys

try:
    x = int(sys.argv[1]) - 3500 - 0

    if x <= 1500 and x >0:
        tax = x * 0.03 - 0
        
    elif x <= 4500 and x > 1500:
        tax = x * 0.10 - 105

    elif x <= 9000 and x > 4500:
        tax = x * 0.20 - 555

    elif x <= 35000 and x > 9000:
        tax = x * 0.25 - 1005
 
    elif x <= 55000 and x > 35000:
        tax = x * 0.3 - 2755

    elif x <= 80000 and x > 55000:
        tax = x * 0.35 - 5505

    elif x > 80000:
        tax = x * 0.45 - 13505

    else:
        tax = 0

    print (format(tax, ".2f"))

except IndexError:
    print("Parameter Error")
except ValueError:
    print("Parameter Error")
