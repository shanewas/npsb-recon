from processor import *
from recon import *
import pandas as pd

class converter:
    def convert(self, dlo, p, recon):
        for each in dlo:
            date = p.getTransactionDate(each)
            card = p.getCardNumber(each)
            rrn = p.getRRN(each)
            arn = p.getARN(each)
            auth = p.getAuthCode(each)
            mcc = int(p.getMCC(each))
            req = p.getRequestCategory(each)
            msg = p.getMsgCode(each)
            type = p.getTransTypeCode(each)
            billing = p.getBRInfo(each.BILLING, 'Amount')
            merid = p.getMerchantID(each)
            mname = p.getMerchantName(each)
            contractnumber = p.getContractNumber(each)
            memberid = p.getMemberId(each)
            srvc = p.getSCInfo(each, 'SRVC')
            cpid = p.getSCInfo(each, 'CPID')

            recon.SETTLEMENT.append(date)
            recon.CARDNUMBER.append(card)
            recon.RRN.append(rrn)
            recon.ARN.append(arn)
            recon.AUTHCODE.append(auth)
            recon.MCC.append(mcc)
            recon.REQUESTCATEGORY.append(req)
            recon.MSGCODE.append(msg)
            recon.TRXNTYPE.append(type)
            recon.AMOUNT.append(billing)
            recon.MERCHANTID.append(merid)
            recon.MERCHANTNAME.append(mname)
            recon.ORIGCONTRACTNUMBER.append(contractnumber)
            recon.ORIGMEMBERID.append(memberid)
            recon.SRVC.append(srvc)
            recon.CPID.append(cpid)

        # Calling DataFrame constructor after zipping
        # both lists, with columns specified
        df = pd.DataFrame(list(zip(
                                    recon.SETTLEMENT,
                                    recon.CARDNUMBER,
                                    recon.RRN,
                                    recon.ARN,
                                    recon.AUTHCODE,
                                    recon.MCC,
                                    recon.REQUESTCATEGORY,
                                    recon.MSGCODE,
                                    recon.TRXNTYPE,
                                    recon.AMOUNT,
                                    recon.MERCHANTID,
                                    recon.MERCHANTNAME,
                                    recon.ORIGCONTRACTNUMBER,
                                    recon.ORIGMEMBERID,
                                    recon.SRVC,
                                    recon.CPID
                                    )),
                                    columns =['DATE_TIME',
                                             'PAN',
                                             'TRANNUMBER',
                                             'ARN',
                                             'APPROVALCODE',
                                             'TERMSIC',
                                             'REQUESTCATEGORY',
                                             'MSGCODE',
                                             'TRANSTYPE',
                                             'BILLING',
                                             'TERMRETAILERNAME',
                                             'MERCHANTNAME',
                                             'TERMNAME',
                                             'MEMBERID',
                                             'SRVC',
                                             'CPID'])
        return df
