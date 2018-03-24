============
JSON:API ORM
============


.. image:: https://img.shields.io/pypi/v/jsonapi_orm.svg
        :target: https://pypi.python.org/pypi/jsonapi_orm

.. image:: https://img.shields.io/travis/mislavcimpersak/jsonapi_orm.svg
        :target: https://travis-ci.org/mislavcimpersak/jsonapi_orm

.. image:: https://readthedocs.org/projects/jsonapi-orm/badge/?version=latest
        :target: https://jsonapi-orm.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Quick and dirty ORM that maps JSON:API responses to object attributes.


* Free software: BSD license
* Documentation: https://jsonapi-orm.readthedocs.io.


How To
------

Use Requests_ or (if you are a masochist) Python's built-in urllib modules to make the request to your JSON:API service and from there pass the response to JSON:API ORM.

So, first install requests and this lib:

.. code-block:: bash

    pip install requests
    pip install jsonapi-orm

Switch to your Python code and use the magic!

.. code-block:: python

    import requests
    from jsonapi_orm import response_to_obj


    # list of items
    r = requests.get('http://jsonapiplayground.reyesoft.com/v2/authors')
    obj = response_to_obj(r.json())

    print('LIST OF ITEMS:')
    for item in obj.data:
        print(item.name)

    # single item
    r = requests.get('http://jsonapiplayground.reyesoft.com/v2/authors/1')
    obj = response_to_obj(r.json())
    print('SINGLE ITEM')
    print(obj.data.name)


.. _Requests: http://docs.python-requests.org
