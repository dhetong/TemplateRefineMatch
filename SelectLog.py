import pandas as pd
import random

sample_num = 10000

unmatchedfile = open('Datasets/HealthApp.log').readlines()

line_num = len(unmatchedfile)
step = int(line_num/sample_num)
start_pos = 0
select_pos = random.randint(start_pos, start_pos+step)

select_lines = []
count = 0
while(count < sample_num):
    select_log = unmatchedfile[select_pos]
    select_lines.append(select_log)
    count = count+1

    start_pos = start_pos+step
    select_pos = random.randint(start_pos, start_pos+step)

select_file = open('Datasets/HealthApp.sample0.log', 'w')
for line in select_lines:
    select_file.write(line)

# unmatchedfile = pd.read_csv("Mac_unmatched.csv", usecols=['UnmathedLogs'])
# loglist = unmatchedfile['UnmathedLogs']

# line_num = len(loglist)
#
# step = int(line_num/sample_num)
# start_point = 0
# select_point = random.randint(start_point, start_point+step)

# logfile = open("Mac_unmatched.log", 'w')
# for line in loglist:
#     print(line)
#     logfile.write(line)
# logfile.close()

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