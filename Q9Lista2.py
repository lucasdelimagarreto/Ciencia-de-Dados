import pandas as pd
import statistics as sts

# -------------------------------
# Carregar o arquivo CSV
# -------------------------------
loja = pd.read_csv("dados_loja.csv")

print("\n--- Pré-visualização dos dados ---")
print(loja.head())

# -------------------------------
# Selecionar apenas atributos quantitativos
# -------------------------------
loja_quant = loja[["Quantidade", "Preco (R$)"]]

print("\n--- Correlação entre atributos quantitativos ---")
print(loja_quant.corr(), "\n")

# -------------------------------
# Calcular moda dos atributos qualitativos
# -------------------------------
moda_produto = sts.mode(loja["Produto"])
moda_categoria = sts.mode(loja["Categoria"])

print("\n--- Moda dos atributos qualitativos ---")
print(f"Produto mais frequente: {moda_produto}")
print(f"Categoria mais frequente: {moda_categoria}")

# -------------------------------
# Interpretação básica
# -------------------------------
