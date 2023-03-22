import pandas as pd
import random

sample_num = 5000
unmatchedfile = pd.read_csv("Mac_unmatched.csv", usecols=['UnmathedLogs'])
loglist = unmatchedfile['UnmathedLogs']
# line_num = len(loglist)
#
# step = int(line_num/sample_num)
# start_point = 0
# select_point = random.randint(start_point, start_point+step)

logfile = open("Mac_unmatched.log", 'w')
for line in loglist:
    print(line)
    logfile.write(line)
logfile.close()

# HDFS_part_num = 56
#
# logfile = open('HDFS_unmatched.log', 'w')
#
# for i in range(HDFS_part_num):
#     file_name = 'Results/HDFS_unmatched.part'+ str(i) + '.csv'
#     print(file_name)
#     unmatchedfile = pd.read_csv(file_name, usecols=['Unmathed logs'])
#     loglist = unmatchedfile['Unmathed logs']
#     for line in loglist:
#         logfile.write(line)
# logfile.close()