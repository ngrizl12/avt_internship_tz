import random


class ItemFactory:

    @staticmethod
    def valid_item(seller_id=None):
        return {
            "sellerID": seller_id or random.randint(111111, 999999),
            "name": "Test Item",
            "price": 1200,
            "statistics": {
                "likes": 10,
                "viewCount": 20,
                "contacts": 5
            }
        }

    @staticmethod
    def invalid_name_item():
        body = ItemFactory.valid_item()
        body["name"] = ""
        return body

    @staticmethod
    def negative_price_item():
        body = ItemFactory.valid_item()
        body["price"] = -10
        return body

    @staticmethod
    def item_id():
        item_id = "b540ac51-c38e-4bb3-b000-aa8e31979cbc"
        return item_id

    @staticmethod
    def seller_id():
        seller_id = str(random.randint(111111, 999999))
        return seller_id

    @staticmethod
    def my_seller_id():
        seller_id = "176937"
        return seller_id

    @staticmethod
    def non_existing_id():
        non_existing_id = "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
        return non_existing_id

