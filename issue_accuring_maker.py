from npsb_read import *
from issuing import *
from matching import *

class ia_maker:
    def __init__(self, proc, s_path):
        self.run = npsb_read(s_path)
        m = matching()
        self.sw_i = issuing_accuring()
        self.bd_i = issuing_accuring()

        for dlo in proc.DLO:
            if(m.binSelector(proc.getCardNumber(dlo)) != 0):
                self.bd_i.issuing.append(dlo)
            elif(m.binSelector(proc.getCardNumber(dlo)) == 0):
                self.bd_i.accuring.append(dlo)
        # df = self.run.S_PAN
        for each in self.run.S_PAN:
            # print(run.S_PAN[0])
            # index = df[df == each].index
            if(m.binSelector(each) != 0):
                self.sw_i.issuing.append(each)
            elif(m.binSelector(each) == 0):
                self.sw_i.accuring.append(each)
