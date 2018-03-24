"""Tests for `jsonapi_orm` package."""

import json

import pytest


from jsonapi_orm import jsonapi_orm


@pytest.fixture
def response():
    """JSON:API list pytest fixture."""
    return json.load(open('tests/responses/example_list.json'))

@pytest.fixture
def response():
    """JSON:API single pytest fixture."""
    return json.load(open('tests/responses/example_single.json'))

@pytest.fixture
def response():
    """JSON:API errors pytest fixture."""
    return json.load(open('tests/responses/example_errors.json'))


def test_dummy(response):
    """Dummy test for now."""
    assert 1 + 2 == 3
