def create_dictionary(dataframe):
    """
    Create dictionary row-wise from dataframe
    """
    dictionary_by_row_index = dataframe.to_dict('index')
    return dictionary_by_row_index


def create_csv(dataframe, table_title, i):
    """
    Convert dataframe to csv
    """
    dataframe.to_csv(f'{table_title}_{i}.csv')
    return f'Downloaded to {table_title}_{i}.csv'
