import xml.etree.ElementTree as ET
import threading
from doclist import *
# from recon import *
from processor import *
from npsb_read import *
from issue_accuring_maker import *
from type_determine import *
from recon import *
from converter import *
class parsing:
    def __init__(self, path, s_path):
        tree = ET.parse(path)
        root = tree.getroot()
        # get [0,1,2 etc of child tag . e.g: Fileheader, DocList, FileTrailer]
        FILEHEADER = root[0]
        DOCLIST = root[1]
        FILETRAILER = root[2]
        self.proc = processor()
        # p = processor()
        for doc in DOCLIST:
            self.proc.DLO.append(
                docListBuild(doc[0], doc[1], doc[2], doc[3], doc[4], doc[5], doc[6], doc[7], doc[8], doc[9]))


        self.ia_maker = ia_maker(self.proc, s_path)
        bdi_frame = self.ia_maker.B_PAN_issuing
        bda_frame = self.ia_maker.B_PAN_accuring
        swi_frame = self.ia_maker.S_PAN_issuing
        swa_frame = self.ia_maker.S_PAN_accuring

        self.bd_issuing = type_determine(self.proc, bdi_frame)
        self.bd_accuring = type_determine(self.proc, bda_frame)
        self.sw_issuing = type_determine(self.proc, swi_frame)
        self.sw_accuring = type_determine(self.proc, swa_frame)

        print(self.bd_issuing.atm.count)
        print(self.bd_accuring.atm.count)
        print(self.sw_issuing.atm.count)
        print(self.sw_accuring.atm.count)
        # print(swi_frame)
        # print(swa_frame)

    def print(self, dlo):
        p = processor()
        return p.getTransactionDate(dlo)
        # for dlo in p.DLO:
        # dlo = p.DLO[0]
        # print("Date: " + p.getTransactionDate(dlo))
        # print("card: " + p.getCardNumber(dlo))
        # print("rrn: " + p.getRRN(dlo))
        # print("arn: " + str(p.getARN(dlo)))
        # print("auth: " + p.getAuthCode(dlo))
        # print("mcc: " + p.getMCC(dlo))
        # print("req: " + p.getRequestCategory(dlo))
        # print("msg: " + str(p.getMsgCode(dlo)))
        # print("type: " + p.getTransTypeCode(dlo))
        # print("Billing amount: " + p.getBRInfo(dlo.BILLING, 'Amount'))
        # print("MID: " + p.getMerchantID(dlo))
        # print("MNANE: " + p.getMerchantName(dlo))
        # print("contract Number: " + p.getContractNumber(dlo))
        # print("Memberid: " + p.getMemberId(dlo))
        # print("srvc: " + p.getSCInfo(dlo, 'SRVC'))
        # print("cpid: " + p.getSCInfo(dlo, 'CPID'))

class assign:
    def __init__(self):
        self.list = []

if __name__ == '__main__':
    switch_report = (r'resources/NPSB_ISS_ACQ_TRX_export_20_OCT_2019.xlsx')
    p1 = parsing('resources/OIC_Documents_245_000245_20191021_38.xml', switch_report)
    # dlo = p1.proc.DLO

    # recon = recon()
    # p = processor()
    # converter = converter()
    # print(converter.convert(dlo, p, recon))


    # abatm = p1.bd_accuring.atm
    # asatm = p1.sw_accuring.atm
    # ibatm = p1.bd_issuing.atm
    # isatm = p1.sw_issuing.atm
    # # iatm = p1.sw_issuing.atm
    # df = pd.DataFrame()
    # def checker():
    #     for each in isatm:
    #
    #
    # print("issuing atm bd: " + str(len(ibatm.count)))
    # print("issuing atm sw: " + str(len(isatm.count)))
    # print("accuring atm bd: " + str(len(abatm.count)))
    # print("accuring atm bd: " + str(len(asatm.count)))
    # print(len(satm.count))
    # print(satm.count['PAN'][0])
    # for each in iatm.count:
    #     # print(p.getBRInfo(each.BILLING,'Amount'))
    #     p1.print(each)
    #     print('----------------------------')
    # for each in aatm.count:
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
