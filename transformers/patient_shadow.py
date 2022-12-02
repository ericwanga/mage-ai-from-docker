from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def execute_transformer_action(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Execute Transformer Action: ActionType.AVERAGE

    Docs: https://github.com/mage-ai/mage-ai/blob/master/docs/actions/transformer_actions/README.md#aggregation-actions
    """
    action = build_transformer_action(
        df,
        action_type=ActionType.AVERAGE,
        action_code='',  # Enter filtering condition on rows before aggregation
        arguments=[],  # Enter the columns to compute aggregate over
        axis=Axis.COLUMN,
        options={'groupby_columns': []},  # Enter columns to group by
        outputs=[
            # The number of outputs below must match the number of arguments
            {'uuid': 'new_aggregate_column', 'column_type': 'number_with_decimals'},
        ],
    )

    return BaseAction(action).execute(df)


@test
def test_output(df, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert df is not None, 'The output is undefined'
