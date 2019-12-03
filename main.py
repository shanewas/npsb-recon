import pandas as pd
from parse import parsing
from writer import writer
if __name__ == '__main__':
    switch_report = (r'resources/NPSB_ISS_ACQ_TRX_export_20_OCT_2019.xlsx')
    p1 = parsing('resources/OIC_Documents_245_000130_20191021_38.xml',
                    'resources/OIC_Documents_245_000245_20191021_38.xml', switch_report)
    bdIssuing = p1.defination_match(p1.ia_maker.B_PAN_issuing)
    bdAccuring = p1.defination_match(p1.ia_maker.B_PAN_accuring)
    switchIssuing = p1.defination_match(p1.ia_maker.S_PAN_issuing)
    switchAccuring = p1.defination_match(p1.ia_maker.S_PAN_accuring)

    bd_I_ATM = bdIssuing.atm.count.reset_index()
    bd_A_ATM = bdAccuring.atm.count.reset_index()
    sw_I_ATM = switchIssuing.atm.count.reset_index()
    sw_A_ATM = switchAccuring.atm.count.reset_index()

    bd_I_POS = bdIssuing.pos.count.reset_index()
    bd_A_POS = bdAccuring.pos.count.reset_index()
    sw_I_POS = switchIssuing.pos.count.reset_index()
    sw_A_POS = switchAccuring.pos.count.reset_index()
    
    atmList = {'Bangladesh Bank Issuing' : bd_I_ATM, 
                'Bangladesh Bank Accuring' : bd_A_ATM,
                'Switch Report Issuing' : sw_I_ATM,
                'Switch Report Accuring' : sw_A_ATM}

    posList = {'Bangladesh Bank Issuing' : bd_I_POS,
                'Bangladesh Bank Accuring' : bd_A_POS,
                'Switch Report Issuing' : sw_I_POS,
                'Switch Report Accuring' : sw_A_POS}
    
    atm = writer('resources/atm.xlsx')
    pos = writer('resources/pos.xlsx')

    atm.open()
    atm.write(atmList)
    atm.close()

    pos.open()
    pos.write(posList)
    pos.close()