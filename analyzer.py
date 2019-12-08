import json
class analyzer:
    def analysis(self, df, name):
        df1 = df['DiffIssuing']
        df2 = df['DiffAccuring']
        i_Bangladesh_Bank =  self.judgement(df1, 'right_only')
        i_Switch =  self.judgement(df1, 'left_only')
        a_Bangladesh_Bank =  self.judgement(df2, 'right_only')
        a_Switch =  self.judgement(df2, 'left_only')

        i_Bangladesh_Bank = self.BDdropper(i_Bangladesh_Bank)
        a_Bangladesh_Bank = self.BDdropper(a_Bangladesh_Bank)
        i_Switch = self.SWdropper(i_Switch)
        a_Switch = self.SWdropper(a_Switch)
        # i_Bangladesh_Bank.dropna(axis='columns', inplace = True)
        # a_Bangladesh_Bank.dropna(axis='columns', inplace = True)
        # i_Switch.dropna(axis='columns', inplace = True)
        # a_Switch.dropna(axis='columns', inplace = True)
        return [i_Bangladesh_Bank, i_Switch, a_Bangladesh_Bank, a_Switch]
                
    def BDdropper(self, df):
        df.drop(['Unnamed: 0_x', 'index_x', 'DATE_TIME_x',  'FROMACCT',  
                'TRANCODE', 'TYPE', 'TERMNAME_x',  'TERMPSNAME',  'AUTHFINAME',  
                'TRANNUMBER_x',  'EXTRRN',  'TERMSIC_x',  'TERMOWNER',  'TERMRETAILERNAME_x', 
                'CURRENCY_x',  'RESPCODE',  'IA Status_x',  'Unnamed: 0_y',  'index_y', 'IA Status_y',
                '_merge'], axis=1, inplace=True)
        return df
    def SWdropper(self, df):
        df.drop(['Unnamed: 0_x','IA Status_x', 'index_x', 'Unnamed: 0_y', 'index_y',  'DATE_TIME_y',  
                'TERMNAME_y', 'TRANNUMBER_y', 'ARN',  'TERMSIC_y',  'REQUESTCATEGORY',  
                'MSGCODE',  'TRANSTYPE',  'TERMRETAILERNAME_y',  'CURRENCY_y',  'MERCHANTNAME', 
                'MEMBERID',  'IA Status_y',  '_merge'], axis=1, inplace=True)
        return df

    def judgement(self, df, tag):
        df = df[df['_merge'] == tag]
        # df.dropna(inplace = True)
        # hold = df.to_dict(orient='records')
        return df



        #x = {
        #         "Type": name,
        #         "Difference": 
        #                     [
        #                         {
        #                             'Issuing' : 
        #                                 [
        #                                     {'Bangladesh Bank' : self.judgement(df1, 'right_only')},
        #                                     {'Switch' : self.judgement(df1, 'left_only')}
        #                                 ]
        #                         },
        #                         {
        #                             'Accuring' :
        #                                 [
        #                                     {'Bangladesh Bank' : self.judgement(df2, 'right_only')},
        #                                     {'Switch' : self.judgement(df2, 'left_only')}
        #                                 ] 
        #                         }
                                
        #                     ]
        #     }
        # # y = json.dumps(x)

#         from pandas import DataFrame
# import numpy as np

# firstProductSet = {'Product1': ['Computer','Phone','Printer','Desk'],
#                    'Price1': [1200,800,200,350]
#                    }
# df1 = DataFrame(firstProductSet,columns= ['Product1', 'Price1'])


# secondProductSet = {'Product2': ['Computer','Phone','Printer','Desk'],
#                     'Price2': [900,800,300,350]
#                     }
# df2 = DataFrame(secondProductSet,columns= ['Product2', 'Price2'])


# df1['Price2'] = df2['Price2'] #add the Price2 column from df2 to df1

# df1['pricesMatch?'] = np.where(df1.Price1 == df2.Price2, 'True', 'False')  #create new column in df1 to check if prices match
# df1['priceDiff?'] = np.where(df1.Price1 == df2.Price2, '0', df1.Price1 - df2.Price2) #create new column in df1 for price diff 
# print (df1)