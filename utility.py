class utility:
    def slicer(self, df):
        df.drop(df.columns.difference(['PAN','TERMNAME','TRANNUMBER',
            'TERMSIC','TERMRETAILERNAME','AMOUNT']), 1, inplace=True)
        return df