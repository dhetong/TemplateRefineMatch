import re

regex = 'Progress of TaskAttempt .* is \: .*'

loglines = open('Datasets/unmatched.log')
for log in loglines:
    match = re.search(regex, log)
    if(match):
        pass
    else:
        print(log)