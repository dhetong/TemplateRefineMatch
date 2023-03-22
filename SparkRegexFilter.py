import re

def IsMatched(regexlist, logline):
    for regex in regexlist:
        match = re.search(regex, logline)
        if(match):
            return True
    return False