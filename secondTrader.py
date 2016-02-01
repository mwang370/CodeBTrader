from clientpy3 import *

try:
    
    usr = 'LimitlessDrive'
    pw = 'stopeatinginvisiblecows123'

    while True:

        while getCash() > 100:

            stockDict = getSecurities()
            mySec = getMySecurities()

            tickers = sorted(stockDict)
            divs = ""
    
            for i in tickers:
                divs = divs + stockDict[i][1] + " "
            divs = divs.split()
            for i in range(0, len(divs)):
                divs[i] = float(divs[i])
            
            top3 = getTop3(tickers, divs)


            for i in top3:
                price = str(minAsk(i))
                run(usr, pw, 'BID ' + i.strip() + ' ' + price.strip() + ' 5')
                
        stockDict = getSecurities()
        mySec = getMySecurities()

        tickers = sorted(stockDict)

        divs = ""
    
        for i in tickers:
            divs = divs + stockDict[i][1] + " "
        divs = divs.split()
        for i in range(0, len(divs)):
            divs[i] = float(divs[i])

        print('hi')
        if len(list(mySec.keys())) > 0:
            for i in list(mySec.keys()):
                if(divs[tickers.index(i)] < 0.001):
                    price = str(1.01*maxBid(i))
                    quantity = mySec[i]
                    print('hi')
                    print('ASK ' + i.strip() + ' ' + price.strip() + quantity)
                    run(usr, pw, 'ASK ' + i.strip() + ' ' + price.strip() + ' '  + quantity)
                            
                    
except:
    print("unexpected error, logging out")
    

finally:
    run(usr, pw, 'CLOSE_CONNECTION')
