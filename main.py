import os

from tables_generator import tables_generator
from data_formatter import create_dictionary, create_csv


class Pdf:

    def __init__(self):
        self._pdf_file = None
        self._tables = None
        self._table_title = None
        self._dataframe = None
        self._dictionary = None
        self._csv = None

    def set_pdf_file(self, pdf_file):
        """
        Setter method for pdf parsing
        Pass pdf_file path
        """
        try:
            self._pdf_file = os.path.abspath(pdf_file)
            self._tables, self._table_title = tables_generator(self._pdf_file)
        except Exception as e:
            print(str(e))

    def get_pdf_file(self):
        """
        Getter method for pdf_file path
        """
        try:
            return self._pdf_file
        except Exception as e:
            print(str(e))

    def get_dataframe(self, i=None):
        """
        Get dataframe by table number
        """
        try:
            if i is None:
                return "Allocate index."
            elif 0 < i <= len(self._tables):
                self._dataframe = self._tables[i]
                return self._dataframe
            else:
                return "Table doesn't exist."
        except Exception as e:
            print(str(e))

    def get_dictionary(self, i=None):
        """
        Get dictionary by table number
        """
        try:
            if i is None:
                return "Allocate index."
            elif 0 < i <= len(self._tables):
                self._dataframe = self._tables[i]
                self._dictionary = create_dictionary(self._dataframe)
                return self._dictionary
            else:
                return "Table doesn't exist."
        except Exception as e:
            print(str(e))

    def get_csv(self, i=None):
        """
        Download Csv file
        """
        try:
            if i is None:
                os.mkdir(self._table_title)
                for j in range(len(self._tables)):
                    create_csv(self._tables[j+1], self._table_title, j+1)
            elif 0 < i <= len(self._tables):
                os.mkdir(self._table_title)
                self._dataframe = self._tables[i]
                self._csv = create_csv(self._dataframe, self._table_title, i)
                return self._csv
            else:
                return "Table doesn't exist."
        except Exception as e:
            print(str(e))
