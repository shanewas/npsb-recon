from helper import *

class processor:

    DLO = []

    RNN = 0
    ARN = 0
    count = 0

    def getTransactionDate(dlo):
        return dlo.LOCALDT.text

    def getCardNumber(dlo):
        return dlo.DESTINATION[0].text

    def getRRN(dlo):
        # for dlo in processor.DLO:
        if (dlo.DOCREFSET[-3][0].text == 'RRN'):
            return dlo.DOCREFSET[-3][1].text
            # print(str(dlo.DOCREFSET[-3][0].text) + ": " + str(dlo.DOCREFSET[-3][1].text))
        else:
            return helper.crawler(dlo.DOCREFSET, 'RRN')

    def getARN(dlo):
        # for dlo in processor.DLO:
        if (dlo.DOCREFSET[-2][0].text == 'ARN'):
            return dlo.DOCREFSET[-2][1].text
            # print(str(dlo.DOCREFSET[-2][0].text) + ": " + str(dlo.DOCREFSET[-2][1].text))
        else:
            return helper.crawler(dlo.DOCREFSET, 'ARN')

    def getAuthCode(dlo):
        # for dlo in processor.DLO:
        if (dlo.DOCREFSET[-1][0].text == 'AuthCode'):
            return dlo.DOCREFSET[-1][1].text
            # print(str(dlo.DOCREFSET[-1][0].text) + ": " + str(dlo.DOCREFSET[-1][1].text))
        else:
            return helper.crawler(dlo.DOCREFSET, 'AuthCode')

    def getMCC(dlo):
        return dlo.SOURCEDTLS[0].text

    def getRequestCategory(dlo):
        # for dlo in processor.DLO:
        if (dlo.TRANSTYPE[0][1].tag == 'RequestCategory'):
            return dlo.TRANSTYPE[0][1].text
            # print(dlo.TRANSTYPE[0][1].tag + ": " + str(dlo.TRANSTYPE[0][1].text))
        else:
            return helper.tagFinder(dlo.TRANSTYPE[0], 'RequestCategory')

    def getMsgCode(dlo):
        # for dlo in processor.DLO:
        if (dlo.TRANSTYPE[0][0].tag == 'MsgCode'):
            return dlo.TRANSTYPE[0][0].text
            # print('MsgCode: ' + str(dlo.TRANSTYPE[0][0].text))
        else:
            return helper.tagFinder(dlo.TRANSTYPE[0], 'MsgCode')

    def getTransTypeCode(dlo):
        # for dlo in processor.DLO:
        if (dlo.TRANSTYPE[0][-1].tag == 'TransTypeCode'):
            return dlo.TRANSTYPE[0][-1].text
            # print("TransTypeCode: " + str(dlo.TRANSTYPE[0][-1].text))
        else:
            helper.tagFinder(dlo.TRANSTYPE[0], 'TransTypeCode')

    # getBillingPhaseDate(dlo.BILLING/dlo.RECONCILIATION,
                            #  'PhaseDate/Currency/Amount')
    def getBRInfo(token, parm):
        return processor._Bi_Re(token)[parm]

    def getMerchantName(dlo):
        return dlo.SOURCEDTLS[-2].text

    def getMerchantID(dlo):
        return dlo.SOURCEDTLS[-1].text

    def getContractNumber(dlo):
        return dlo.ORIGINATOR[0].text

    def getMemberId(dlo):
        return dlo.ORIGINATOR[1].text

    def _Bi_Re(Object):
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

    # processor.getSCInfo(dlo, 'SRVC')/processor.getSCInfo(dlo, 'CPID')
    def getSCInfo(dlo, parm):
        return processor._cpid_srvc(dlo)[parm]

    def _cpid_srvc(dlo):
        dic = {'SRVC': '', 'CPID': ''}
        for each in dlo.TRANSACTION[2][1]:
            if (each[0].text == 'SRVC'):
                dic['SRVC'] = each[1].text
            if (each[0].text == 'CPID'):
                dic['CPID'] = each[1].text
        return dic
