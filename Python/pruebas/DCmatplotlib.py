import matplotlib.pyplot as plt
import seaborn as sns
import os

from tflearn.datasets import titanic

datasetName = 'titanic_dataset.csv'

if os.path.isfile('./' + datasetName):
    print("Titanic dataset... already exists")
else:
    titanic.download_dataset(datasetName)

import pandas as pd
df = pd.read_csv('titanic_dataset.csv', header='infer')

survivedSex = df[["survived", "sex"]]

sns.barplot('sex', 'survived', data=survivedSex, color="aquamarine")
plt.show()
