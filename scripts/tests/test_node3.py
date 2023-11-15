
import sys
sys.path.append('../scripts')

import pytest
import node3


class TestNode3:
    def test_transformed_data(self):
        john_data = {
            'name': 'John Q. Public',
            'street': '123 Main St.',
            'city': 'Anytown',
            'state': 'FL',
            'zip': 99999,
            'relationships': {
                'siblings': ['Michael R. Public', 'Suzy Q. Public'],
                'parents': ['John Q. Public Sr.', 'Mary S. Public'],
            }
        }
        results = node3.transform(john_data)
        assert len(results) == 7, "Results should have 7 elements"

    def test_final_transform(self):
        john_data = {
            'name': 'John Q. Public',
            'street': '123 Main St.',
            'city': 'Anytown',
            'state': 'FL',
            'zip': 99999,
            'relationships': {
                'siblings': ['Michael R. Public', 'Suzy Q. Public'],
                'parents': ['John Q. Public Sr.', 'Mary S. Public'],
            }
        }
        transformed_data = node3.transform(john_data)
        results = node3.final_transform(transformed_data)
        assert len(results) == 4, "Results should be 4 element"


