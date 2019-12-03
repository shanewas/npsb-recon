from parse import parsing
if __name__ == '__main__':
    switch_report = (r'resources/NPSB_ISS_ACQ_TRX_export_20_OCT_2019.xlsx')
    p1 = parsing('resources/OIC_Documents_245_000130_20191021_38.xml',
                    'resources/OIC_Documents_245_000245_20191021_38.xml', switch_report)
    ba = p1.defination_match(p1.ia_maker.S_PAN_issuing)
    atm = p1.slicing(ba.atm.count)
    # pos = p1.slicing(ba.pos.count)
    # ib = p1.slicing(ba.ib.count)
    print(atm)
    # a = pd.concat([bi,si],axis=1)
    # a = atm[atm['TRANNUMBER'] == 102010395491]
    # b = type(si[atm?['TRANNUMBER'] == 102010395491]['AMOUNT'][849])
    # if (a == b):
    # print(a)
    # print(bi[bi['PAN'] == '462870******4021'])
    # print(si[si['PAN'] == '462870******4021'])

    # atm_writer = pd.ExcelWriter('resources/atm.xlsx', engine='xlsxwriter')
    # atm_writer2 = pd.ExcelWriter('resources/atm_acc.xlsx', engine='xlsxwriter')
    # # pos_writer = pd.ExcelWriter('resources/pos.xlsx', engine='xlsxwriter')
    # # ib_writer = pd.ExcelWriter('resources/ib.xlsx', engine='xlsxwriter')
    #
    # saccu.to_excel(atm_writer2, sheet_name='filtered')
    # satm.to_excel(atm_writer, sheet_name='filtered')

    # atm_writer.save()
    # atm_writer2.save()
    print('-----------------------')