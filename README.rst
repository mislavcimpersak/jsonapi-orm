============
JSON:API ORM
============


.. image:: https://badge.fury.io/py/jsonapi-orm.svg
    :target: https://badge.fury.io/py/jsonapi-orm
    :alt: PyPI

.. image:: https://circleci.com/gh/mislavcimpersak/jsonapi-orm.svg?style=svg
    :target: https://circleci.com/gh/mislavcimpersak/jsonapi-orm
    :alt: CircleCI

.. image:: https://coveralls.io/repos/github/mislavcimpersak/jsonapi-orm/badge.svg?branch=master
    :target: https://coveralls.io/github/mislavcimpersak/jsonapi-orm?branch=master
    :alt: Coveralls

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
    r = requests.get('https://raw.githubusercontent.com/mislavcimpersak/jsonapi-orm/master/tests/responses/example_list.json')
    obj = response_to_obj(r.json())

    print('LIST OF ITEMS:')
    for item in obj.data:
        print(item.title)
        # author is defined as a relationship
        print(item.author.twitter)


    # single item
    r = requests.get('https://raw.githubusercontent.com/mislavcimpersak/jsonapi-orm/master/tests/responses/example_single.json')
    obj = response_to_obj(r.json())

    print('SINGLE ITEM')
    print(obj.data.title)
    # author is defined as a relationship
    print(obj.data.author.id)
    print(obj.data.author.twitter)


Caveats
-------

* Since Python object attribute names `have certain rules`__ like not starting with a number or not containing "-" char, all such attributes can be accessed using ``.get()`` method. Ie. ``obj.data.author.get('first-name')``.

* If relationship is not described in more detail in the ``included`` part of the response matching fails silently.

* For now, this lib does not lazily follow relationship links or anything like that. You can of course make a new request to the given link and pass that response to JSON:API ORM.

* For now, there is no check if response is a valid JSON:API response. But you'll probably get that you are trying to parse an invalid response when things start to break.

* And last, this lib requires Python 3.5 or newer.


.. _Requests: http://docs.python-requests.org
.. _rules: https://docs.python.org/3/reference/lexical_analysis.html#identifiers

__ rules_
