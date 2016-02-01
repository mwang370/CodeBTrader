import socket
import sys
    

def run(user, password, *commands):
    HOST, PORT = "codebb.cloudapp.net", 17429

    
    data=user + " " + password + "\n" + "\n".join(commands) + "\nCLOSE_CONNECTION\n"

    returnArray = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.connect((HOST, PORT))
        sock.sendall(bytes(data, "utf-8"))
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            returnArray.append(rline.strip())
            rline = sfile.readline()
        return (returnArray)

def subscribe(user, password):
    HOST, PORT = "codebb.cloudapp.net", 17429
    
    data=user + " " + password + "\nSUBSCRIBE\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.connect((HOST, PORT))
        sock.sendall(bytes(data, "utf-8"))
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            print(rline.strip())
            rline = sfile.readline()
            
def getSecurities():
    usr = 'LimitlessDrive'
    pw = 'stopeatinginvisiblecows123'

    x = run(usr,pw,"SECURITIES")
    y = x[0].split()

    stockDict = {}
    latestKey = ""
    
    for i in range(1, len(y)):
        if i % 4 == 1:
            latestKey = y[i]
            stockDict[latestKey] = ""
        else:
           stockDict[latestKey] = stockDict[latestKey] + (y[i]) + " "
    
    for i in sorted(stockDict):
        stockDict[i] = stockDict[i].split()

    return stockDict

def getMySecurities():
    usr = 'LimitlessDrive'
    pw = 'stopeatinginvisiblecows123'

    x = run(usr,pw, "MY_SECURITIES")
    y = x[0].split()

    stockDict = {}
    latestKey = ""
    for i in range(1, len(y)):
        latestKey = y[i-1]
        if i % 3 == 2:
            if int(y[i]) > 0:
                stockDict[latestKey] = y[i]

    return stockDict

def getTop3(names, divs):
    maxDiv = []
    for i in range(3):
        m = int(divs.index(max(divs)))
        maxDiv.append(names[m])
        divs.pop(m)
        names.pop(m)
    return maxDiv

def getCash():
    usr = 'LimitlessDrive'
    pw = 'stopeatinginvisiblecows123'

    x = run(usr,pw, "MY_CASH")
    y = x[0].split()

    return float(y[1])

def maxBid(ticker):
    parameter = "ORDERS " + ticker
    maxBid = 0;

    allOrders = run('LimitlessDrive', 'stopeatinginvisiblecows123', parameter)
    separated = allOrders[0].split()


    for i in range(1, len(separated)):
        if separated[i] == 'BID':
            if float (separated[i+2]) > maxBid:
                maxBid = float (separated[i+2])

    return round(maxBid, 3)

def minAsk(ticker):
    parameter = "ORDERS " + ticker
    minAsk = 100000000
    allOrders = run('LimitlessDrive', 'stopeatinginvisiblecows123', parameter)
    separated = allOrders[0].split()

    for i in range(1, len(separated)):
        if separated[i] == 'ASK':
            if float (separated[i+2]) < minAsk:
                minAsk = float (separated[i+2])
    return round(minAsk, 3)
