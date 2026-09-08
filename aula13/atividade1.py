from bs4 import BeautifulSoup
import requests
import tkinter as tk

url = 'https://gratuitos.netlify.app/'

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar todas as linhas da tabela
linhas = soup.find_all('tr')

idades = []

for linha in linhas:
    colunas = linha.find_all('td')

    if colunas:
        # Ajuste o índice conforme a posição da coluna "Idade"
        idade = colunas[1].get_text(strip=True)
        idades.append(idade)

print("Idades encontradas:")
print(idades)

# Tkinter
janela = tk.Tk()
janela.title("Idades extraídas")
janela.geometry("300x300")

label = tk.Label(
    janela,
    text="Idades encontradas:\n\n" + "\n".join(idades),
    font=("Arial", 14)
)
label.pack(pady=30)

janela.mainloop()
