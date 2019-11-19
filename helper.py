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
