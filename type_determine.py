from type import *
from npsb_read import *
from processor import *
import pandas as pd
class type_determine:
    def __init__(self, proc, DataFrame):
        self.atm = postype()
        self.pos = postype()
        self.ib = postype()
        self.mb = postype()
        self.kiosk = postype()
        self.other = postype()
        # length = len(ia_maker)
        # self.df = pd.DataFrame()
        # for each in ia_maker:
        #     df = DataFrame[DataFrame['PAN'] == each]
        #     self.df = self.df.append(df, ignore_index=True)

        hold = DataFrame['TERMSIC']
        # print(hold)
        # self.atm.count =
        self.atm.count = DataFrame[hold == '6011']
        self.pos.count = DataFrame[hold == '6010']
        self.ib.count = DataFrame[hold == '6014']
