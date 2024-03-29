import pandas as pd
pd.set_option('display.precision',20)

class npsb_read:
    def __init__(self, path):
        df = pd.read_excel (path)
        self.switchFrame = df

        self.S_DATE = df['DATE_TIME']
        self.S_PAN = df['PAN']
        self.FROMACCT = df['FROMACCT']
        self.TRANCODE = df['TRANCODE']
        self.TYPE = df['TYPE']
        self.S_CONTRACTNUMBER = df['TERMNAME']
        self.TERMPSNAME = df['TERMPSNAME']
        self.AUTHFINAME = df['AUTHFINAME']
        self.S_RRN = df['TRANNUMBER']
        self.EXTRRN = df['EXTRRN']
        self.S_AUTHCODE = df['APPROVALCODE']
        self.S_MCC = df['TERMSIC']
        self.TERMOWNER = df['TERMOWNER']
        tempmerchentid = df['TERMRETAILERNAME'].astype(str)
        self.S_MERCHENTID = tempmerchentid
        tempCurrency = df['CURRENCY'].astype(float)
        self.S_CURRENCY = tempCurrency
        self.S_AMOUNT = df['AMOUNT']
        self.RESPCODE = df['RESPCODE']