import pandas as pd

class writer:
    def __init__(self, path):
        self.name = path.split('/')[-1].split('.')[0]
        self.path = path
        self.writer = object

    def open(self):
        try:
            self.writer = pd.ExcelWriter(self.path, engine='xlsxwriter')
        except:
            raise
    def write(self, data):
        for each in data:
            try:
                data[each].to_excel(self.writer, sheet_name=each)
            except IOError:
                print('Cant write xlsx file' + IOError)
                continue
    
    def close(self):
        self.writer.save()
        print("Successfully wrote " + self.name + " sheet")