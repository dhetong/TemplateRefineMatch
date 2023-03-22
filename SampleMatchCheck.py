import pandas as pd

from RegexTransformer import RegexMatch2File

contentlist = pd.read_csv("Templates/Mac_2k_0_refined_1.csv", usecols=['RefinedTemplate'])
templates = contentlist['RefinedTemplate']

RegexMatch2File(templates, "Datasets/Mac_2k_0.log")

# for tmp in templates:
#     regex = Templates2Regex(tmp)
#     print(regex)