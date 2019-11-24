import xml.etree.ElementTree as ET
import threading
from doclist import *
# from recon import *
from processor import *

class parsing:
    def __init__(self, path):
        tree = ET.parse(path)
        self.root = tree.getroot()
        # get [0,1,2 etc of child tag . e.g: Fileheader, DocList, FileTrailer]
        self.FILEHEADER = self.root[0]
        self.DOCLIST = self.root[1]
        self.FILETRAILER = self.root[2]
        self.proc = processor()
        for doc in self.DOCLIST:
            self.proc.DLO.append(
                docListBuild(doc[0], doc[1], doc[2], doc[3], doc[4], doc[5], doc[6], doc[7], doc[8], doc[9]))

    def print(self):
        p = processor()
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
    
    p1 = parsing('resources/OIC_Documents_245_000245_20191021_38.xml')
    p1.print()
    p = parsing('resources/OIC_Documents_245_000130_20191021_38.xml')
    print("------------------------")
    p.print()
    # p130.print()

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

