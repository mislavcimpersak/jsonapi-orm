"""Tests for `jsonapi_orm` package."""

import json

import pytest


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


def test_dummy():
    """Dummy test for now."""
    assert 1 + 2 == 3
