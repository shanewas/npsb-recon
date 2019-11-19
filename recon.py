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
