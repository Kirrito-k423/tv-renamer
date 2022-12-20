
import re
name = 'x2)'

matchObj = re.match('x2\)', name)
if matchObj:
    print("yes")