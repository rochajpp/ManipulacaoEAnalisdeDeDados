import pandas as pd
import numpy as np


#date_range = criamos uma lista
#periods = quantos dias
#20221201 = Ano/Mes/Dia
dataFrames_Data = pd.date_range('20221201', periods=31)
print(dataFrames_Data)

print("\n---------- DataFrame 12 meses com a freq M ----------\n")
dataFrames_Meses = pd.date_range('20221201', periods=12, freq="M")
print(dataFrames_Meses)
print("\n")

