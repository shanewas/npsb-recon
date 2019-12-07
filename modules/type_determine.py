import modules.type as t

class type_determine:
    def __init__(self, proc, DataFrame):
        self.atm = t.postype()
        self.pos = t.postype()
        self.ib = t.postype()
        self.mb = t.postype()
        self.kiosk = t.postype()
        self.other = t.postype()

        hold = DataFrame['TERMSIC']
        hold2 = DataFrame['TERMRETAILERNAME']
        self.atm.count = DataFrame[hold == 6011]
        # self.pos.count = DataFrame[hold == 6010]

        DataFrame['Pos?'] = hold2.str.contains('70000', na=False)
        self.pos.count = DataFrame[DataFrame['Pos?'] == True]

        self.ib.count = DataFrame[hold == 6014]
