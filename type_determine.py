from type import *
from npsb_read import *
from processor import *
class type_determine:
    def __init__(self, ia_maker, proc):
        # self.df = pd.read_excel(s_path)
        # df = self.run.S_PAN
        self.atm = postype()
        self.pos = postype()
        self.ib = postype()
        self.mb = postype()
        self.kiosk = postype()
        self.other = postype()
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
        #
        # for each in ia_maker:
        #     # newdf[ a[0] ] [0]
        #     # self.df[each[0]]
        #     # index = df[df == each].index
        #     print(self.df[each][0])
