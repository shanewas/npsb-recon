import json
class analyzer:
    def analysis(self, df, name):
        df1 = df['DiffIssuing']
        df2 = df['DiffAccuring']
        i_Bangladesh_Bank =  self.judgement(df1, 'right_only')
        i_Switch =  self.judgement(df1, 'left_only')
        s_Bangladesh_Bank =  self.judgement(df2, 'right_only')
        s_Switch =  self.judgement(df2, 'left_only')
        return [i_Bangladesh_Bank, i_Switch, s_Bangladesh_Bank, s_Switch]
                

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