import pandas as pd
import statistics as sts
import matplotlib.pyplot as plt
import seaborn as srn

# -------------------------------
# DataFrame com os dados do Hospital
# -------------------------------
dados = {
    "Id": [4201, 3217, 4039, 1920, 4340, 2301, 1322, 3027],
    "Nome": ["João", "Maria", "Luiz", "José", "Cláudia", "Ana", "Marta", "Paulo"],
    "Idade": [28, 18, 49, 18, 21, 22, 19, 34],
    "Sexo": ["M", "F", "M", "M", "F", "F", "F", "M"],
    "Peso": [79, 67, 92, 43, 52, 72, 87, 67],
    "Manchas": ["Concentradas", "Inexistente", "Espalhadas", "Inexistente", "Uniformes", "Inexistentes", "Espalhadas", "Uniformes"],
    "Temperatura": [38.0, 39.5, 38.0, 38.5, 37.0, 38.0, 39.0, 38.4],
    "NumInternacoes": [2, 4, 2, 8, 1, 3, 6, 2],
    "Estado": ["SP", "MG", "RS", "MG", "PE", "RJ", "AM", "GO"],
    "Diagnóstico": ["Doente", "Doente", "Saudável", "Doente", "Saudável", "Doente", "Doente", "Saudável"]
}

hospital = pd.DataFrame(dados)

# -------------------------------
# Estatísticas Univariadas
# -------------------------------
print("\n--- Estatísticas Univariadas ---\n")

for coluna in ["Idade", "Peso", "Temperatura", "NumInternacoes"]:
    print(f"▶ {coluna}")
    print(f"Média: {hospital[coluna].mean():.2f}")
    print(f"Mediana: {hospital[coluna].median():.2f}")
    print(f"Moda: {sts.mode(hospital[coluna])}")
    print(f"Desvio Padrão: {hospital[coluna].std():.2f}")
    print(f"Q1: {hospital[coluna].quantile(0.25)}")
    print(f"Q3: {hospital[coluna].quantile(0.75)}\n")

# -------------------------------
# Frequências de dados qualitativos
# -------------------------------
print("\n--- Frequências de Variáveis Qualitativas ---\n")
print("Sexo:\n", hospital["Sexo"].value_counts(), "\n")
print("Manchas:\n", hospital["Manchas"].value_counts(), "\n")
print("Estado:\n", hospital["Estado"].value_counts(), "\n")
print("Diagnóstico:\n", hospital["Diagnóstico"].value_counts(), "\n")

# -------------------------------
# Estatísticas Multivariadas
# -------------------------------
print("\n--- Covariância ---\n")
print(hospital[["Idade", "Peso", "Temperatura", "NumInternacoes"]].cov(), "\n")

print("\n--- Correlação ---\n")
print(hospital[["Idade", "Peso", "Temperatura", "NumInternacoes"]].corr(), "\n")

# -------------------------------
# Visualizações
# -------------------------------

# -------------------------------
# Histograma
# -------------------------------
hospital[["Idade", "Peso", "Temperatura", "NumInternacoes"]].hist(figsize=(10, 8))
plt.suptitle("Histogramas das Variáveis Quantitativas")
plt.show()

# -------------------------------
# Boxplot
# -------------------------------
srn.boxplot(data=hospital[["Idade", "Peso", "Temperatura", "NumInternacoes"]])
plt.title("Boxplot das Variáveis Quantitativas")
plt.show()

# -------------------------------
# Diagrama de dispersão (scatterplot matrix)
# -------------------------------
srn.pairplot(hospital[["Idade", "Peso", "Temperatura", "NumInternacoes"]])
plt.suptitle("Matriz de Dispersão", y=1.02)
plt.show()