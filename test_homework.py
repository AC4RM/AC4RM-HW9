from homework import *
from pathlib import Path
import urllib.request
import sqlite3
import pandas as pd
import sklearn
import re
import numpy as np
import pytest


def test_python():
    account = BankAccount('Test', 2000)
    account.deposit(500)

    assert account.check_balance() == "Your current balance is 2500"
    with pytest.raises(ValueError, match="You don't have enough money!"):
        account.withdraw(3000)


def test_sql():
    urllib.request.urlretrieve('https://github.com/AC4RM/AC4RM-dataset/blob/main/sql/data.db?raw=true', 'data.db')

    con = sqlite3.connect('data.db')

    employee_df = pd.read_sql_query(sql_query_1, con)
    customer_df = pd.read_sql_query(sql_query_2, con)

    assert employee_df.shape == (11, 3)
    assert 'Guthrey' in employee_df['first_name'].values
    assert customer_df.shape == (3, 3)
    assert 'Thacher' in customer_df['first_name'].values

    Path('data.db').unlink(missing_ok=True)


def test_model():
    np.random.seed(42)
    model, predictions = train_model()

    assert isinstance(model, sklearn.ensemble._forest.RandomForestClassifier)
    assert sum(predictions) == 83


def test_regex():
    test_string = """
    This is a test string. This string might contain numbers like 2, 2, 2, etc.
    """
    result_1 = word_count(test_string)
    result_2 = word_count(test_string, number=True)

    assert result_1.most_common(2) == [('this', 2), ('string', 2)]
    assert result_2.most_common(2) == [('2', 3), ('this', 2)]

