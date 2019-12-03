import xml.etree.ElementTree as ET
import threading
import numpy as np

from doclist import docListBuild
from processor import processor
from npsb_read import npsb_read
from issue_accuring_maker import ia_maker
from type_determine import type_determine
from recon import recon
from converter import converter

class parsing:
    def __init__(self, path130, path245, s_path):
        tree130 = ET.parse(path130)
        tree245 = ET.parse(path245)
        root130 = tree130.getroot()
        root245 = tree245.getroot()
        # get [0,1,2 etc of child tag . e.g: Fileheader, DocList, FileTrailer]
        # FILEHEADER = root130[0]
        DOCLIST130 = root130[1]
        DOCLIST245 = root245[1]
        # FILETRAILER = root130[2]
        self.proc = processor()
        for doc in DOCLIST130:
            self.proc.DLO.append(
                docListBuild(doc[0], doc[1], doc[2], doc[3], doc[4], doc[5], doc[6], doc[7], doc[8], doc[9]))
        for doc in DOCLIST245:
            self.proc.DLO.append(
                docListBuild(doc[0], doc[1], doc[2], doc[3], doc[4], doc[5], doc[6], doc[7], doc[8], doc[9]))
        self.ia_maker = ia_maker(self.proc, s_path)

    def defination_match(self,frame):
        self.manager = type_determine(self.proc, frame)
        return self.manager

    def slicing(self, df):
        df.drop(df.columns.difference(['PAN','TERMNAME','TRANNUMBER',
            'TERMSIC','TERMRETAILERNAME','AMOUNT']), 1, inplace=True)
        return df

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
    p1 = parsing('resources/OIC_Documents_245_000130_20191021_38.xml',
                    'resources/OIC_Documents_245_000245_20191021_38.xml', switch_report)
    ba = p1.defination_match(p1.ia_maker.S_PAN_issuing)
    atm = p1.slicing(ba.atm.count)
    # pos = p1.slicing(ba.pos.count)
    # ib = p1.slicing(ba.ib.count)
    print(atm)
    # a = pd.concat([bi,si],axis=1)
    # a = atm[atm['TRANNUMBER'] == 102010395491]
    # b = type(si[atm?['TRANNUMBER'] == 102010395491]['AMOUNT'][849])
    # if (a == b):
    # print(a)
    # print(bi[bi['PAN'] == '462870******4021'])
    # print(si[si['PAN'] == '462870******4021'])

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
