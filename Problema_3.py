import json
import os

arquivo = os.path.join('faturamento_102024.json') #os valores com 0 correspondem a finais de semana e/ou feriados

if os.path.exists(arquivo):
    with open(arquivo, 'r') as file:
        dados = json.load(file)
    
    print(dados)
else:
    print(f"Arquivo '{arquivo}' não encontrado.")

import json

with open('faturamento_102024.json', 'r') as file:
    dados = json.load(file)

faturamento_dias_uteis = [dia['valor'] for dia in dados if dia['valor'] > 0]

menor_faturamento_dia = min(faturamento_dias_uteis)
maior_faturamento_dia = max(faturamento_dias_uteis)

media_faturamento = sum(faturamento_dias_uteis) / len(faturamento_dias_uteis)

dias_acima_media = sum(1 for valor in faturamento_dias_uteis if valor > media_faturamento)

print(f"Menor valor de faturamento diario: {menor_faturamento_dia}")
print(f"Maior valor de faturamento diario: {maior_faturamento_dia}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
