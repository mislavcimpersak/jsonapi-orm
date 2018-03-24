"""Main module."""

from munch import Munch, munchify


def response_to_obj(response: dict) -> Munch:
    # TODO this is bad and I should feel bad
    global includes
    includes = mapped_included(response.get('included'))

    return munchify(resolve(response))


def resolve(response: dict) -> dict:
    for key, value in response.items():
        if key == 'data':
            if isinstance(value, list):
                response['data'] = []
                for order, item in enumerate(value):
                    response['data'].append(resolve_single_data_item(item))
            elif isinstance(value, dict):
                response['data'] = resolve_single_data_item(value)
            else:
                raise Exception(
                    'Invalid JSON:API response. '
                    '"data" is type "{type(value)}".'
                )
        else:
            pass

    try:
        del response['included']
    except KeyError:
        pass

    # Have to keep response['data'] because on that level of dict other keys
    # like links, meta, errors need to be present.
    # Also, because data can be a single item or a list
    return response


def resolve_single_data_item(data: dict) -> dict:
    if data is None:
        # case if child from relationships is missing from included
        # TODO handle better, at least send type and id
        # and send info to logger
        return {}

    attributes = data.get('attributes')
    if attributes:
        for key, value in attributes.items():
            data[key] = value
        del data['attributes']

    relationships = data.get('relationships')
    if relationships:
        for key, value in relationships.items():
            child = resolve(value)
            child_data = child['data']
            if isinstance(child_data, dict):
                data[key] = resolve_single_data_item(
                    includes.get(
                        (child_data.get('type'), child_data.get('id'))
                    )
                )
            elif isinstance(child_data, list):
                data[key] = []
                for item in child_data:
                    data[key].append(
                        resolve_single_data_item(
                            includes.get((item.get('type'), item.get('id')))
                        )
                    )

        del data['relationships']

    return data


def mapped_included(inc: dict) -> dict:
    """Makes included more easily searchable by creating a dict that
    has (type,id) pair as key.

    Also, returned value for the key can be used for relationships node.

    ie.
    {
        ('people', '12'): {
            'id': '12,
            'type': 'people',
            'attributes': {
                'name': 'John'
            }
        },
        ('tag', '11'): {
            ...
        }
    }
    """
    included = {}

    if inc:
        for include in inc:
            included[include.get('type'), include.get('id')] = include

    return included
