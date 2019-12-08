import pandas as pd
import json
import numpy as np
pd.set_option('display.precision',20)
from pandas import ExcelWriter
from pandas import ExcelFile
from analyzer import * 
from utility import utility


class npsb:
    def dataframe_difference(self, df1, df2, which=None):
        comparison_df = df1.merge(df2,
                                indicator=True,
                                on=['APPROVALCODE', 'PAN', 'AMOUNT'],
                                how='outer')
        if which is None:
            diff_df = comparison_df[comparison_df['_merge'] != 'both']
        else:
            diff_df = comparison_df[comparison_df['_merge'] == which]
        return diff_df

    def matching(self, path):
        self.BangladeshBankIssuing = pd.read_excel(path, 
                            sheet_name='Bangladesh Bank Issuing')
        self.BangladeshBankAccuring = pd.read_excel(path, 
                            sheet_name='Bangladesh Bank Accuring')
        self.SwitchReportIssuing = pd.read_excel(path, 
                            sheet_name='Switch Report Issuing')
        self.SwitchReportAccuring = pd.read_excel(path, 
                            sheet_name='Switch Report Accuring')

        # BangladeshBankIssuing_s = utility().slicer(self.BangladeshBankIssuing)
        # SwitchReportIssuing_s = utility().slicer(self.SwitchReportIssuing)
        # BangladeshAccuring_s = utility().slicer(self.BangladeshBankAccuring)
        # SwitchReportAccuring_s = utility().slicer(self.SwitchReportAccuring)

        # BangladeshBankIssuing_s['TERMRETAILERNAME'] = BangladeshBankIssuing_s['TERMRETAILERNAME'].astype(str)
        # SwitchReportIssuing_s['TERMRETAILERNAME'] = SwitchReportIssuing_s['TERMRETAILERNAME'].astype(str)
        # BangladeshAccuring_s['TERMRETAILERNAME'] = BangladeshAccuring_s['TERMRETAILERNAME'].astype(str)
        # SwitchReportAccuring_s['TERMRETAILERNAME'] = SwitchReportAccuring_s['TERMRETAILERNAME'].astype(str)

        self.BangladeshBankIssuing['AMOUNT'] = self.BangladeshBankIssuing['AMOUNT'].astype(float)
        self.BangladeshBankAccuring['AMOUNT'] = self.BangladeshBankAccuring['AMOUNT'].astype(float)
        self.SwitchReportAccuring['AMOUNT'] = self.SwitchReportAccuring['AMOUNT'].astype(float)
        self.SwitchReportIssuing['AMOUNT'] = self.SwitchReportIssuing['AMOUNT'].astype(float)

        
        diffAccuring = self.dataframe_difference(self.SwitchReportAccuring,self.BangladeshBankAccuring)
        diffIssuing = self.dataframe_difference(self.SwitchReportIssuing,self.BangladeshBankIssuing)
        #----------might be useful dont delete -------------------
        # df = pd.concat([BangladeshAccuring_s, SwitchReportAccuring_s])
        # df = df.reset_index(drop=True)

        # df_gpby = df.groupby(list(df.columns))

        # idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1]

        # diff2 = df.reindex(idx)
        #------------------------------------------------------------
        
        return {'DiffIssuing' : diffIssuing,
                'DiffAccuring' : diffAccuring}

    
    def fastWrite(self, data, path):
        writer = pd.ExcelWriter(path, engine='xlsxwriter')
        #[i_Bangladesh_Bank, i_Switch, a_Bangladesh_Bank, a_Switch]
        data[0].to_excel(writer, sheet_name='Issuing not on Switch')
        data[2].to_excel(writer, sheet_name='Accuring not on Switch')
        data[1].to_excel(writer, sheet_name='issuing not on BB')
        data[3].to_excel(writer, sheet_name='accuring not on BB')
        writer.save()

if __name__ == "__main__":
    atm_ = npsb().matching('resources/atm.xlsx')
    pos_ = npsb().matching('resources/pos.xlsx')

    atm_ana = analyzer()
    pos_ana = analyzer()

    outA = atm_ana.analysis(atm_ , 'atm')
    outP = atm_ana.analysis(pos_ , 'pos')
    
    npsb().fastWrite(outA, 'resources/ATM_Difference.xlsx')
    npsb().fastWrite(outP, 'resources/POS_Difference.xlsx')