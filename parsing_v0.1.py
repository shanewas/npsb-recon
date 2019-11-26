import xml.etree.ElementTree as ET
import threading
from doclist import *
# from recon import *
from processor import *
from npsb_read import *
from matching import *
from issuing import *
from issue_accuring_maker import *
from type_determine import *

class parsing:
    def __init__(self, path, s_path):
        tree = ET.parse(path)
        root = tree.getroot()
        # get [0,1,2 etc of child tag . e.g: Fileheader, DocList, FileTrailer]
        FILEHEADER = root[0]
        DOCLIST = root[1]
        FILETRAILER = root[2]
        proc = processor()
        # p = processor()
        for doc in DOCLIST:
            proc.DLO.append(
                docListBuild(doc[0], doc[1], doc[2], doc[3], doc[4], doc[5], doc[6], doc[7], doc[8], doc[9]))

        self.ia_maker = ia_maker(proc, s_path)

        self.bd_issuing = type_determine(self.ia_maker.bd_i.issuing, proc)
        self.bd_accuring = type_determine(self.ia_maker.bd_i.accuring, proc)
        # self.sw_issuing = type_determine(self.ia_maker.sw_i.issuing, proc)
        # self.sw_accuring = type_determine(self.ia_maker.sw_i.accuring, proc)

    def print(self):
        p = processor()
        # for dlo in p.DLO:
        dlo = p.DLO[0]
        print("Date: " + p.getTransactionDate(dlo))
        print("card: " + p.getCardNumber(dlo))
        print("rrn: " + p.getRRN(dlo))
        print("arn: " + str(p.getARN(dlo)))
        print("auth: " + p.getAuthCode(dlo))
        print("mcc: " + p.getMCC(dlo))
        print("req: " + p.getRequestCategory(dlo))
        print("msg: " + str(p.getMsgCode(dlo)))
        print("type: " + p.getTransTypeCode(dlo))
        print("Billing amount: " + p.getBRInfo(dlo.BILLING, 'Amount'))
        print("MID: " + p.getMerchantID(dlo))
        print("MNANE: " + p.getMerchantName(dlo))
        print("contract Number: " + p.getContractNumber(dlo))
        print("Memberid: " + p.getMemberId(dlo))
        print("srvc: " + p.getSCInfo(dlo, 'SRVC'))
        print("cpid: " + p.getSCInfo(dlo, 'CPID'))


if __name__ == '__main__':
    loc2 = (r'resources/NPSB_ISS_ACQ_TRX_export_20_OCT_2019.xlsx')
    p1 = parsing('resources/OIC_Documents_245_000245_20191021_38.xml', loc2)

    # p1.print()
    # p = parsing('resources/OIC_Documents_245_000130_20191021_38.xml')
    # print("------------------------")
    # p.print()
    # p130.print()
    # p = processor()
    # m = matching()
    # sw_i = issuing_accuring()
    p = processor()



    # for dlo in p.DLO:
    dlo = p.DLO[0]
    bd_i = p1.ia_maker.bd_i
    iatm = p1.bd_issuing.atm
    aatm = p1.bd_accuring.atm
    # siatm = p1.sw_issuing.atm
    # saatm = p1.sw_accuring.atm
    print(len(iatm.count))
    print(len(aatm.count))
    # print(len(siatm.count))
    # print(len(saatm.count))
    # for each in atm.count:
    # print(len(p.getMCC(iatm.count)))
    # print(len(p.getMCC(aatm.count)))
    # print(len(bd_i.issuing))
    # print(len(bd_i.accuring))
    # print(len(bd_i.s_issuing))
    # print(len(bd_i.s_accuring))
    print('-----------------------')
    # run = npsb_read(loc2)
    # p1.
    sw_i = p1.ia_maker.sw_i

    # bd_i = issuing_accuring()
    # print(len(sw_i.issuing))
    # print(len(sw_i.accuring))
    # print(len(sw_i.s_issuing))
    # print(len(sw_i.s_accuring))
    print('-----------------------')

    # def p245():
    #     p245 = parsing('resources/OIC_Documents_245_000245_20191021_38.xml')
    #     p245.print()
    #     print('------------------------')

    # def p130():
    #     p130 = parsing('resources/OIC_Documents_245_000130_20191021_38.xml')
    #     p130.print()
    #     print('------------------------')

    #     # creating thread
    # p245 = threading.Thread(target=p245, args=())
    # p130 = threading.Thread(target=p130, args=())

    # # starting thread 1
    # p245.start()
    # # starting thread 2
    # p130.start()

    # # wait until thread 1 is completely executed
    # # p245.join()
    # # # wait until thread 2 is completely executed
    # # p130.join()
