import pytest
import wbgapi as wb
import pandas as pd

def test_world_bank_connection():
    """Test if we can connect to World Bank API"""
    try:
        # Try to fetch a simple indicator
        data = wb.data.DataFrame('NY.GDP.MKTP.CD', ['USA'], mrv=1)
        assert isinstance(data, pd.DataFrame)
        assert not data.empty
    except Exception as e:
        pytest.fail(f"Failed to connect to World Bank API: {str(e)}")

def test_indicator_validity():
    """Test if our economic indicators are valid"""
    indicators = [
        'NY.GDP.MKTP.CD',  # GDP
        'FP.CPI.TOTL.ZG',  # Inflation
        'SL.UEM.TOTL.ZS'   # Unemployment
    ]
    
    for indicator in indicators:
        try:
            data = wb.data.DataFrame(indicator, ['USA'], mrv=1)
            assert not data.empty
        except Exception as e:
            pytest.fail(f"Invalid indicator {indicator}: {str(e)}")

def test_data_structure():
    """Test if the data structure is as expected"""
    data = wb.data.DataFrame('NY.GDP.MKTP.CD', ['USA'], mrv=1)
    
    # Check if the DataFrame has the expected structure
    assert 'time' in data.index.names
    assert 'economy' in data.index.names 