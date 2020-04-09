import pyodbc


class DatabaseUtility():

    def __init__(self):
        self.connection = None
        self.cursor = None


    def _open_connection(self):
        '''
        Establish a connection to database. Not to be accessed outside of this class.
        '''
        self.connection = pyodbc.connect("Driver={SQL Server};"
                                         "Server=BDC8-LX-G01ERDV;"
                                         "Database=guidewire;"
                                         "Trusted_Connection=yes;")

    def execute_statement(self):
        '''
        Executes a statement by establishing the connection to database
        '''
        try:
            self._open_connection()
            self.cursor = self.connection.cursor()
            self.cursor.execute('Select * from Tests')
            for row in self.cursor:
                print(row)
        except Exception as e:
            raise e
        finally:
            if self.cursor is not None: self.cursor.close()
            if self.connection is not None: self.connection.close()