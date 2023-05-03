import pandas as pd

alunos = [
    {
        "Nome": "João",
        "Idade": 19,
        "Média": 10
    },

    {
        "Nome": "Lucas",
        "Idade": 20,
        "Média": 10
    },

    {
        "Nome": "Alan",
        "Idade": 22,
        "Média": 9
    },

    {
        "Nome": "André",
        "Idade": 20,
        "Média": 8
    },
]

DataFrame = pd.DataFrame(alunos).sort_values(by="Média", ascending=False)
print(DataFrame)
