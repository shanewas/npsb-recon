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

        # for dlo in DLO:
        #     if dlo.DOCREFSET[3][0].text == "RRN":
        #         i = i + 1
        #         print(dlo.DOCREFSET[3][0].text + "==" + dlo.DOCREFSET[3][1].text)
        #     else:
        #         # print(dlo.DOCREFSET[-2][0].text + "==" + dlo.DOCREFSET[-2][1].text)
        #         break
        # print("count with RRN= " + str(i))
        ###################### testing code ######################
        # def getRRN():
        #     i = 0
        #     J = 0
        #     K = 0
        #     for dlo in DLO:
        #         if dlo.DOCREFSET[3][0].text == "RRN":
        #             J = J+1
        #             print(dlo.DOCREFSET[3][0].text + "==" + dlo.DOCREFSET[3][1].text)
        #         else:
        #             K = K+1
        #             for each in dlo.DOCREFSET:
        #                 if each[0].text == 'RRN':
        #                     print(each[0].text + "==" + each[1].text)
        #         i = i + 1
        #     print("count with RRN= " + str(i) +'************'+ str(J) +'**********'+ str(K))