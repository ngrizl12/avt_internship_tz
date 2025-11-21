import pytest
from api import ItemAPI
from validators import ItemValidator
from data.boundary_values import Boundary
from data.item_factory import ItemFactory

def test_get_item_by_id_status_positive():
    item_id = ItemFactory.item_id()
    response = ItemAPI.get_item_by_id(item_id)
    ItemValidator.assert_status(response, [200])

def test_get_item_by_id_json_structure():
    item_id = ItemFactory.item_id()
    response = ItemAPI.get_item_by_id(item_id)
    ItemValidator.assert_status(response, [200])

    body = response.json()

    ItemValidator.assert_get_item_by_response_structure(body)


@pytest.mark.parametrize("invalid_id", Boundary.INVALID_IDS)
def test_get_item_by_id_negative(invalid_id):
    response = ItemAPI.get_item_by_id(invalid_id)
    ItemValidator.assert_status(response, [400])
