def test_root_redirects_to_static_index(client):
    expected_location = "/static/index.html"

    response = client.get("/", follow_redirects=False)

    assert response.status_code == 307
    assert response.headers["location"] == expected_location


def test_root_redirect_target_serves_index_page(client):
    response = client.get("/", follow_redirects=True)

    assert response.status_code == 200
    assert "Mergington High School" in response.text