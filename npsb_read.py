import pandas as pd

class npsb_read:
    def __init__(self, path):
        df = pd.read_excel (path)
        #S_ means mapped with switch & BD bank
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
        self.S_MERCHENTID = df['TERMRETAILERNAME']
        self.S_CURRENCY = df['CURRENCY']
        self.S_AMOUNT = df['AMOUNT']
        self.RESPCODE = df['RESPCODE']

# if __name__ == '__main__':
#     loc = (r"resources/NPSB_ISS_ACQ_TRX_export_OCT_2019_updated.xlsx")
#     loc1 = (r'resources/pandas_simple.xlsx')
#     loc2 = (r'resources/NPSB_ISS_ACQ_TRX_export_20_OCT_2019.xlsx')
#     run = npsb_read(loc2)
#     for i in run.S_PAN:
#         print(i)
