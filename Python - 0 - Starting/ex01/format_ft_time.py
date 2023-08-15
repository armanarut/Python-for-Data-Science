import time


date = "Seconds since January 1, 1970: " + str(format(time.time(), ",.4f")) + \
    " or " + str(format(time.time(), ".2e")) + " in scientific notation"
print(date)

date = time.strftime("%b %d %Y", time.localtime())
print(date)
