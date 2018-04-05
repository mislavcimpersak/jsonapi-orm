"""Tests for `jsonapi_orm` package."""

import json

import pytest

from jsonapi_orm import response_to_obj


@pytest.fixture
def list_response():
    """JSON:API list pytest fixture."""
    return json.load(open('tests/responses/example_list.json'))


@pytest.fixture
def single_response():
    """JSON:API single pytest fixture."""
    return json.load(open('tests/responses/example_single.json'))


@pytest.fixture
def errors_response():
    """JSON:API errors pytest fixture."""
    return json.load(open('tests/responses/example_errors.json'))


def test_list_response(list_response):
    """Testing if data is a list of objects and these objects have set
    attributes.
    """
    obj = response_to_obj(list_response)

    assert obj.links.self == 'http://example.com/articles'
    assert isinstance(obj.data, list)

    assert obj.data[0].id == '1'
    assert obj.data[0].type == 'articles'
    assert obj.data[0].title == 'JSON API paints my bikeshed article 1!'
    assert obj.data[0].author.id == '9'
    assert obj.data[0].author.twitter == 'dgeb'
    assert obj.data[0].author.get('first-name') == 'Dan'

    assert obj.data[1].id == '2'
    assert obj.data[1].type == 'articles'
    assert obj.data[1].title == 'JSON API paints my bikeshed article 2!'
    assert obj.data[1].author.id == '2'
    assert obj.data[1].author.twitter == 'john'
    assert obj.data[1].author.get('first-name') == 'John'


def test_single_response(single_response):
    """Testing if data is a single object and this object has set
    attributes.
    """
    obj = response_to_obj(single_response)

    assert isinstance(obj.data, dict)

    assert obj.data.id == '1'
    assert obj.data.type == 'articles'
    assert obj.data.title == 'JSON API paints my bikeshed!'
    assert obj.data.author.id == '9'
    assert obj.data.author.twitter == 'dgeb'
    assert obj.data.author.get('first-name') == 'Dan'


def test_errors_response(errors_response):
    obj = response_to_obj(errors_response)

    assert isinstance(obj.errors, list)

    assert obj.errors[0].status == '403'
    assert obj.errors[1].status == '422'
    assert obj.errors[2].status == '500'
