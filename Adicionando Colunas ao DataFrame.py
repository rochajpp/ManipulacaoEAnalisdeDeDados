import pandas as pd

notasAlunos_DF = pd.DataFrame({
    "Nome": ["Ana", "Pedro", "João"],
    "Nota 1": [9, 7, 10],
    "Nota 2": [6, 9, 8],
    "Nota 3": [7, 5, 10],
    "Nota 4": [10, 10, 6]
})

print("\n--------- DataFrame Dicionário Notas Alunos ------- \n")
print(notasAlunos_DF)
print("\n")

quantNotas = len(notasAlunos_DF.columns) - 1

notasAlunos_DF["Média"] = (notasAlunos_DF["Nota 1"] + notasAlunos_DF["Nota 2"] + notasAlunos_DF["Nota 3"] +
                           notasAlunos_DF["Nota 4"]) / quantNotas
print(notasAlunos_DF)

