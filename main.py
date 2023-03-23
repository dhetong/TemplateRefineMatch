import pandas as pd

from RegexTransformer import Templates2Regex, RegexMatch
from SparkRegexFilter import IsMatched

template_df = pd.read_csv("Templates/Mac_refined.csv", usecols=['Templates'])
templates = template_df['Templates']

regex_list = []
for tmp in templates:
    regex = Templates2Regex(tmp)
    regex_list.append(regex)

unmatchedlog = []

loglines = open('Datasets/Mac.log')
for log in loglines:
    if(IsMatched(regex_list, log) == True):
        pass
    else:
        unmatchedlog.append(log)

for log in unmatchedlog:
    print(log)
print(unmatchedlog.__len__())
# contentlist = pd.read_csv("Templates/Mac_2k_0_refined.csv", usecols=['RefinedTemplate'])
# templates = contentlist['RefinedTemplate']
#
# unmatchedlogs = RegexMatch(templates, "Datasets/Mac.log")
#
# print(len(unmatchedlogs))
#
# unmatchedata = pd.DataFrame({"UnmathedLogs" : unmatchedlogs})
# unmatchedata.to_csv("Mac_unmatched.csv")