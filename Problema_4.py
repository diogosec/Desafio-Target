#é necessário instalar as bibliotecas openpyxl (leitura de xlsx) e matplotlib (elementos gráficos) no terminal
#utilize 
#pip install openpyxl 
#e depois 
#pip install matplotlib

import openpyxl
import matplotlib.pyplot as plt

workbook = openpyxl.load_workbook("Faturamento_estadual.xlsx")
sheet = workbook.active

estados = []
faturamentos = []

for row in sheet.iter_rows(min_row=2, values_only=True):
    estado, faturamento = row
    estados.append(estado)
    faturamentos.append(faturamento)

faturamento_total = sum(faturamentos)

plt.figure(figsize=(10, 7))
plt.pie(faturamentos, labels=estados, autopct='%1.1f%%', startangle=140)
plt.title("Representação do Faturamento por Estado")
plt.axis('equal')
plt.show()
