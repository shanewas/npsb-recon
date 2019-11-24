import xml.etree.ElementTree as ET
# import threading
from doclist import *
from recon import *
from processor import *

tree = ET.parse('resources/OIC_Documents_245_000245_20191021_38.xml')
root = tree.getroot()

# get [0,1,2 etc of child tag . e.g: Fileheader, DocList, FileTrailer]
FILEHEADER = root[0]
DOCLIST = root[1]
FILETRAILER = root[2]


def collector():
    i = 0
    j = 0
    for dlo in processor.DLO:
        # msgcode = processor.msgCode(dlo)
        # if(msgcode == "DcP--01-"):
        #     print(processor.msgCode(dlo))
        #     print(dlo.DESTINATION[0].text)
        # accuring = dlo.DESTINATION[0].text
        # check = accuring[0:6]
        # # print(check)
        # if(check != "462870"):
        #     i = i +1
        #     if(dlo.DESTINATION[0].text[0:6] != "000245"):
        #         # print(dlo.SOURCEDTLS[0].text)
        #         print(dlo.DESTINATION[0].text)
        #         print(str(dlo.SOURCEDTLS[-2].tag) + ": " + str(dlo.SOURCEDTLS[-2].text))
        #         print("Msg Code: " + str(processor.msgCode(dlo)))
        # else:
        #     j = j+1
            # print(dlo.DESTINATION[0].text)
    # print("issuing = " + str(i)+'----- accuring = '+ str(j))
            i = i + 1
            # print("Transaction Date: " + str(dlo.LOCALDT.text))
            # print("Card Number: "+ str(dlo.DESTINATION[0].text))
            # print("RRN: " + str(processor.getRRN(dlo)))
            # print("ARN: " + str(processor.getARN(dlo)))
            # processor.authCode(dlo)
            # print("MCC: " + str(dlo.SOURCEDTLS[0].text))
            # print("Request Category: " + str(processor.requestCategory(dlo)))
            # print("Msg Code: " + str(processor.msgCode(dlo)))
            # print("Transaction Type: " + str(processor.transTypeCode(dlo)))
            # print("BILLING PhaseDate: "+ str(processor._Bi_Re(dlo, dlo.BILLING)['PhaseDate']))
            # print("BILLING Currency: "+ str(processor._Bi_Re(dlo, dlo.BILLING)['Currency']))
            # print("BILLING Amount: " + str(processor._Bi_Re(dlo, dlo.BILLING)['Amount']))
            # # MerchantName
            # print(str(dlo.SOURCEDTLS[-2].tag) + ": " + str(dlo.SOURCEDTLS[-2].text))
            # # MerchantID
            # print(str(dlo.SOURCEDTLS[-1].tag) + ": " + str(dlo.SOURCEDTLS[-1].text))
            # # ContractNumber
            # print(str(dlo.ORIGINATOR[0].tag) + ': ' + str(dlo.ORIGINATOR[0].text))
            # MemberId
            # print(str(dlo.ORIGINATOR[1].tag) + ': ' + str(dlo.ORIGINATOR[1].text))
            print("SRVC: " + str(processor._cpid_srvc(dlo)['SRVC']))
            print("CPID: " + str(processor._cpid_srvc(dlo)['CPID']))
            # print("Recon PhaseDate: "+ str(processor._Bi_Re(dlo, dlo.RECONCILIATION)['PhaseDate']))
            # print("Recon Currency: "+ str(processor._Bi_Re(dlo, dlo.RECONCILIATION)['Currency']))
            # print("Recon Amount: " + str(processor._Bi_Re(dlo, dlo.RECONCILIATION)['Amount']))
            print('------------------------------------------------------------------')

    print(i)

    # t1.start()
    # # starting thread 2
    # t2.start()
    #
    # # wait until thread 1 is completely executed
    # t1.join()
    # # wait until thread 2 is completely executed
    # t2.join()

if __name__ == '__main__':
    for doc in DOCLIST:
        processor.DLO.append(
            docListBuild(doc[0], doc[1], doc[2], doc[3], doc[4], doc[5], doc[6], doc[7], doc[8], doc[9]))
    # print(processor.getARN(0))
    # processor.authCode(0)
    # processor.requestCategory()
    # collector()
    # if not myString:
    # for dlo in processor.DLO:
    #     if not processor.getSCInfo(dlo, 'CPID'):
    #         continue
    #     else:
    #     # print(processor.getMemberId(dlo))
    #         print(processor.getSCInfo(dlo, 'SRVC'))
    # processor.transTypeCode()
    dlo = processor.DLO[100]
    print("Date: " + processor.getTransactionDate(dlo))
    print("card: " + processor.getCardNumber(dlo))
    print("rrn: " + processor.getRRN(dlo))
    print("arn: " + processor.getARN(dlo))
    print("auth: " + processor.getAuthCode(dlo))
    print("mcc: " + processor.getMCC(dlo))
    print("req: " + processor.getRequestCategory(dlo))
    print("msg: " + str(processor.getMsgCode(dlo)))
    print("type: " + processor.getTransTypeCode(dlo))
    print("Billing amount: " + processor.getBRInfo(dlo.BILLING, 'Amount'))
    print("MID: " + processor.getMerchantID(dlo))
    print("MNANE: " + processor.getMerchantName(dlo))
    print("contract Number: " + processor.getContractNumber(dlo))
    print("Memberid: " + processor.getMemberId(dlo))
    print("srvc: " + processor.getSCInfo(dlo, 'SRVC'))
    print("cpid: " + processor.getSCInfo(dlo, 'CPID'))