from flask import url_for, json


def test_munkres_api(test_client):
    result = test_client.post(
        url_for("munkres_api.process_matrix"),
        data=json.dumps({"matrix": [[5, 9, 1], [10, 3, 2], [8, 7, 4]]}),
    )
    assert result.get_json() == [[0, 1], [1, 0], [2, 2]]
