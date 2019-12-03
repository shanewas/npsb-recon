import pandas as pd
pd.set_option('display.precision',20)
from pandas import ExcelWriter
from pandas import ExcelFile

from utility import utility


class npsb:
    def dataframe_difference(self, df1, df2, which=None):
        comparison_df = df1.merge(df2,
                                indicator=True,
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

        BangladeshBankIssuing_s = utility().slicer(self.BangladeshBankIssuing)
        SwitchReportIssuing_s = utility().slicer(self.SwitchReportIssuing)
        BangladeshAccuring_s = utility().slicer(self.BangladeshBankAccuring)
        SwitchReportAccuring_s = utility().slicer(self.SwitchReportAccuring)

        BangladeshBankIssuing_s['TERMRETAILERNAME'] = BangladeshBankIssuing_s['TERMRETAILERNAME'].astype(str)
        SwitchReportIssuing_s['TERMRETAILERNAME'] = SwitchReportIssuing_s['TERMRETAILERNAME'].astype(str)
        BangladeshAccuring_s['TERMRETAILERNAME'] = BangladeshAccuring_s['TERMRETAILERNAME'].astype(str)
        SwitchReportAccuring_s['TERMRETAILERNAME'] = SwitchReportAccuring_s['TERMRETAILERNAME'].astype(str)

        BangladeshBankIssuing_s['AMOUNT'] = BangladeshBankIssuing_s['AMOUNT'].astype(float)
        BangladeshAccuring_s['AMOUNT'] = BangladeshAccuring_s['AMOUNT'].astype(float)
        SwitchReportAccuring_s['AMOUNT'] = SwitchReportAccuring_s['AMOUNT'].astype(float)
        SwitchReportIssuing_s['AMOUNT'] = SwitchReportIssuing_s['AMOUNT'].astype(float)

        
        # print(BangladeshBankIssuing_s.dtypes)
        # print(SwitchReportIssuing_s.dtypes)
        # print(BangladeshAccuring_s.dtypes)
        # print(SwitchReportAccuring_s.dtypes)
        # diff1 = self.dataframe_difference(SwitchReportIssuing_s,BangladeshBankIssuing_s)
        diff2 = self.dataframe_difference(SwitchReportIssuing_s,BangladeshBankIssuing_s)
        #----------might be useful dont delete -------------------
        # df = pd.concat([BangladeshAccuring_s, SwitchReportAccuring_s])
        # df = df.reset_index(drop=True)

        # df_gpby = df.groupby(list(df.columns))

        # idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1]

        # diff2 = df.reindex(idx)
        #------------------------------------------------------------
        
        print(diff2)
        writer = pd.ExcelWriter('resources/diff.xlsx', engine='xlsxwriter')
        diff2.to_excel(writer, sheet_name="difference")
        writer.save()
    
if __name__ == "__main__":
    npsb().matching('resources/atm.xlsx')