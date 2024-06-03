import pytest
import tempfile
import os
from calc2pytest import read_numbers_from_file

def test_read_numbers_from_file():
    # Create a temporary file with test data
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as f:
        f.write("1.0\n2.0\n3.5\n")
        temp_filename = f.name
    
    # Test the read_numbers_from_file function
    result = read_numbers_from_file(temp_filename)
    assert result == [1.0, 2.0, 3.5]
    
    # Clean up the temporary file
    os.remove(temp_filename)
