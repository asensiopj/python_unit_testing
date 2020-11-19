import pytest
import pandas as pd
import sys
sys.path.append("/home/peter/Documents/02_bigdata/01_data_engineerng_datacamp/python_unit_testing/src/")
from data.cargar_datos import remove_nan


class TestRemoveNan(object):
    def test_remove_nan(self):
        """
        Fail if provided value is not NaN
        """
        message = "Actual return value"
        df = pd.read_csv("src/data/googleplaystore.csv", sep=",") # go up one level beccause of we are in test file global
        remove_nan(df, 'Rating')

        assert df['Rating'].isnull().values.any() == pytest.approx(0), message