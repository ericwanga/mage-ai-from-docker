import io
import pandas as pd
import requests
from pandas import DataFrame
import mysql.connector
from mysql.connector import errorcode


# configuration
db_name = 'world'
table_name = 'city'
user = 'ewang'
password = 'UniSA!1234'
host = '127.0.0.1'

# assemble
conn_config = {
    'user': user,
    'password': password,
    'host': host,
    'database': db_name,
    'raise_on_warnings': True
}

query = '''
select * from {}.{}
'''.format(db_name, table_name)


if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


# @data_loader
# def load_data_from_api(**kwargs) -> DataFrame:
#     """
#     Template for loading data from API
#     """
#     url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'

#     response = requests.get(url)
#     return pd.read_csv(io.StringIO(response.text), sep=',')

def query_mysql(config, query, table_name):

    try:
        cnx = mysql.connector.connect(**config)
        # if cnx.is_connected():

            # verify connection with db
        db_info = cnx.get_server_info()
        print("Connected to MySQL Server version", db_info)

        cursor = cnx.cursor()

        # get columns
        cursor.execute(f'DESCRIBE {table_name}')
        record = cursor.fetchall()
        columns = [r[0] for r in record]
        # print('Columns: ', columns)

        # get rows
        cursor.execute(query)
        rows = cursor.fetchall()

        # assemble dataframe
        df = pd.DataFrame(rows, columns=columns)

        cursor.close()
        cnx.close()
        # print("MySQL connection is closed")

        # return db_info, cursor.fetchall()
        return df

    except mysql.connector.Error as err:
        print("Error: {}".format(err))


@data_loader
def load_data(**kwargs) -> DataFrame:
    # return query_table('city', query)
    return query_mysql(conn_config, query, table_name)

# print(df.shape)


@test
def test_output(df) -> None:
    """
    Template code for testing the output of the block.
    """
    assert df is not None, 'The output is undefined'
