
import sys
sys.path.append('../scripts')

import pytest
import node3

@pytest.fixture(params=['nodict', 'dict'])
def generate_data(request):
    test_input = {
        'name': 'John Q. Public',
        'street': '123 Main St.',
        'city': 'Anytown',
        'state': 'FL',
        'zip': 99999,
    }

    transformed_data = {
        'name': 'John Q. Public',
        'street': '123 Main St.',
        'city': 'Anytown',
        'state': 'FL',
        'zip': 99999,
    }

    if request.param == 'dict':
        test_input['relationships'] = {
            'siblings': ['Michael R. Public', 'Suzy Q. Public'],
            'parents': ['John Q. Public Sr.', 'Mary S. Public'],
        }

        transformed_data['siblings'] = ['Michael R. Public', 'Suzy Q. Public']
        transformed_data['parents'] = ['John Q. Public Sr.', 'Mary S. Public']
    
    return test_input, transformed_data

@pytest.fixture
def generate_final_transform():
    transformed_data = {
        'name': 'John Q. Public',
        'siblings': ['Michael R. Public', 'Suzy Q. Public'],
        'parents': ['John Q. Public Sr.', 'Mary S. Public'],
        'street': '123 Main St.',
        'city': 'Anytown',
        'state': 'FL',
        'zip': 99999,
    }

    final_transform = {
        'name': 'John Q. Public',
        'siblings': ['Michael R. Public', 'Suzy Q. Public'],
        'parents': ['John Q. Public Sr.', 'Mary S. Public'],
    }

    final_transform['address'] = str.format("{0}\n{1}, {2} {3}", 
                                             transformed_data['street'],
                                             transformed_data['state'], 
                                             transformed_data['city'], 
                                             transformed_data['zip'])
    return transformed_data, final_transform


def test_transform(generate_data):
    test_input = generate_data[0]
    transformed_data = generate_data[1]
    assert node3.transform(test_input) == transformed_data, "Something wrong here!"

def test_final_transform(generate_final_transform):
    transformed_data = generate_final_transform[0]
    expected_result = generate_final_transform[1]
    results = node3.final_transform(transformed_data)
    assert results == expected_result, "Something wrong here."


