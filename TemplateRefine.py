import pandas as pd

def insertTemplate(tmp, tmplist):
    index = 0
    for t in tmplist:
        if(((t in tmp) == True) and ((tmp in t) == False)):
            return index
        else:
            index = index+1
    return -1

contentlist = pd.read_csv("Templates/Mac_templates.csv", usecols=['Templates'])
templates = contentlist['Templates']

templates_new = []
for index in range(0,len(templates)):
    if(templates[index] in templates_new):
        pass
    else:
        pos = insertTemplate(templates[index], templates_new)
        if(pos == -1):
            templates_new.append(templates[index])
        else:
            templates_new.insert(pos, templates[index])

print(len(templates))
print(len(templates_new))

refinedtmps = pd.DataFrame({'Templates' : templates_new})
refinedtmps.to_csv("Templates/Mac_refined.csv")
