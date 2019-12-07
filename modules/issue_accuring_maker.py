from modules.npsb_read import npsb_read
from modules.recon import recon
from modules.converter import converter

class ia_maker:
    def __init__(self, proc, s_path):
        self.switchread = npsb_read(s_path)
        self.recon = recon()
        dlo = proc.DLO
        self.converter = converter()
        self.swframe = self.switchread.switchFrame
        self.bdframe = self.converter.convert(dlo, proc, self.recon)

        B_PAN = self.bdframe
        B_PAN['IA Status'] = B_PAN['PAN'].str.contains('462870|526238')
        self.B_PAN_issuing = B_PAN[B_PAN['IA Status'] == True]
        self.B_PAN_accuring = B_PAN[B_PAN['IA Status'] == False]

        S_PAN = self.swframe
        S_PAN['IA Status'] = S_PAN['PAN'].str.contains('462870|526238')
        self.S_PAN_issuing = S_PAN[S_PAN['IA Status'] == True]
        self.S_PAN_accuring = S_PAN[S_PAN['IA Status'] == False]
