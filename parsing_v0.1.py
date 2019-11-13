import xml.etree.ElementTree as ET

class docListBuild(object):
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


tree = ET.parse('OIC_Documents_245_000130_20191021_38.xml')
#root DocFile
root = tree.getroot()

#get [0,1,2 etc of child tag . e.g: Fileheader, DocList, FileTrailer]
FILEHEADER = root[0]
DOCLIST = root[1]
FILETRAILER = root[2]

DLO = []

for doc in DOCLIST:
    DLO.append(docListBuild(doc[0], doc[1], doc[2], doc[3], doc[4], doc[5], doc[6], doc[7], doc[8], doc[9]))

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
RNN = 0
ARN = 0
def crawler(dlo, tag):
    for each in dlo.DOCREFSET:
        if each[0].text == tag:
            print(each[0].text + "==" + each[1].text)
            break

def getARN(ARN):
    i = 0
    for dlo in DLO:
        crawler(dlo, 'ARN')
        ARN = ARN + 1
    # print("count with ARN= " + str(ARN))
    return ARN
def getRRN(RNN):
    i = 0
    for dlo in DLO:
        crawler(dlo, 'RRN')
        RNN = RNN + 1
    # print("count with RRN= " + str(RNN))
    return RNN

# print("ARN = " + str(ARN) + " RRN = " + str(RNN))
def transaction():
    i = 0
    total = 0
    for dlo in DLO:
        i = i+1
        total = total + float(dlo.TRANSACTION[1].text)
        # print(dlo.TRANSACTION[1].text)
        print("Total " + str(i) + " transactions and Total ammount is " + str(total))
# transaction()
count = 0
def authCode(count):
    for dlo in DLO:
        crawler(dlo, 'AuthCode')
        count = count +1
    return count

def collector():
    i = 0
    for dlo in DLO:
        i = i+1
        # print("Transaction Date: " + str(dlo.LOCALDT.text))
        # print("Card Number: "+ str(dlo.DESTINATION[0].text))
        # print("MCC " + str(dlo.SOURCEDTLS[0].tag))
        #needs to be filtered out
        if (dlo.TRANSTYPE[0][1].tag == 'RequestCategory'):
            print("Trx_Req_category: " + str(dlo.TRANSTYPE[0][1].tag))
        else:
            for each in dlo.TRANSTYPE[0]:
                if(each.tag == 'RequestCategory'):
                    print("Trx_Req_category: " + str(each.tag))
                    break
    print(i)
collector()

# print(DLO[0].ORIGINATOR[0].tag)
# print(DLO[200].ORIGINATOR[0].text)

# transactionDate()
# print(authCode(count))
# RNN = getRRN(RNN)
# ARN = getARN(ARN)

# Approval Code/ Authorization Code
# DocFile\DocList\Doc\DocRefSet\Parm\ParmCode='AuthCode']\Value


# + " = " + dlo.TRANSACTION[1].text
# total = total + float(dlo.TRANSACTION[1].text)
# ammount = 0
# for dlo in DLO:
#     ammount = ammount + float(dlo.TRANSACTION[1].text)
#     print(ammount)

# print(DLO[2000].DOCREFSET[3][1].tag + "==" + DLO[2000].DOCREFSET[3][1].text)
# print(DLO[1].TRANSACTION[1].text)
# print(DLO[1].DOCREFSET[4][0].text)
# print(DLO[1].DOCREFSET[4][1].text)
# a = DLO[29].DOCREFSET[6][0]
# b = DLO[29].DOCREFSET[6][1]
# print(a.text +" = "+ b.text)




# print(DLO[2000].DOCREFSET[3][0].text)
# print(DLO[2000].TRANSACTION[1].tag)
# print(DLO[2000].TRANSACTION[1].text)
#
# for ob in DLO[2000].TRANSACTION:
#     print (ob.tag +' = '+ ob.text)



# for i in range(100):
#     my_objects.append(MyClass(i))

# # later

# for obj in my_objects:
#     print obj.number