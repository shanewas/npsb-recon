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
        self.hold_my_glass = self.ia_maker.run
        self.bd_issuing = type_determine(self.ia_maker.bd_i.issuing, proc, self.hold_my_glass)
        # self.bd_accuring = type_determine(self.ia_maker.bd_i.accuring, proc, self.hold_my_glass)
        self.sw_issuing = type_determine(self.ia_maker.sw_i.issuing, proc, self.hold_my_glass)
        # self.sw_accuring = type_determine(self.ia_maker.sw_i.accuring, proc, self.hold_my_glass)
        # self.sw_issuing = type_determine(self.ia_maker, proc)
            # hold_my_glass = p1.ia_maker.run

    def print(self, dlo):
        p = processor()
        # for dlo in p.DLO:
        # dlo = p.DLO[0]
        # print("Date: " + p.getTransactionDate(dlo))
        print("card: " + p.getCardNumber(dlo))
        # print("rrn: " + p.getRRN(dlo))
        # print("arn: " + str(p.getARN(dlo)))
        # print("auth: " + p.getAuthCode(dlo))
        print("mcc: " + p.getMCC(dlo))
        print("req: " + p.getRequestCategory(dlo))
        # print("msg: " + str(p.getMsgCode(dlo)))
        print("type: " + p.getTransTypeCode(dlo))
        # print("Billing amount: " + p.getBRInfo(dlo.BILLING, 'Amount'))
        # print("MID: " + p.getMerchantID(dlo))
        # print("MNANE: " + p.getMerchantName(dlo))
        # print("contract Number: " + p.getContractNumber(dlo))
        # print("Memberid: " + p.getMemberId(dlo))
        print("srvc: " + p.getSCInfo(dlo, 'SRVC'))
        print("cpid: " + p.getSCInfo(dlo, 'CPID'))


if __name__ == '__main__':
    switch_report = (r'resources/NPSB_ISS_ACQ_TRX_export_20_OCT_2019.xlsx')
    p1 = parsing('resources/OIC_Documents_245_000245_20191021_38.xml', switch_report)

    # p = processor()

    iatm = p1.bd_issuing.atm
    # aatm = p1.bd_accuring.atm
    satm = p1.sw_issuing.watm
    # saccu = p1.sw_accuring.watm
    # df = pd.DataFrame()
    # def checker():

    print(len(satm))
    print(len(iatm.count))

    # for each in iatm.count:
    #     # print(p.getBRInfo(each.BILLING,'Amount'))
    #     p1.print(each)
    #     print('----------------------------')

    # atm_writer = pd.ExcelWriter('resources/atm.xlsx', engine='xlsxwriter')
    # atm_writer2 = pd.ExcelWriter('resources/atm_acc.xlsx', engine='xlsxwriter')
    # # pos_writer = pd.ExcelWriter('resources/pos.xlsx', engine='xlsxwriter')
    # # ib_writer = pd.ExcelWriter('resources/ib.xlsx', engine='xlsxwriter')
    #
    # saccu.to_excel(atm_writer2, sheet_name='filtered')
    # satm.to_excel(atm_writer, sheet_name='filtered')

    # atm_writer.save()
    # atm_writer2.save()
    print('-----------------------')
