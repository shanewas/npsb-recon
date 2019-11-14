import xml.etree.ElementTree as ET
import threading


class docListBuild:
    def __init__(self, tramstype, docrefset, localdt, newdt, sourcedtls, originator, destination, transaction, billing, reconciliaion):
        self.TRANSTYPE = tramstype
        self.DOCREFSET = docrefset
        self.LOCALDT = localdt
        self.NWDT = newdt
        self.SOURCEDTLS = sourcedtls
        self.ORIGINATOR = originator
        self.DESTINATION = destination
        self.TRANSACTION = transaction
        self.BILLING = billing
        self.RECONCILIATION = reconciliaion


# class potato:
#     def __init__(self, y):
#         self.x = 0
#         self.y = y
#
# x = potato(5)
#
# print(x.y)
class recon:
    def __init__(self, id, settlementDate, transactionDate, cardNumber, RRN, ARN, authCode, MCC, RequestCategory,
                 msgCode, trxnType, amount, currency, merchantName, merchantID, OrigContractNumber, OrigMemberID,
                 SRVC, CPID, phaseDate, reconCurrency, reconAmount):
        self.ID = id
        self.SETTLEMENT = settlementDate
        self.TRANSACTIONDATE = transactionDate
        self.CARDNUMBER = cardNumber
        self.RRN = RRN
        self.ARN = ARN
        self.AUTHCODE = authCode
        self.MCC = MCC
        self.REQUESTCATEGORY = RequestCategory
        self.MSGCODE = msgCode
        self.TRXNTYPE = trxnType
        self.AMOUNT = amount
        self.CURRENCY = currency
        self.MERCHANTNAME = merchantName
        self.MERCHANTID = merchantID
        self.ORIGCONTRACTNUMBER = OrigContractNumber
        self.ORIGMEMBERID = OrigMemberID
        self.SRVC = SRVC
        self.CPID = CPID
        self.PHASEDATE = phaseDate
        self.RECONCURRENCY = reconCurrency
        self.RECONAMOUNT = reconAmount

# x = recon()
#
# print (x.CPID)

tree = ET.parse('OIC_Documents_245_000245_20191021_38.xml')
root = tree.getroot()

# get [0,1,2 etc of child tag . e.g: Fileheader, DocList, FileTrailer]
FILEHEADER = root[0]
DOCLIST = root[1]
FILETRAILER = root[2]

class helper:
    def tagFinder(dlo_ite, token):
        for each in dlo_ite:
            if (each.tag == token):
                return each.text
                # print(token + ': ' + str(each.text))
                # break

    def crawler(Object, tag):
        for each in Object:
            if each[0].text == tag:
                return each[1].text
                # print(each[0].text + ": " + each[1].text)
                # break

