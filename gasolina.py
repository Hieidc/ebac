# #Criação do csv
# %%writefile gasolina.csv
# 
# dia,venda
# 
# 1,5.11
# 
# 2,4.99
# 
# 3,5.02
# 
# 4,5.21
# 
# 5,5.07
# 
# 6,5.09
# 
# 7,5.13
# 
# 8,5.12
# 
# 9,4.94
# 
# 10,5.03

# Bibliotecas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Vizualização csv no pandas
gasolina_df = pd.read_csv('gasolina.csv', sep=',')
gasolina_df

# Defina o estilo do Seaborn (opcional, apenas para melhorar a aparência do gráfico)
sns.set(style="darkgrid")

# Crie o gráfico de linhas
plt.figure(figsize=(10, 6))  # Define o tamanho da figura (opcional)
sns.lineplot(data = gasolina_df, x="dia", y="venda")

# Adicione rótulos e título
plt.xlabel("Dia")
plt.ylabel("Preço")
plt.title("Gráfico de Linhas: Preço ao longo dos dias")

# Salva o arquivo em png
plt.savefig('gasolina.png')

# Exiba o gráfico
plt.show()