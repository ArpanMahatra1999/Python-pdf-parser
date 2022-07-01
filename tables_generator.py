import pandas as pd
import camelot


def create_dataframe(table):
    """
    Delete empty rows
    """
    dataframe = table.df

    # Drop first row
    dataframe.columns = dataframe.iloc[0]
    dataframe = dataframe.reindex(dataframe.index.drop(0)).reset_index(drop=True)
    dataframe.columns.name = None

    # Drop empty rows with the help of later deleted column k/a empty
    empty_list = [all([dataframe.loc[i, col] == "" for col in dataframe.columns]) for i in range(len(dataframe.index))]
    dataframe['empty'] = pd.Series(empty_list, index=range(len(dataframe.index)))
    dataframe = dataframe[dataframe['empty'] == False]
    dataframe.drop('empty', inplace=True, axis=1)

    return dataframe


def tables_generator(pdf_name):
    """
    Convert pdf to tables with non-empty rows
    """
    # Convert pdf to tables
    tables = camelot.read_pdf(pdf_name)
    table_title = pdf_name.split(".pdf")[-2].strip()

    dataframes = {}

    for i in range(tables.n):
        # Create dataframe without empty rows from each table
        dataframe = create_dataframe(tables[i])
        dataframes[i+1] = dataframe
    return dataframes, table_title

