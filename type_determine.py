from type import *

class type_determine:
    def __init__(self, proc, DataFrame):
        self.atm = postype()
        self.pos = postype()
        self.ib = postype()
        self.mb = postype()
        self.kiosk = postype()
        self.other = postype()

        hold = DataFrame['TERMSIC']
        hold2 = DataFrame['TERMRETAILERNAME']
        self.atm.count = DataFrame[hold == 6011]
        self.pos.count = DataFrame[hold == 6010]
        # hold2 = hold2.str.contains('7000', na=False)
        # print(hold2)
        self.ib.count = DataFrame[hold == 6014]
