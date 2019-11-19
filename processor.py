from helper import *

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
