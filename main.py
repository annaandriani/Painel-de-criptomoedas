import time
import requests
import schedule

def Cotacoes():
  headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'e67833b8-9e5c-41c3-9614-fb44f610795f'
   }
  parametros = {
  'symbol': 'BTC,ETH,LTC'
    }

  r = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest", headers=headers, params=parametros).json()
  Bit = r["data"]["BTC"]["quote"]["USD"]
  Eth = r["data"]["ETH"]["quote"]["USD"]
  Ltc = r["data"]["LTC"]["quote"]["USD"]

  print("O valor BTCUSD (Bitcoin convertido em dólar), é: $",round(Bit["price"],3))
  print("O valor do ETHUSD (Ethereum convertido em dólar), é: $",round(Eth["price"],3))
  print("O valor do LTCUSD (Litecoin convertido em dólar), é: $",round(Ltc["price"],3))

def inicio():
  print("Olá, seja bem vindo ao painel de preços da MRBIT!")
  print("Escolha o número 1 para ter acesso aos valores das criptomoedas ou qualquer outro caractere para encerrar a execução!")
  valor = input("Adicione aqui o número desejado")
  if valor == "1":
    Cotacoes()
    schedule.every(10).seconds.do(Cotacoes)
    while True:
      schedule.run_pending()
      time.sleep(1)
  else:
    print("Você encerrou o painel de preços")

inicio()

