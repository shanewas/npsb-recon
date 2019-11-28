from type import *
from npsb_read import *
from processor import *
class type_determine:
    def __init__(self, ia_maker, proc, hold_my_glass):
        self.atm = postype()
        self.pos = postype()
        self.ib = postype()
        self.mb = postype()
        self.kiosk = postype()
        self.other = postype()
        print(len(ia_maker))
        if isinstance(ia_maker, str):
            for each in ia_maker:
                df = hold_my_glass.datafram[hold_my_glass.S_PAN == each]
                hold_my_glass.dataframType = hold_my_glass.dataframType.append(df, ignore_index=True)

            hold = hold_my_glass.dataframType['TERMSIC']
            self.atm.count = hold_my_glass.dataframType[hold == 6011]
            self.pos.count = hold_my_glass.dataframType[hold == 6010]
            self.ib.count = hold_my_glass.dataframType[hold == 6014]
        elif(len(ia_maker) != 0):
            for each in ia_maker:
                if(proc.getMCC(each) == "6011"):
                    self.atm.count.append(each)
                elif(proc.getMCC(each) == "6010"):
                    self.pos.count.append(each)
                elif(proc.getMCC(each) == "6014"):
                    self.ib.count.append(each)
                elif(proc.getMCC(each) == "6017"):
                    self.mb.count.append(each)
                elif(proc.getMCC(each) == "6015"):
                    self.kiosk.count.append(each)
                else:
                    self.other.count.append(each)
        else:
            pass
