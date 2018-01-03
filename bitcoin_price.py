import requests
import time
import math

numOfCurr = 10 # number of currencies to show
currRange = numOfCurr - 1 # 1 less for the loops
timeDelay = 7 # Delay so cycles through in one minute
updateTime = 120 # How often the programs updates

def getData(): # get all the data as quickly as possible
	
	rawData = requests.get('https://api.coinmarketcap.com/v1/ticker/?convert=GBP') # coinmarketcap.com api, in GBP, all currencies they do
	
	for i in xrange (0, currRange):
		symbol.append(rawData.json()[i]['symbol'])
		cryptoGBP.append(float(rawData.json()[i]['price_gbp']))
		dayChange.append(float(rawData.json()[i]['percent_change_24h']))
		weekChange.append(float(rawData.json()[i]['percent_change_7d']))
	
	print('***Fresh Data Imported***')

def round_sigfigs(num, sig_figs):
    """Round to specified number of sigfigs.

    >>> round_sigfigs(0, sig_figs=4)
    0
    >>> int(round_sigfigs(12345, sig_figs=2))
    12000
    >>> int(round_sigfigs(-12345, sig_figs=2))
    -12000
    >>> int(round_sigfigs(1, sig_figs=2))
    1
    >>> '{0:.3}'.format(round_sigfigs(3.1415, sig_figs=2))
    '3.1'
    >>> '{0:.3}'.format(round_sigfigs(-3.1415, sig_figs=2))
    '-3.1'
    >>> '{0:.5}'.format(round_sigfigs(0.00098765, sig_figs=2))
    '0.00099'
    >>> '{0:.6}'.format(round_sigfigs(0.00098765, sig_figs=3))
    '0.000988'
    """
    if num != 0:
        return round(num, -int(math.floor(math.log10(abs(num))) - (sig_figs - 1)))
    else:
        return 0  # Can't take the log of 0
        
def showData(): # What to do with the data
	for i in xrange (0, currRange):
		
		### Make display info the correct length ###
		symbolText = str(symbol[i][:3])
		
		if symbolText == 'BTC' or symbolText == 'BCH': # Special Bitcoin case, get just the int
			coinVal = int(cryptoGBP[i])
			cryptoVal = str(coinVal)
		else:
			cryptoVal = str(round_sigfigs(cryptoGBP[i], sig_figs = 6)) # Convert float to string
		while len(cryptoVal) < 6:
			cryptoVal = ' ' + cryptoVal
		cryptoVal = cryptoVal[:6] # double check output is 6 characters
				
		oneDayChange = str(round_sigfigs(dayChange[i], sig_figs = 5)) # Convert float to string
 		while len(oneDayChange) < 5:
			oneDayChange = ' ' + oneDayChange
 		oneDayChange = oneDayChange[:5]
 		
 		oneWeekChange = str(round_sigfigs(weekChange[i], sig_figs = 5)) # Convert float to string
		while len(oneWeekChange) < 5:
			oneWeekChange = ' ' + oneWeekChange
		oneWeekChange = oneWeekChange[:5]
		
		### What to show ###
		print(symbolText + ' Value ' + unichr(163) + cryptoVal + ' 24 hr change ' + oneDayChange + '% 7 day change ' + oneWeekChange + '%')
		
		time.sleep(timeDelay)

### Main loop ###
while True:
	### Set timer variables ###
	startTime = time.time()
	currentTime = time.time()
	
	### Start accessable lists ###
	symbol = []
	cryptoGBP = []
	dayChange = []
	weekChange = []
	
	getData()
	
	while (currentTime - startTime) < updateTime: # Run this for minimum of the update time
		showData()
		currentTime = time.time()
		
		print(currentTime - startTime)
		print(' ')
