import pandas as pd

critical_points = pd.read_csv("dados_criticos.csv") 

critical_only = critical_points[critical_points["is_critical"] == True]

critical_only.to_csv("regioes_criticas.csv", index=False)
critical_only.to_json("regioes_criticas.json", orient="records")

print("Exportações concluídas com sucesso!")