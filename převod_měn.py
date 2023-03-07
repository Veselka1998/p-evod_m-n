from bs4 import BeautifulSoup
import requests
from tkinter import *

response = requests.get("https://www.aaavaluty.cz/smenarna-brno/?gclid=Cj0KCQiAutyfBhCMARIsAMgcRJSawWTf5NZpTHau9lQB1LPkmqpeUyRIsub0fQVuLwS0-XpMtrD5-uwaAtsCEALw_wcB")
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all(name="td", class_="cervena bold fs14")
euro = articles[0]
euro = list(euro)
usd = articles[2]
usd = list(usd)

def get_bitcoin_value_from_web_to_float():
    response2 = requests.get("https://streamer.kurzy.cz/crypto/json/btc.json?callback=jcb&_=1677594635006&fbclid=IwAR3pzslrTEaVNQGaF_zOlKa3hs6VqDZJkw0S0VxFojllBQ6x2oYU5DTuPkk")
    soup2 = BeautifulSoup(response2.text, "html.parser")

    soup2 = str(soup2)
    new_string = ""
    for i in soup2:
        if i == soup2[0] or i == soup2[1] or i == soup2[2] or i == soup2[3] or i == soup2[-1]:
            continue
        elif i == "[" or i == "]" or i == '"':
            continue
        else:
            new_string += i
    new_string = new_string.split(", ")
    return float(new_string[2])
                                     
def euro_str_to_float():
    new_string = ""
    for i in str(euro):
        if i == "[" or i == "]" or i == "'":
            continue
        elif i == ",":
            new_string += "."
        else:
            new_string += i
    return float(new_string)
    
def usd_str_to_float():
    new_string = ""
    for i in str(usd):
        if i == "[" or i == "]" or i == "'":
            continue
        elif i == ",":
            new_string += "."
        else:
            new_string += i
    return float(new_string)

# Screen
window = Tk()
window.title("Kalkulačka VESELKA")
window.minsize(200, 300)
window.resizable(False, False)
window.config(bg="#0b00a4")


# Convert for better read
bitcoin = get_bitcoin_value_from_web_to_float()
euro = euro_str_to_float()
usd = usd_str_to_float()

# Funkcion 
def convert_money_and_add_dot():
    bitcoin_new_string = ""
    amount_czk = float(amount_input.get()) * bitcoin
    amount_czk = round(amount_czk)
    for index, i in enumerate(reversed(str(amount_czk))):
        if index % 3 == 0 and index != 0:
            bitcoin_new_string += "."
            bitcoin_new_string += i
        else:
            bitcoin_new_string += i
    bitcoin_new_string = bitcoin_new_string[::-1]
    result_label_czk["text"] = bitcoin_new_string
    
    euro_new_string = ""
    amount_euro = float(amount_input.get()) * bitcoin / euro
    amount_euro = round(amount_euro)
    for index, i in enumerate(reversed(str(amount_euro))):
        if index % 3 == 0 and index != 0:
            euro_new_string += "."
            euro_new_string += i
        else:
            euro_new_string += i
    euro_new_string = euro_new_string[::-1]
    result_label_euro["text"] = euro_new_string

    usd_new_string = ""
    amount_usd = float(amount_input.get()) * bitcoin / usd
    amount_usd = round(amount_usd)
    for index, i in enumerate(reversed(str(amount_usd))):
        if index % 3 == 0 and index != 0:
            usd_new_string += "."
            usd_new_string += i
        else:
            usd_new_string += i
    usd_new_string = usd_new_string[::-1]
    result_label_usd["text"] = usd_new_string

    return result_label_czk["text"], result_label_euro["text"], result_label_usd["text"]

# Input
amount_input = Entry(width=10, font=("Helvetica", 15))
amount_input.grid(row=0, column=0, padx=10, pady=10)

# Label convert
result_label_czk = Label(text="0", font=("Helvetica", 15), bg="#0b00a4", fg="white")
result_label_czk.grid(row=1, column=0)

result_label_euro = Label(text="0", font=("Helvetica", 15), bg="#0b00a4", fg="white")
result_label_euro.grid(row=2, column=0)

result_label_usd = Label(text="0", font=("Helvetica", 15), bg="#0b00a4", fg="white")
result_label_usd.grid(row=3, column=0)

# Label currency
btc_label = Label(text="BTC", font=("Helvetica", 15), bg="#0b00a4", fg="white")
btc_label.grid(row=0, column=1)

czk_label = Label(text="CZK", font=("Helvetica", 15), bg="#0b00a4", fg="white")
czk_label.grid(row=1, column=1)

eur_label = Label(text="EUR", font=("Helvetica", 15), bg="#0b00a4", fg="white")
eur_label.grid(row=2, column=1)

usd_label = Label(text="USD", font=("Helvetica", 15), bg="#0b00a4", fg="white")
usd_label.grid(row=3, column=1)

# Butten
count_button = Button(text="Převést", font=("Helvetica", 15), bg="#242f7a", fg="white", command=(convert_money_and_add_dot))
count_button.grid(row=0, column=2, padx=10, pady=10)

# Main loop
window.mainloop()
