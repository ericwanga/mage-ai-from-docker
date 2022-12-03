from pandas import DataFrame
import math

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# get columns
def select_number_columns(df: DataFrame) -> DataFrame:
    # return df[['Age', 'Fare', 'Parch', 'Pclass', 'SibSp', 'Survived']]
    return df[df.columns.values]

# fill missing values
def fill_missing_values_with_median(df: DataFrame) -> DataFrame:
    for col in df.columns:
        values = sorted(df[col].dropna().tolist())
        median_ = values[math.floor(len(values) / 2)]
        df[[col]] = df[[col]].fillna(median_)
    return df

# function to change all str columns to UPPER CASE
def to_upper(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    filter out columns with dtypes == object, then Upper case them
    """
    filter_obj = df.dtypes[df.dtypes == object].index.to_list()
    df[filter_obj] = df[filter_obj].apply(lambda x: x.astype(str).str.upper())

    return df

@transformer
def transform_df(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        df (DataFrame): Data frame from parent block.

    Returns:
        DataFrame: Transformed data frame
    """
    # Specify your transformation logic here
    df = to_upper(df)

    return fill_missing_values_with_median(select_number_columns(df))




@test
def test_output(df) -> None:
    """
    Template code for testing the output of the block.
    """
    assert df is not None, 'The output is undefined'
