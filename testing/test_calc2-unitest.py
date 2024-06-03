import unittest
import tempfile
import os
from calc2unitest import read_numbers_from_file

class TestReadNumbersFromFile(unittest.TestCase):
    def test_read_numbers_from_file(self):
        # Create a temporary file with test data
        with tempfile.NamedTemporaryFile(delete=False, mode='w') as f:
            f.write("1.0\n2.0\n3.5\n")
            temp_filename = f.name
        
        # Test the read_numbers_from_file function
        result = read_numbers_from_file(temp_filename)
        self.assertEqual(result, [1.0, 2.0, 3.5])
        
        # Clean up the temporary file
        os.remove(temp_filename)

if __name__ == '__main__':
    unittest.main()
