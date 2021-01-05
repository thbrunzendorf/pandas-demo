import pandas as pd

def print_column_statistics(df,column,max_frequent_values=5,excluded_columns=()):
    print('--------------------')
    print('column',column)
    print('--------------------')
    print('statistics')
    print(df[column].describe(),end='\n\n')
    print('most frequent values - max',max_frequent_values)
    if df[column].name in excluded_columns:
        print('n/a')
    else:
        print(df[column].value_counts()[:max_frequent_values])

def print_file_statistics(df,filter_column='',filter_value=''):
    if filter_column != '':
        print('filtered by',filter_column,'=',filter_value)
    print('value count per column excluding n/a values')
    print(df.count(),end='\n\n')

def read_from_file(filename):
    df = pd.read_csv(filename,sep=';',low_memory=False,na_values='(null)')
    # converts to dtypes supporting pd.NA and avoids key errors with floats
    return df.convert_dtypes()

def print_file_header(filename):
    print('\n\n')
    print('====================')
    print('file',filename)
    print('====================')
    print('\n\n')

def main():
    filenames = ('demo.csv',)
    excluded_columns = ('ID','AMOUNT')
    filter_column = 'CATEGORY'
    filter_values = ('MUSIC','VIDEO')
    for filename in filenames:
        print_file_header(filename)
        df = read_from_file(filename)
        print_file_statistics(df)
        for column in df:
            print_column_statistics(df,column,max_frequent_values=2,excluded_columns=excluded_columns)
        for filter_value in filter_values:
            print_file_header(filename)
            filtered_df = df.loc[df[filter_column] == filter_value]
            print_file_statistics(filtered_df,filter_column,filter_value)
            for column in filtered_df:
                print_column_statistics(filtered_df,column,max_frequent_values=2,excluded_columns=excluded_columns)

main()
