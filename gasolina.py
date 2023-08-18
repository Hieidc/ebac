# código de geração do gráfico

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Vizualização csv no pandas
gasolina_df = pd.read_csv('gasolina.csv', sep=',')
gasolina_df

# Defina o estilo do Seaborn (opcional, apenas para melhorar a aparência do gráfico)
sns.set(style="whitegrid")

# Crie o gráfico de linhas
plt.figure(figsize=(12, 8))  # Define o tamanho da figura (opcional)
sns.lineplot(data = gasolina_df, x="dia", y="venda")

# Adicione rótulos e título
plt.xlabel("Dia")
plt.ylabel("Preço")
plt.title("Preço ao longo dos dias")

# Salva o arquivo em png
plt.savefig('gasolina.png')

# Exiba o gráfico
plt.show()