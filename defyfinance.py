import yfinance as yf

def cotacao(bid):
    try:
        c = yf.Ticker(bid).info.get('currentPrice')
        return c
    except:
        try:
            c = yf.Ticker(bid+'.SA').info.get('currentPrice')
            return c
        except:
            return 0  

def moeda(val):
    try:
        m = yf.Ticker(val).info.get('currency')
        if (m == 'USD'):
            return '$'
        elif (m == 'BRL'):
            return 'R$'
        elif (m == 'GBp'):
            return '£'
        elif (m == 'EUR'):
            return '€'
        else:
            return m
    except:
        try:
            m = yf.Ticker(val+'.SA').info.get('currency')
            if (m == 'BRL'):
                return 'R$'
            else:
                return m
        except:
            return 'Ticker Inválido' 
          
def nome(_name):
    try:
        n = yf.Ticker(_name).info.get('shortName')
        return n
    except:
        try:
            n = yf.Ticker(_name+'.SA').info.get('shortName')
            return n
        except:
            return '-'


#ticker = str(input('Digite um Ticker: ')).upper()

#print(f'A cotação atual de {ticker} = {moeda(ticker)} {cotacao(ticker):.2f}')
#t = yf.Ticker(ticker)
#print(f'{t.info}')