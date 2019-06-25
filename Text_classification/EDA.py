import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
# 그래프를 주피터 노트북에서 바로 그리도록 하려면 %matplotlib inline 사용

DATA_IN_PATH = './Text_classification/data/' #데이터가 저장된 경로
train_data = pd.read_csv(DATA_IN_PATH + 'labeledTrainData.tsv', header=0, delimiter='\t', quoting=3)
# delimiter = 사용할 데이터는 탭으로 구분되어 있기 때문
# header = 0 데이터에 각 항복명이 포함되어 있기 때문에
# quoting = 3 ""를 무시하기 위해

train_data.head()afd