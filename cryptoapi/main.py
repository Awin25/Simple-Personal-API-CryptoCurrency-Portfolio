import matplotlib.pyplot as plt
from tkinter import *
import requests
import json
import os
os.system('clear')

root = Tk() ## tk function


def font_change(amt):
    if amt >=0:
        return "green"
    else:
        return "red"


##create header
name_title = Label(root,text="Name",bg ="white",font = "Arial 10 bold ")
name_title.grid(row=0,column=0,sticky=N+S+E+W)

rank_title = Label(root,text="Rank",bg ="grey",font = "Arial 10 bold")
rank_title.grid(row=0,column=1,sticky=N+S+E+W)

current_price_title = Label(root,text="Current Price",bg ="white",font = "Arial 10 bold")
current_price_title.grid(row=0,column=2,sticky=N+S+E+W)

price_paid_title = Label(root,text="Price Paid",bg ="grey",font = "Arial 10 bold")
price_paid_title.grid(row=0,column=3,sticky=N+S+E+W)

profit_loss_per_title = Label(root,text="P\L Per",bg ="white",font = "Arial 10 bold")
profit_loss_per_title.grid(row=0,column=4,sticky=N+S+E+W)

hr_1_change_title = Label(root,text="1 HR Change",bg ="grey",font = "Arial 10 bold")
hr_1_change_title.grid(row=0,column=5,sticky=N+S+E+W)

hr_24_change_title = Label(root,text="24 HR Change",bg ="white",font = "Arial 10 bold")
hr_24_change_title.grid(row=0,column=6,sticky=N+S+E+W)

day_7_change_title = Label(root,text="7 Day Change",bg ="grey",font = "Arial 10 bold")
day_7_change_title.grid(row=0,column=7,sticky=N+S+E+W)

current_value_title = Label(root,text="Current Value",bg ="white",font = "Arial 10 bold")
current_value_title.grid(row=0,column=8,sticky=N+S+E+W)

profitloss_total_title = Label(root,text="Profit Loss Total",bg ="grey",font = "Arial 10 bold")
profitloss_total_title.grid(row=0,column=9,sticky=N+S+E+W)











def info():
## dictionary containing portfolio
    my_portfolio = [
            {
                "sym": "VET",
                "amount_owned": 1200,
                "price_paid_for": 0.09
            },
            {
                "sym": "XRP",
                "amount_owned": 600,
                "price_paid_for": 1.69
            },
            {
                "sym": "ADA",
                "amount_owned": 750,
                "price_paid_for": 2.10
            },

            { 
                "sym": "DOGE",
                "amount_owned": 1250,
                "price_paid_for": 0.10
            },
        ]
    headers = {  ### api key that acesses from coinmarketcap
        'X-CMC_PRO_API_KEY': "611ed76a-95f3-4069-ada4-33df73d00ba7",
        'Accepts': 'application/kson'
    }

    params = {     ## parameters that accesses the top coins of api using this.
        'start': '1',
        'limit': '25',
        'convert': 'USD'
    }
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    json = requests.get(url, params=params, headers=headers).json(); ## using json request able to access api
    coins = json['data']  ##data on coins

    portfolio_profitloss = 0
    total_currentvalue = 0
    row_count = 1
    pie = []
    pie_size = []

