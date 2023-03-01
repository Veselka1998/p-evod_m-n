from bs4 import BeautifulSoup
import requests
from tkinter import *
import json


class Currency:
    def __init__(self, name, url_to_get_rate):
        self.name = name
        self.url_to_get_rate = url_to_get_rate
      
    def exchange(self, czk_amount):
        return czk_amount / self.getRate()
    
    def getResponseFromWeb(self):
        return requests.get(self.url_to_get_rate)
    
    def getRate(self):
        response = self.getResponseFromWeb()
        doc = BeautifulSoup(response.text, 'html.parser')
        
        p_elem = doc.find(name='p', class_='akt_kurz')
        rate = p_elem.find(name='span', class_='clrred').text
        return float(rate)
            
        
class EuroCurrency(Currency):
    def __init__(self):
        super().__init__('EUR', 'https://www.kurzy.cz/kurzy-men/nejlepsi-kurzy/EUR-euro/')

    
class DollarCurrency(Currency):    
    def __init__(self):
        super().__init__('USD', 'https://www.kurzy.cz/kurzy-men/nejlepsi-kurzy/USD-americky-dolar/')
    

class BitcoinCurrency(Currency):
    def __init__(self):
        super().__init__('BTC', 'https://streamer.kurzy.cz/crypto/json/btc.json')
    
    def getRate(self):
        response = self.getResponseFromWeb()
        values = json.loads(response.text.replace('jcb(','').replace(')', ''))
        return float(values[2])



currencies = [EuroCurrency(), DollarCurrency(), BitcoinCurrency()]
labelCurrencies = {}

def add_currency_to_gui(currency):
    global labelCurrencies
    countCurrenciesInGui = len(labelCurrencies.keys())
    
    result_label = Label(text="0", font=("Helvetica", 15), bg="#0b00a4", fg="white")
    result_label.grid(row=countCurrenciesInGui + 1, column=0)
    
    currency_caption_label = Label(text=currency.name, font=("Helvetica", 15), bg="#0b00a4", fg="white")
    currency_caption_label.grid(row=countCurrenciesInGui + 1, column=1)
    
    labelCurrencies[currency.name] = result_label



def exchange():  
    for c in currencies:
        amount = float(amount_input.get())
        labelCurrencies[c.name]['text'] = c.exchange(amount) 


window = Tk()
window.title("Kalkulačka VESELKA")
window.minsize(200, 300)
window.resizable(False, False)
window.config(bg="#0b00a4")
window.iconbitmap("BTC.ico")

# Input
amount_input = Entry(width=10, font=("Helvetica", 15))
amount_input.grid(row=0, column=0, padx=10, pady=10)

btc_label = Label(text="CZK", font=("Helvetica", 15), bg="#0b00a4", fg="white")
btc_label.grid(row=0, column=1)

#currencies to exchange
for c in currencies:
    add_currency_to_gui(c)


# Button
count_button = Button(text="Převést", font=("Helvetica", 15), bg="#242f7a", fg="white", command=(exchange))
count_button.grid(row=0, column=2, padx=10, pady=10)


window.mainloop()
        
    
    
    
    