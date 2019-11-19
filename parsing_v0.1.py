import xml.etree.ElementTree as ET
# import threading
from doclist import *
from recon import *
from processor import *

tree = ET.parse('resources/OIC_Documents_245_000245_20191021_38.xml')
root = tree.getroot()

# get [0,1,2 etc of child tag . e.g: Fileheader, DocList, FileTrailer]
FILEHEADER = root[0]
DOCLIST = root[1]
FILETRAILER = root[2]


    # t1.start()
    # # starting thread 2
    # t2.start()
    #
    # # wait until thread 1 is completely executed
    # t1.join()
    # # wait until thread 2 is completely executed
    # t2.join()

if __name__ == '__main__':
    for doc in DOCLIST:
        processor.DLO.append(
            docListBuild(doc[0], doc[1], doc[2], doc[3], doc[4], doc[5], doc[6], doc[7], doc[8], doc[9]))
    # print(processor.getARN(0))
    # processor.authCode(0)
    # processor.requestCategory()
    processor.collector()
    # processor.transTypeCode()
