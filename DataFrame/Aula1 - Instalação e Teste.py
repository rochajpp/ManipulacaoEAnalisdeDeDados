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

#-------------------------------

numerosAleatorios = pd.DataFrame(np.random.rand(15, 10) * 100)
print("\n------- DataFrame Números Aleatórios 15 linhas e 10 coluna -------\n")
print(numerosAleatorios)
print("\n")


#columns = Renomeamos os nomes das colunas
numerosAleatorios = pd.DataFrame(np.random.rand(15, 10) * 100, columns=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
print("--------- DataFrame Números Aleatórios 15 linhas e 10 colunas -------\n")
print(numerosAleatorios)
print("\n")

#Exibe o nome de todas as colunas
print(numerosAleatorios.columns)

#Criando um DataFrame a partir de um dicionário
notasAlunos_DataFrame = pd.DataFrame({
    "Nome": ["Ana", "Pedro", "João", "Marta", "Allan"],
    "Média": [9, 7, 10, 8, 9]
})
#\n = Quebra de linha (mesma qeu dar um enter para deixar um espaço)
print("\n-------- DataFrame Dicionário Notas Alunos\n")
print(notasAlunos_DataFrame)
