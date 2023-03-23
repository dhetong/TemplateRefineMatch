import re
import pandas as pd

def Templates2Regex(template):
    regex = template
    regex = regex.replace("\\", "\\\\")
    regex = regex.replace(".", "\.")
    regex = regex.replace("*", "\*")

    regex = regex.replace("<\*>", ".*")

    regex = regex.replace("(", "\(")
    regex = regex.replace(")", "\)")

    regex = regex.replace("[","\[")
    regex = regex.replace("]","\]")

    regex = regex.replace("|","\|")

    regex = regex.replace("+", "\+")
    regex = regex.replace("?", "\?")
    regex = regex.replace("$", "\$")
    regex = regex.replace("@", "\@")
    regex = regex.replace("^", "\^")

    regex = regex.replace(":", "\:")

    return regex

def RegexMatch(tmp_list, file):
    num_match = 0

    logfile = open(file)
    loglines = logfile.readlines()

    matchlist = []
    index_regex = 0

    for tmp_ori in tmp_list:
        tmp = Templates2Regex(tmp_ori)
        index = 0

        print('Begin:' + str(tmp))

        for line in loglines:
            if (index in matchlist):
                pass
            else:
                match = re.search(tmp, line)
                if match:
                    num_match = num_match+1
                    matchlist.append(index)
                else:
                    pass
            index = index + 1
            if(index == 10000):
                print("Finished another 10000")

        print('Finish:' + str(index_regex))
        index_regex = index_regex + 1

    index = 0
    unmatchedlogs = []
    unmatchedindex = []
    for line in loglines:
        if(index in matchlist):
            pass
        else:
            unmatchedindex.append(index)
            unmatchedlogs.append(line)
        index = index + 1

    print(num_match)
    return unmatchedlogs

def RegexMatch2File(tmp_list, file):
    tmp_col = []
    log_col = []

    tmp_col_num = []
    num_col = []

    num_match = 0

    logfile = open(file)
    loglines = logfile.readlines()

    matchlist = []
    index_regex = 0

    for tmp_ori in tmp_list:
        tmp = Templates2Regex(tmp_ori)
        index = 0

        print('Begin:' + str(tmp))

        tmp_n = 0

        for line in loglines:
            if (index in matchlist):
                pass
            else:
                match = re.search(tmp, line)
                if match:
                    num_match = num_match+1
                    tmp_n = tmp_n + 1
                    matchlist.append(index)

                    tmp_col.append(tmp_ori)
                    log_col.append(line)
                else:
                    pass
            index = index + 1
            if(index == 10000):
                print("Finished another 10000")

        tmp_col_num.append(tmp_ori)
        num_col.append(tmp_n)

        print('Finish:' + str(index_regex))
        print(tmp_n)
        index_regex = index_regex + 1

    matchedata = pd.DataFrame({"Template": tmp_col, "Matchedlog": log_col})
    matchedata.to_csv("Mac_2k_matchresult.csv")

    matchedata_num = pd.DataFrame({"Template": tmp_col_num, "Matchednum": num_col})
    matchedata_num.to_csv("Mac_2k_matchednum.csv")

    print(num_match)

    index = 0
    unmatchedlogs = []
    for line in loglines:
        if (index in matchlist):
            pass
        else:
            unmatchedlogs.append(line)
            print(line)
        index = index + 1