class processor:

    DLO = []

    RNN = 0
    ARN = 0
    count = 0



    def getARN(dlo):
        # for dlo in processor.DLO:
        if (dlo.DOCREFSET[-2][0].text == 'ARN'):
            return dlo.DOCREFSET[-2][1].text
            # print(str(dlo.DOCREFSET[-2][0].text) + ": " + str(dlo.DOCREFSET[-2][1].text))
        else:
            return helper.crawler(dlo.DOCREFSET, 'ARN')

    def getRRN(dlo):
        # for dlo in processor.DLO:
        if (dlo.DOCREFSET[-3][0].text == 'RRN'):
            return dlo.DOCREFSET[-3][1].text
            # print(str(dlo.DOCREFSET[-3][0].text) + ": " + str(dlo.DOCREFSET[-3][1].text))
        else:
            return helper.crawler(dlo.DOCREFSET, 'RRN')

    # def transaction():
    #     i = 0
    #     total = 0
    #     for dlo in processor.DLO:
    #         i = i + 1
    #         total = total + float(dlo.TRANSACTION[1].text)
    #         print("Total " + str(i) + " transactions and Total ammount is " + str(total))

    def authCode(dlo):
        # for dlo in processor.DLO:
        if (dlo.DOCREFSET[-1][0].text == 'AuthCode'):
            return dlo.DOCREFSET[-1][1].text
            # print(str(dlo.DOCREFSET[-1][0].text) + ": " + str(dlo.DOCREFSET[-1][1].text))
        else:
            return helper.crawler(dlo.DOCREFSET, 'AuthCode')

    def requestCategory(dlo):
        # for dlo in processor.DLO:
        if (dlo.TRANSTYPE[0][1].tag == 'RequestCategory'):
            return dlo.TRANSTYPE[0][1].text
            # print(dlo.TRANSTYPE[0][1].tag + ": " + str(dlo.TRANSTYPE[0][1].text))
        else:
            return helper.tagFinder(dlo.TRANSTYPE[0], 'RequestCategory')

    def msgCode(dlo):
        # for dlo in processor.DLO:
        if (dlo.TRANSTYPE[0][0].tag == 'MsgCode'):
            return dlo.TRANSTYPE[0][0].text
            # print('MsgCode: ' + str(dlo.TRANSTYPE[0][0].text))
        else:
            return helper.tagFinder(dlo.TRANSTYPE[0], 'MsgCode')

    def transTypeCode(dlo):
        # for dlo in processor.DLO:
        if (dlo.TRANSTYPE[0][-1].tag == 'TransTypeCode'):
            return dlo.TRANSTYPE[0][-1].text
            # print("TransTypeCode: " + str(dlo.TRANSTYPE[0][-1].text))
        else:
            helper.tagFinder(dlo.TRANSTYPE[0], 'TransTypeCode')

    def _Bi_Re(dlo, Object):
        dic = {'PhaseDate': '', 'Currency': '', 'Amount': ''}
        for each in Object:
            if each.tag == 'PhaseDate':
                dic['PhaseDate'] = each.text
            elif each.tag == 'Currency':
                dic['Currency'] = each.text
            elif each.tag == 'Amount':
                dic['Amount'] = each.text
            else:
                continue
        return dic

    def _cpid_srvc(dlo):
        dic = {'SRVC': '', 'CPID': ''}
        for each in dlo.TRANSACTION[2][1]:
            if (each[0].text == 'SRVC'):
                dic['SRVC'] = each[1].text
            if (each[0].text == 'CPID'):
                dic['CPID'] = each[1].text
        return dic

    # t1 = threading.Thread(target=msgCode())
    # t2 = threading.Thread(target=requestCategory())
    # t3 = threading.Thread(target=transTypeCode())
    def collector():
        i = 0
        J = 0
        for dlo in processor.DLO:
            i = i + 1
            print("Transaction Date: " + str(dlo.LOCALDT.text))
            print("Card Number: "+ str(dlo.DESTINATION[0].text))
            print("RRN: " + str(processor.getRRN(dlo)))
            print("ARN: " + str(processor.getARN(dlo)))
            processor.authCode(dlo)
            print("MCC: " + str(dlo.SOURCEDTLS[0].text))
            print("Request Category: " + str(processor.requestCategory(dlo)))
            print("Msg Code: " + str(processor.msgCode(dlo)))
            print("Transaction Type: " + str(processor.transTypeCode(dlo)))
            print("BILLING PhaseDate: "+ str(processor._Bi_Re(dlo, dlo.BILLING)['PhaseDate']))
            print("BILLING Currency: "+ str(processor._Bi_Re(dlo, dlo.BILLING)['Currency']))
            print("BILLING Amount: " + str(processor._Bi_Re(dlo, dlo.BILLING)['Amount']))
            # MerchantName
            print(str(dlo.SOURCEDTLS[-2].tag) + ": " + str(dlo.SOURCEDTLS[-2].text))
            # MerchantID
            print(str(dlo.SOURCEDTLS[-1].tag) + ": " + str(dlo.SOURCEDTLS[-1].text))
            # ContractNumber
            print(str(dlo.ORIGINATOR[0].tag) + ': ' + str(dlo.ORIGINATOR[0].text))
            # MemberId
            print(str(dlo.ORIGINATOR[1].tag) + ': ' + str(dlo.ORIGINATOR[1].text))
            print("SRVC: " + str(processor._cpid_srvc(dlo)['SRVC']))
            print("CPID: " + str(processor._cpid_srvc(dlo)['CPID']))
            print("Recon PhaseDate: "+ str(processor._Bi_Re(dlo, dlo.RECONCILIATION)['PhaseDate']))
            print("Recon Currency: "+ str(processor._Bi_Re(dlo, dlo.RECONCILIATION)['Currency']))
            print("Recon Amount: " + str(processor._Bi_Re(dlo, dlo.RECONCILIATION)['Amount']))
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
    processor.collector()
    # processor.transTypeCode()