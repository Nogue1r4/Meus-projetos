import json, requests

moedas_disponiveis= {'USD', 'EUR', 'BRL', 'JPY'}

for moeda in moedas_disponiveis:
    print(f"-{moeda}")

origem = input("Dinheiro de Origem: ")
dest= input("Dinheiro de Destino: ")
qnt_de_moeda= float(input("Quanto Dinheiro Deseja Converter? "))

if origem in moedas_disponiveis and dest in moedas_disponiveis:
    requisicao=requests.get(f"https://economia.awesomeapi.com.br/{origem}-{dest}")
    cotacao= requisicao.json()

    print(f"{qnt_de_moeda} {origem} equivale a {float(cotacao[0]['bid']) * qnt_de_moeda:.2f} {dest}")
else:
    print('Moedas Inválidas')