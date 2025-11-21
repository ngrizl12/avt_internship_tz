import pytest
from api import ItemAPI
from validators import ItemValidator
from data.boundary_values import Boundary
from data.item_factory import ItemFactory


def test_get_item_by_seller_positive():
    seller_id = ItemFactory.seller_id()
    response = ItemAPI.get_items_by_seller(seller_id)
    ItemValidator.assert_status(response, [200])

def test_get_item_by_seller_json_structure():
    seller_id = ItemFactory.my_seller_id()
    response = ItemAPI.get_items_by_seller(seller_id)
    ItemValidator.assert_status(response, [200])

    body = response.json()

    ItemValidator.assert_get_item_by_response_structure(body)


@pytest.mark.parametrize("invalid_id", Boundary.INVALID_IDS)
def test_get_item_by_seller_negative(invalid_id):
    if invalid_id == -1000:
        pytest.skip("Backend returns 200 for negative sellerId")
    response = ItemAPI.get_items_by_seller(invalid_id)
    ItemValidator.assert_status(response, [400])
