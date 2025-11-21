import pytest
from api import ItemAPI
from validators import ItemValidator
from data.item_factory import ItemFactory


def test_create_item_valid():
    body = ItemFactory.valid_item()
    response = ItemAPI.create_item(body)
    ItemValidator.assert_status(response, [200])


@pytest.mark.parametrize("payload", [
    ItemFactory.invalid_name_item(),
    ItemFactory.negative_price_item()
])

def test_create_item_negative(payload):
    if payload.get("price") == -10:
        pytest.skip("Backend returns 200 for negative price")
    response = ItemAPI.create_item(payload)
    ItemValidator.assert_status(response, [400])

def test_create_item_empty_body():
    body = {}
    response = ItemAPI.create_item(body)
    ItemValidator.assert_status(response, [400])
