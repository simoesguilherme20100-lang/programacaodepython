import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

# Abrir janela para escolher o arquivo Excel
Tk().withdraw()

arquivo = filedialog.askopenfilename(
    title="Selecione o arquivo Excel",
    filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
)

# Verificar se foi selecionado um arquivo
if arquivo == "":
    print("Nenhum arquivo foi selecionado.")
    exit()

# Ler o Excel
df = pd.read_excel(arquivo)

# Mostrar os dados
print("\nDADOS:")
print(df)

# Média
media = df["Vendas"].mean()

print("\nMÉDIA DAS VENDAS:")
print(f"{media:.2f}")

# Variação percentual
df["Variacao_Percentual"] = df["Vendas"].pct_change() * 100

print("\nVARIAÇÃO PERCENTUAL:")
print(df[["Meses", "Vendas", "Variacao_Percentual"]])

# Maior venda
maior = df["Vendas"].max()
mes_maior = df.loc[df["Vendas"].idxmax(), "Meses"]

print("\nMAIOR VENDA:")
print(f"{mes_maior}: {maior}")

# Menor venda
menor = df["Vendas"].min()
mes_menor = df.loc[df["Vendas"].idxmin(), "Meses"]

print("\nMENOR VENDA:")
print(f"{mes_menor}: {menor}")

# Gráfico
sns.set_theme(style="whitegrid")

plt.figure(figsize=(15, 7))

sns.lineplot(
    data=df,
    x="Meses",
    y="Vendas",
    marker="o",
    color="blue",
    linewidth=2
)

plt.title("Vendas Mensais - 2023 e 2024")
plt.xlabel("Meses")
plt.ylabel("Vendas")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()