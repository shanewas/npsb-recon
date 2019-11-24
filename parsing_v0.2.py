# class recon:
#     def __init__(self, id, settlementDate, transactionDate, cardNumber, RRN, ARN, authCode, MCC, RequestCategory,
#                  msgCode, trxnType, amount, currency, merchantName, merchantID, OrigContractNumber, OrigMemberID,
#                  SRVC, CPID, phaseDate, reconCurrency, reconAmount):
#         self.ID = id
#         self.SETTLEMENT = settlementDate
#         self.TRANSACTIONDATE = transactionDate
#         self.CARDNUMBER = cardNumber
#         self.RRN = RRN
#         self.ARN = ARN
#         self.AUTHCODE = authCode
#         self.MCC = MCC
#         self.REQUESTCATEGORY = RequestCategory
#         self.MSGCODE = msgCode
#         self.TRXNTYPE = trxnType
#         self.AMOUNT = amount
#         self.CURRENCY = currency
#         self.MERCHANTNAME = merchantName
#         self.MERCHANTID = merchantID
#         self.ORIGCONTRACTNUMBER = OrigContractNumber
#         self.ORIGMEMBERID = OrigMemberID
#         self.SRVC = SRVC
#         self.CPID = CPID
#         self.PHASEDATE = phaseDate
#         self.RECONCURRENCY = reconCurrency
#         self.RECONAMOUNT = reconAmount
#
#         # for dlo in DLO:
#         #     if dlo.DOCREFSET[3][0].text == "RRN":
#         #         i = i + 1
#         #         print(dlo.DOCREFSET[3][0].text + "==" + dlo.DOCREFSET[3][1].text)
#         #     else:
#         #         # print(dlo.DOCREFSET[-2][0].text + "==" + dlo.DOCREFSET[-2][1].text)
#         #         break
#         # print("count with RRN= " + str(i))
#         ###################### testing code ######################
#         # def getRRN():
#         #     i = 0
#         #     J = 0
#         #     K = 0
#         #     for dlo in DLO:
#         #         if dlo.DOCREFSET[3][0].text == "RRN":
#         #             J = J+1
#         #             print(dlo.DOCREFSET[3][0].text + "==" + dlo.DOCREFSET[3][1].text)
#         #         else:
#         #             K = K+1
#         #             for each in dlo.DOCREFSET:
#         #                 if each[0].text == 'RRN':
#         #                     print(each[0].text + "==" + each[1].text)
#         #         i = i + 1
#         #     print("count with RRN= " + str(i) +'************'+ str(J) +'**********'+ str(K))

import xml.etree.ElementTree as ET
# import threading
from doclist import *
# from recon import *
from processor import *

tree = ET.parse('resources/OIC_Documents_245_000245_20191021_38.xml')
root = tree.getroot()

# get [0,1,2 etc of child tag . e.g: Fileheader, DocList, FileTrailer]
FILEHEADER = root[0]
DOCLIST = root[1]
FILETRAILER = root[2]


def collector():
    i = 0
    # j = 0
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
            # MerchantName
            print(str(dlo.SOURCEDTLS[-2].tag) + ": " + str(dlo.SOURCEDTLS[-2].text))
            # MerchantID
            print(str(dlo.SOURCEDTLS[-1].tag) + ": " + str(dlo.SOURCEDTLS[-1].text))
            # ContractNumber
            print(str(dlo.ORIGINATOR[0].tag) + ': ' + str(dlo.ORIGINATOR[0].text))
            # MemberId
            print(str(dlo.ORIGINATOR[1].tag) + ': ' + str(dlo.ORIGINATOR[1].text))
            # print("SRVC: " + str(processor._cpid_srvc(dlo)['SRVC']))
            # print("CPID: " + str(processor._cpid_srvc(dlo)['CPID']))
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
    collector()
    # for dlo in processor.DLO:
    #     # if processor.getTransTypeCode(dlo) == None:
    #     #     continue
    #     # else:
    #     print(processor.getMerchantID(dlo))
        # print(processor.getPhaseDate(dlo.BILLING, 'Amount'))
    # processor.transTypeCode()
