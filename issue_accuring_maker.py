from npsb_read import *
from issuing import *
from matching import *
import pandas as pd
from recon import *
from converter import *
class ia_maker:
    def __init__(self, proc, s_path):
        self.switchread = npsb_read(s_path)
        self.recon = recon()
        dlo = proc.DLO
        self.converter = converter()
        self.swframe = self.switchread.switchFrame
        self.bdframe = self.converter.convert(dlo, proc, self.recon)
        # m = matching()

        B_PAN = self.bdframe
        B_PAN['IA Status'] = B_PAN['PAN'].str.contains('462870|526238')
        self.B_PAN_issuing = B_PAN[B_PAN['IA Status'] == True]
        self.B_PAN_accuring = B_PAN[B_PAN['IA Status'] == False]

        S_PAN = self.swframe
        S_PAN['IA Status'] = S_PAN['PAN'].str.contains('462870|526238')
        self.S_PAN_issuing = S_PAN[S_PAN['IA Status'] == True]
        self.S_PAN_accuring = S_PAN[S_PAN['IA Status'] != False]


        # self.sw_i = issuing_accuring()
        # self.bd_i = issuing_accuring()
        #
        # for each in B_PAN:
        #     if(m.binSelector(each) != 0):
        #         self.bd_i.issuing.append(each)
        #     elif(m.binSelector(each) == 0):
        #         self.bd_i.accuring.append(each)
        #
        # for each in S_PAN:
        #     if(m.binSelector(each) != 0):
        #         self.sw_i.issuing.append(each)
        #     elif(m.binSelector(each) == 0):
        #         self.sw_i.accuring.append(each)
