import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import requests


def crypto_comparison(fsym, tsym):
    crypto_currencies = ['btc', 'eth', 'ltc', 'xrp']
    currencies = ['usd', 'eur', 'pkr', 'cad', 'aud', 'kwd']
    user_input = 0
    baseURL = ''

    if (fsym.lower() in crypto_currencies) and (tsym.lower() in currencies):

        while True:
            try:
                print('Kindly select one of the following:\n\n \
                                     Press 1 for Minute Price\n \
                                     Press 2 for Hour Price\n \
                                     Press 3 For Monthly Price\n')

                user_input = int(input("Kindly enter one of the above mentioned values: "))
                if user_input == 1:

                    baseURL = 'https://min-api.cryptocompare.com/data/{}?fsym={}&tsym={}&limit=59&aggregate=1&e=CCCAGG'.format(
                        'histominute', fsym.upper(), tsym.upper())
                    break
                elif user_input == 2:

                    baseURL = 'https://min-api.cryptocompare.com/data/{}?fsym={}&tsym={}&limit=59&aggregate=1&e=CCCAGG'.format(
                        'histohour', fsym.upper(), tsym.upper())
                    break
                elif user_input == 3:

                    baseURL = 'https://min-api.cryptocompare.com/data/{}?fsym={}&tsym={}&limit=59&aggregate=3&e=CCCAGG'.format(
                        'histoday', fsym.upper(), tsym.upper())
                    break
                else:
                    continue

            except:
                print("\n\nKindly enter valid value!\n\n")
                continue

        df = pd.DataFrame(requests.get(baseURL).json()['Data'])
        print('global', baseURL)
        df['timestamp'] = [dt.datetime.fromtimestamp(d) for d in df.time]
        plt.plot(df.timestamp, df.high, 'yo')
        if user_input == 1:
            print(baseURL)
            plt.xlabel('Time Iteration in Minutes | Total ' + str(len(df)) + " Entries")
            plt.ylabel('Value in ' + tsym.upper())
            plt.title(fsym.upper() + " vs " + tsym.upper() + " | Minute to Minute Chart")
            plt.show()

        if user_input == 2:
            print(baseURL)
            plt.xlabel('Time Iteration Days | Total ' + str(len(df)) + " Entries")
            plt.ylabel('Value in ' + tsym.upper())
            plt.title(fsym.upper() + " vs " + tsym.upper() + " | Day to Day Chart")
            plt.show()

        if user_input == 3:
            print(baseURL)
            plt.xlabel('Time Iteration in Months | Total ' + str(len(df)) + " Entries")
            plt.ylabel('Value in ' + tsym.upper())
            plt.title(fsym.upper() + " vs " + tsym.upper() + " | Month to Month Chart")
            plt.show()

    else:
        print("You can only enter the following currencies:\n")
        print('First Argugemnt Crypto Currencies: ')
        for cc in crypto_currencies:
            print("\t", cc.upper())
        print("\nSecond Argument Normal Currencies:")
        for cc in currencies:
            print("\t", cc.upper())


crypto_comparison('btc', 'usd')
