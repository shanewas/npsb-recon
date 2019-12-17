
# import O365
# from O365 import Account

# credentials = (o365credid, o365credpwd)
# account = Account(credentials)

# def send_email(account, to, subject, start, body, end):
#     m = account.new_message()
#     m.to.add(to)
#     m.subject = subject
#     m.body = start + body + end
#     m.send()

import pandas as pd
from pretty_html_table import build_table
df = pd.read_excel('resources/ATM_Difference.xlsx')

df.to_json(r'resources/ATM_.json',orient='table')
html_table = build_table(df, 'green_dark')

Html_file= open("resources/blue.html","w")
Html_file.write(html_table)
Html_file.close()