import pandas as pd
from datetime import datetime
from argparse import ArgumentParser
# Reading csv file
# take data from argparse
parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="file", help="file to read", metavar="FILE")
parser.add_argument("-o", "--output", dest="output", help="output file", metavar="FILE")
parser.add_argument("-c", "--column", dest="column", help="column to convert", metavar="COLUMN")

args = parser.parse_args()
# reading the args
file = args.file
output = args.output
column = args.column

ArgumentParser()
if column:
    df = pd.read_csv(file)
else:
    df = pd.read_csv(file,names=['date','time','','x'])
    column='date'
# df.columns
from dateutil import parser
df[column]=df[column].apply(lambda x: parser.parse(str(x)))
# df[column] = pd.to_datetime(df[column], format='%d-%m-%Y')
# df.head()
df.loc[df[column].dt.year > 2000, 'date'] -= pd.DateOffset(years=100)
# changing the format of date
format = '%m-%d-%Y'
df[column] = df[column].dt.strftime(format)

# for index,row in df.iterrows():

#     try:
#         row['date'] = datetime.strftime(row['date'],format='%d-%m-%y')
#         # pd.to_datetime(row['date'], format='%d-%m-%y')
#     except:
#         row['date'] = datetime.strptime(row['date'],format='%d-%m-%Y')
        # row['date'] = pd.to_datetime(row['date'], format='%d-%m-%Y')
    
    # row['date']=row['date'].year if row['date'].year < 2020 else row['date'].year-100

    # df.loc[index,'date'] = row['date']
    # print(type(row['date']))
    # row.loc[row['date'].dt.year >= 2020, 'date'] -= pd.DateOffset(years=100)

    # df[column]=df[column].apply(lambda x: str(x).replace('-', '/'))

    # df.loc[index,'date'] = df.loc[index,'date'].strftime('%d/%m/%Y')

# df[column] = pd.to_datetime(df[column], format='%d/%m/%yy')


# df[column] = pd.to_datetime(df[column], format='%d/%m/%yy')


# export to csv
df.to_csv(output, index=False)