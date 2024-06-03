import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
from pypalettes import pypalettes

@pytest.fixture
def mock_palettes_df():
    data = {
        'name': ['palette1', 'palette2'],
        'palette': ["['#000000', '#FFFFFF']", "['#FF0000', '#00FF00', '#0000FF']"],
        'source': ['source1', 'source2']
    }
    df = pd.DataFrame(data)
    return df

@pytest.fixture
def purr_palette_instance(mock_palettes_df):
    with patch('pypalettes.utils.load_csv', return_value=mock_palettes_df):
        instance = pypalettes()
        return instance

def test_get_palette_non_existing(purr_palette_instance):
    with pytest.raises(ValueError):
        purr_palette_instance._get_palette('non_existing_palette')

def test_load_cmap_invalid_type(purr_palette_instance):
    with pytest.raises(ValueError):
        purr_palette_instance.load_cmap(name='palette1', type='invalid_type')