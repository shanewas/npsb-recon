class matching:
    def binSelector(self,panNumber):
        # print(panNumber[0:6])
        if (panNumber[0:6] == "462870" or panNumber[0:6] =="526238"):
            return 1
        else:
            return 0
