from clientpy3 import *

try:
    
    usr = 'LimitlessDrive'
    pw = 'stopeatinginvisiblecows123'

    stockDict = getSecurities()
    mySec = getMySecurities()

    print("All the stocks available: ")
    print(stockDict)
    print()

    print("Stocks currently owned: ")
    print(mySec)
    print()

    tickers = sorted(stockDict)
    divs = ""
    for i in tickers:
        divs = divs + stockDict[i][1] + " "

    divs = divs.split()
    for i in range(0, len(divs)):
        divs[i] = float(divs[i])

    
    print(tickers)
    print(divs)

    top3 = getTop3(tickers, divs)
    print(top3)
    
except:
    print("unexpected error, logging out")

finally:
    run(usr, pw, 'CLOSE_CONNECTION')
