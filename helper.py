from decimal import Decimal
class helper:
    def tagFinder(self, dlo_ite, token):
        for each in dlo_ite:
            if (each.tag == token):
                return each.text
                # print(token + ': ' + str(each.text))
                # break

    def crawler(self, Object, tag):
        for each in Object:
            if each[0].text == tag:
                return each[1].text
                # print(each[0].text + ": " + each[1].text)
                # break

    def _Bi_Re(self, Object):
        dic = {'PhaseDate': '', 'Currency': '', 'Amount': ''}
        for each in Object:
            if each.tag == 'PhaseDate':
                dic['PhaseDate'] = each.text
            elif each.tag == 'Currency':
                dic['Currency'] = each.text
            elif each.tag == 'Amount':
                dic['Amount'] = Decimal(each.text)
            else:
                continue
        return dic

    def _cpid_srvc(self, dlo):
        dic = {'SRVC': '', 'CPID': ''}
        for each in dlo.TRANSACTION[2][1]:
            if (each[0].text == 'SRVC'):
                dic['SRVC'] = each[1].text
            if (each[0].text == 'CPID'):
                dic['CPID'] = each[1].text
        return dic
