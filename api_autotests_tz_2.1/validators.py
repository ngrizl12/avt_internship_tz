class ItemValidator:

    @staticmethod
    def assert_status(response, expected_codes):
        assert response.status_code in expected_codes

    @staticmethod
    def assert_get_item_by_response_structure(body):
        assert isinstance(body, list)
        assert len(body) > 0

        item = body[0]

        assert isinstance(item["id"], str)
        assert isinstance(item["sellerId"], int)
        assert isinstance(item["name"], str)
        assert isinstance(item["price"], int)
        assert isinstance(item["createdAt"], str)

        stats = item["statistics"]
        assert isinstance(stats["likes"], int)
        assert isinstance(stats["viewCount"], int)
        assert isinstance(stats["contacts"], int)

class StatisticValidator:

    @staticmethod
    def assert_ok(response):
        assert response.status_code == 200
        stats = response.json()[0]
        assert "likes" in stats
        assert "viewCount" in stats
        assert "contacts" in stats

    @staticmethod
    def assert_status(response, expected_codes):
        assert response.status_code in expected_codes

