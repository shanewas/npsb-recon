import pandas as pd
pd.set_option('display.precision',20)

from utility import slicer


class npsb:
    def __init__(self, path):
        self.BangladeshBankIssuing = pd.read_excel(path, 
                            sheetname='Bangladesh Bank Issuing')
        self.BangladeshBankAccuring = pd.read_excel(path, 
                            sheetname='Bangladesh Bank Accuring')
        self.SwitchReportIssuing = pd.read_excel(path, 
                            sheetname='Switch Report Issuing')
        self.SwitchReportAccuring = pd.read_excel(path, 
                            sheetname='Switch Report Accuring')


    # def matching( ):
    #     slicer(df)