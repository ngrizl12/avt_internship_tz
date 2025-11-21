import pytest
from api import StatisticAPI
from validators import StatisticValidator
from data.boundary_values import Boundary
from data.item_factory import ItemFactory


def test_statistic_positive():
    item_id = ItemFactory.item_id()
    response = StatisticAPI.get_statistic(item_id)
    StatisticValidator.assert_ok(response)

@pytest.mark.parametrize("invalid_id", Boundary.INVALID_IDS)
def test_statistic_negative(invalid_id):
    response = StatisticAPI.get_statistic(invalid_id)
    StatisticValidator.assert_status(response, [400])
