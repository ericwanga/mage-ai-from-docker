from mage_ai.io.file import FileIO
from pandas import DataFrame

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


# @data_exporter
# def export_data_to_file(df: DataFrame, **kwargs) -> None:
#     """
#     Template for exporting data to filesystem.

#     Docs: https://github.com/mage-ai/mage-ai/blob/master/docs/blocks/data_loading.md#fileio
#     """
#     filepath = 'titanic_clean.csv'
#     FileIO().export(df, filepath)


@data_exporter
def export_data_to_file(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to filesystem.

    Docs: https://github.com/mage-ai/mage-ai/blob/master/docs/blocks/data_loading.md#fileio
    """
    filepath = 'export/df_clean.csv'
    FileIO().export(df, filepath, index=False)


# @data_exporter
# def export_data_to_snowfalke(df: DataFrame, **kwargs) -> None:
import snowflake.connector
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine

engine = create_engine(URL(
    account = 'iq04688.ap-southeast-2',
    user = 'wanzy120',
    password = 'UniSA!1234',
    database = 'DEFAULT_DB',
    schema = 'STAGING',
    warehouse = 'COMPUTE_WH',
    role = 'ACCOUNTADMIN',
))

connection = engine.connect()

df.to_sql('mage_table', con=engine, index=False)

connection.close()
engine.displose()
