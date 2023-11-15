

def transform(data):
    """
    Flatten nested dicts
    """
    results = dict()
    for item in list(data):
        if type(data[item]) is dict:
            for key in data[item]:
                results[key] = data[item][key]
        else:
            results[item] = data[item]
    return results


def final_transform(transformed_data):
    """
    Transform address structures into a single structure
    """
    transformed_data['address'] = str.format("{0}\n{1}, {2} {3}", 
                                             transformed_data['street'],
                                             transformed_data['state'], 
                                             transformed_data['city'], 
                                             transformed_data['zip'])
    transformed_data.pop('street', None)
    transformed_data.pop('state', None)
    transformed_data.pop('city', None)
    transformed_data.pop('zip', None)

    return transformed_data


def print_person(person_data):
    parents = " and ".join(person_data['parents'])
    siblings = " and ".join(person_data['siblings'])
    person_string = str.format(
        "Hello, my name is {0}, my siblings are {1}, "
        "my parents are {2}, and my mailing address is: \n{3}", 
        person_data['name'], parents, siblings, person_data['address'])
    print(person_string)


def main():
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

    suzy_data = {
        'name': 'Suzy Q. Public',
        'street': '456 Broadway',
        'apt': '333',
        'city': 'Miami',
        'state': 'FL',
        'zip': 33333,
        'relationships': {
            'siblings': ['John Q. Public', 'Michael R. Public', 
                        'Thomas Z. Public'],
            'parents': ['John Q. Public Sr.', 'Mary S. Public'],
        }
    }

    inputs = [john_data, suzy_data]

    for input_structure in inputs:
        transformed_data = transform(input_structure)
        final_transformed = final_transform(transformed_data)
        print_person(final_transformed)

def close():
    pass



if __name__=='__main__':
    main()
    