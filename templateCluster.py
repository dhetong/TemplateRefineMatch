import pandas as pd

# def ClusterTemplate(filename):
#     contentlist = pd.read_csv(filename, usecols=['CorrectedTemplate', 'Occurrences'])
#     templates = contentlist['CorrectedTemplate']
#     appearance = contentlist['Occurrences']
#
#     templates_new = []
#     appearance_new = []
#     for index in range(0,len(templates)):
#         if(templates[index] in templates_new):
#             index_new = FindIndex(templates[index], templates_new)
#             appearance_new[index_new] = appearance_new[index_new] + appearance[index]
#         else:
#             templates_new.append(templates[index])
#             appearance_new.append(appearance[index])
#     data_new = {'Templates':templates_new, 'Appearance':appearance_new}
#     template_df = pd.DataFrame(data=data_new)
#     return template_df

def ClusterTemplate(filename):
    contentlist = pd.read_csv(filename, usecols=['CorrectTemplate'])
    templates = contentlist['CorrectTemplate']

    templates_new = []
    for index in range(0,len(templates)):
        if(templates[index] in templates_new):
            pass
        else:
            templates_new.append(templates[index])
    data_new = {'Templates':templates_new}
    template_df = pd.DataFrame(data=data_new)
    return template_df

def FindIndex(temp, templine):
    for index in range(0,len(templine)):
        if(temp == templine[index]):
            return index
    return -1

def RankCheck(tmpcheck, tmplist):
    index = -1
    for tmp in tmplist:
        index = index+1
        if tmpcheck in tmp:
            return index
    return -1

def AdjustTmpRank(tmplist):
    tmplist_new = []

    for tmp in tmplist:
        insertpos = RankCheck(tmp, tmplist_new)
        if(insertpos < 0):
            tmplist_new.append(tmp)
        else:
            tmplist_new.insert(insertpos+1,tmp)

    return tmplist_new