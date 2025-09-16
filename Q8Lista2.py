import pandas as pd
import matplotlib.pyplot as plt
import seaborn as srn

# -------------------------------
# Carregar o arquivo CSV
# -------------------------------
pacientes = pd.read_csv("dados_pacientes.csv")

# Mostrar primeiras linhas para conferência
print("\n--- Pré-visualização dos dados ---")
print(pacientes.head())

# -------------------------------
# Selecionar apenas variáveis quantitativas
# -------------------------------
pacientes_quant = pacientes[["Idade", "Peso", "Temperatura"]]

# -------------------------------
# Calcular covariância e correlação
# -------------------------------
print("\n--- Covariância ---")
print(pacientes_quant.cov(), "\n")

print("\n--- Correlação ---")
print(pacientes_quant.corr(), "\n")

# -------------------------------
# Plotar matriz de dispersão
# -------------------------------
srn.pairplot(pacientes_quant)
plt.suptitle("Matriz de Dispersão - Pacientes", y=1.02)
plt.show()

