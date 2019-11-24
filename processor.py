from helper import *

class processor:
    
    DLO = []
    
    def __init__(self):
        self.help = helper()
        
    def getTransactionDate(self, dlo):
        return dlo.LOCALDT.text

    def getCardNumber(self, dlo):
        return dlo.DESTINATION[0].text

    def getRRN(self, dlo):
        # for dlo in processor.DLO:
        if (dlo.DOCREFSET[-3][0].text == 'RRN'):
            return dlo.DOCREFSET[-3][1].text
            # print(str(dlo.DOCREFSET[-3][0].text) + ": " + str(dlo.DOCREFSET[-3][1].text))
        else:
            return self.help.crawler(dlo.DOCREFSET, 'RRN')

    def getARN(self, dlo):
        # for dlo in processor.DLO:
        if (dlo.DOCREFSET[-2][0].text == 'ARN'):
            return dlo.DOCREFSET[-2][1].text
            # print(str(dlo.DOCREFSET[-2][0].text) + ": " + str(dlo.DOCREFSET[-2][1].text))
        else:
            return self.help.crawler(dlo.DOCREFSET, 'ARN')

    def getAuthCode(self, dlo):
        # for dlo in processor.DLO:
        if (dlo.DOCREFSET[-1][0].text == 'AuthCode'):
            return dlo.DOCREFSET[-1][1].text
            # print(str(dlo.DOCREFSET[-1][0].text) + ": " + str(dlo.DOCREFSET[-1][1].text))
        else:
            return self.help.crawler(dlo.DOCREFSET, 'AuthCode')

    def getMCC(self, dlo):
        return dlo.SOURCEDTLS[0].text

    def getRequestCategory(self, dlo):
        # for dlo in processor.DLO:
        if (dlo.TRANSTYPE[0][1].tag == 'RequestCategory'):
            return dlo.TRANSTYPE[0][1].text
            # print(dlo.TRANSTYPE[0][1].tag + ": " + str(dlo.TRANSTYPE[0][1].text))
        else:
            return self.help.tagFinder(dlo.TRANSTYPE[0], 'RequestCategory')

    def getMsgCode(self, dlo):
        # for dlo in processor.DLO:
        if (dlo.TRANSTYPE[0][0].tag == 'MsgCode'):
            return dlo.TRANSTYPE[0][0].text
            # print('MsgCode: ' + str(dlo.TRANSTYPE[0][0].text))
        else:
            return self.help.tagFinder(dlo.TRANSTYPE[0], 'MsgCode')

    def getTransTypeCode(self, dlo):
        # for dlo in processor.DLO:
        if (dlo.TRANSTYPE[0][-1].tag == 'TransTypeCode'):
            return dlo.TRANSTYPE[0][-1].text
            # print("TransTypeCode: " + str(dlo.TRANSTYPE[0][-1].text))
        else:
            self.help.tagFinder(dlo.TRANSTYPE[0], 'TransTypeCode')

    # getBillingPhaseDate(dlo.BILLING/dlo.RECONCILIATION,
                            #  'PhaseDate/Currency/Amount')
    def getBRInfo(self, token, parm):
        return self.help._Bi_Re(token)[parm]

    def getMerchantName(self, dlo):
        return dlo.SOURCEDTLS[-2].text

    def getMerchantID(self, dlo):
        return dlo.SOURCEDTLS[-1].text

    def getContractNumber(self, dlo):
        return dlo.ORIGINATOR[0].text

    def getMemberId(self, dlo):
        return dlo.ORIGINATOR[1].text

    # processor.getSCInfo(dlo, 'SRVC')/processor.getSCInfo(dlo, 'CPID')
    def getSCInfo(self, dlo, parm):
        return self.help._cpid_srvc(dlo)[parm]