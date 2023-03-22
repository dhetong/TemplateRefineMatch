import pandas as pd

from pyspark import SparkContext, SparkConf

from RegexTransformer import Templates2Regex
from SparkRegexFilter import IsMatched
from templateCluster import ClusterTemplate, AdjustTmpRank

template_df = pd.read_csv("Templates/Hadoop_refined.csv", usecols=['Templates'])
templates = template_df['Templates']

regex_list = []
for tmp in templates:
    regex = Templates2Regex(tmp)
    regex_list.append(regex)

# for r in regex_list:
#     print(r)

sc = SparkContext.getOrCreate(SparkConf())
rddlog = sc.textFile('Datasets/unmatched.log')
warn_lines = rddlog.filter(lambda line: (IsMatched(regex_list, line) == True))

for line in warn_lines.collect():
    print(line)

# temple_df = ClusterTemplate('Templates/Hadoop_refined.csv')
# template_list = temple_df["Templates"]

# template_list_rank = AdjustTmpRank(template_list)
#
# print(len(template_list_rank))
#
# regex_list = []
#
# for tmp in template_list_rank:
#     regex = Templates2Regex(tmp)
#     regex_list.append(regex)
#
# sc = SparkContext.getOrCreate(SparkConf())
# rddlog = sc.textFile('HDFS_unmatched.log')
# warn_lines = rddlog.filter(lambda line: IsMatched(regex_list, line))
# print(warn_lines.count())