##calculations
    for x in coins:
        for coin in my_portfolio:
            if coin["sym"] == x['symbol']:    ##(coin[]) access dictionary of portfolio
                totalpaid = float(coin["amount_owned"]) * float(coin["price_paid_for"])
                currentvalue = float(coin["amount_owned"] * (float(x['quote']["USD"]['price'])))
                profit_loss = currentvalue - totalpaid
                portfolio_profitloss += profit_loss
                profit_loss_per_coin = (float(x['quote']["USD"]['price'])) -  float(coin["price_paid_for"])
                total_currentvalue += currentvalue
                pie.append(x["name"])
                pie.append(coin["amount_owned"])

        ## (x[]) access the actual api dictionary
                print("----------------------------------------------")
                print(" Rank: {0:.0f}".format(float(x['cmc_rank'])))
                print((x['name']))
                print(" Current Price: ${0:.2f}".format(float(x['quote']["USD"]['price'])))
                print(" Profit/Loss per coin : ${0:.2f}".format(float(profit_loss_per_coin)))
                print(" Total paid: ${0:.2f}".format(float(totalpaid)))
                print(" Current Value : ${0:.2f}".format(float( currentvalue)))
                print(" Total Profit/Loss: ${0:.2f}".format(float(profit_loss)))
                name = Label(root, text=(x['name']), bg="white")
                name.grid(row=row_count, column=0, sticky=N + S + E + W)

                rank = Label(root, text=(x['cmc_rank']), bg="grey")
                rank.grid(row=row_count, column=1, sticky=N + S + E + W)

                current_price = Label(root, text=("${0:.2f}".format(float(x['quote']["USD"]['price']))), bg="white")
                current_price.grid(row=row_count, column=2, sticky=N + S + E + W)

                price_paid = Label(root, text=("${0:.2f}".format(coin["price_paid_for"])), bg="grey")
                price_paid.grid(row=row_count, column=3, sticky=N + S + E + W)

                profit_loss_per = Label(root, text="${0:.2f}".format(float(profit_loss_per_coin)), bg="white",fg = font_change(float(profit_loss_per_coin)))
                profit_loss_per.grid(row=row_count, column=4, sticky=N + S + E + W)

                one_hr_change = Label(root, text=("${0:.2f}%".format(float(x['quote']["USD"]['percent_change_1h']))), bg="grey",fg = font_change(float(x['quote']["USD"]['percent_change_1h'])))
                one_hr_change.grid(row=row_count, column=5, sticky=N + S + E + W)

                twentyfour_hr_change_name = Label(root, text=("{0:.2f}%".format(float(x['quote']["USD"]['percent_change_24h']))), bg="white",fg = font_change(float(x['quote']["USD"]['percent_change_24h'])))
                twentyfour_hr_change_name.grid(row=row_count, column=6, sticky=N + S + E + W)

                seven_day_change_name = Label(root, text=("{0:.2f}%".format(float(x['quote']["USD"]['percent_change_7d']))), bg="grey",fg = font_change(float(x['quote']["USD"]['percent_change_7d'])))
                seven_day_change_name.grid(row=row_count, column=7, sticky=N + S + E + W)

                currentvalue = Label(root, text="${0:.2f}".format(float( currentvalue)), bg="white")
                currentvalue.grid(row=row_count, column=8, sticky=N + S + E + W)

                profit_loss_total = Label(root, text="${0:.2f}".format(float(profit_loss)), bg="grey",fg = font_change(float(profit_loss)))
                profit_loss_total.grid(row=row_count, column=9, sticky=N + S + E + W)

                row_count += 1;
        print("----------------------------------------------")
        print("Portfolio's Total Profit: ${0:.2f}".format(float(portfolio_profitloss)))

    portfolioprofit = Label(root,text ="P/L ${0:.2f}".format(float(portfolio_profitloss)),  font = "Arial 10 bold",fg = font_change(float(portfolio_profitloss)))
    portfolioprofit.grid(row = row_count, column = 0,sticky = W,padx = 10,pady= 10)

    total_current_value_output =  Label(root,text ="Current Value ${0:.2f}".format(float(total_currentvalue)),  font = "Arial 10 bold",fg = font_change(float(portfolio_profitloss)))
    total_current_value_output.grid(row=row_count, column=1, sticky=W, padx=10, pady=10)
    root.title("Cryptocurrency Portfolio - Portfolio Value: ${0:.2f}".format(float(total_currentvalue)))
    coins = "" ## refresh api each time
    update_button = Button(root,text = "Update Prices",command = info)
    update_button.grid(row = row_count,column = 9,sticky = E+S,padx=10,pady =10)

 ##   def graph(pie,pie_size):
      ##  labels = pie
       ## sizes = pie_size
       ## colors = ['red', 'yellow', 'gold', 'green']
      ##  patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90,normalize = False)
      ##  plt.legend(patches, labels, loc="best")
      ##  plt.axis('equal')
       ## plt.tight_layout()
      ##  plt.show()

   ## graph_button = Button(root,text = "Pie Chart",command = lambda: graph(pie,pie_size))
    ## use lambda in order to pass in the paramters for function
   ## graph_button.grid(row = row_count,column = 8,sticky = E+S,padx = 10,pady = 10)



info()
root.mainloop() ## instanties function that keeps the window loop working
