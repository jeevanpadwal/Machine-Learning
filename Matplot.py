import pandas as pd
import matplotlib.pyplot as plt

excel_file = 'WinePredictor.xlsx'

data = pd.read_excel(excel_file)

data[['Ash','Alcohol']].plot(kind="hist")
plt.show()