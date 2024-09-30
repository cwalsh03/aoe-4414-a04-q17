# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second

# Output:
#  Time in fractional julian date
#
# Written by Connor Walsh
# Other contributors: None
#

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# initialize script arguments
year = float('nan') # time in years
month = float('nan') # time in months
day = float('nan') # time in days
hour = float('nan') # time in hours
minute = float('nan') # time in minutes
second = float('nan') # time in seconds

# parse script arguments
if len(sys.argv)==7:
    year = int(sys.argv[1]) # time in years
    month = int(sys.argv[2]) # time in months
    day = int(sys.argv[3]) # time in days
    hour = int(sys.argv[4]) # time in hours
    minute = int(sys.argv[5]) # time in minutes
    second = float(sys.argv[6]) # time in seconds
else:
    print(\
   'Usage: '\
   'python3 ymdhms_to_jd.py year month day hour minute second'\
    )
    exit()

# write script below this line

JD = (day - 32075) \
    + 1461 * (year + 4800 + (month - 14)/12)/4 \
    +367*(month-2-(month-14)/12 * 12)/12 \
    -3*((year+4900+(month-14)/12)/100)/4

JD_mnight = JD - 0.5
D_frac = (second + 60 * (minute + 60 * hour)) / 86400.0
jd_frac = JD_mnight + D_frac

print(jd_frac)