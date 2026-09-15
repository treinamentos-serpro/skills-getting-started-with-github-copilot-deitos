def test_get_activities_returns_all_activity_details(client):
    expected_activity_names = {
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Soccer Club",
        "Swimming Club",
        "Art Club",
        "Drama Club",
        "Debate Club",
        "Science Club",
    }
    expected_fields = {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }

    response = client.get("/activities")

    assert response.status_code == 200
    activities = response.json()
    assert set(activities) == expected_activity_names
    assert all(set(activity) == expected_fields for activity in activities.values())
    assert activities["Chess Club"]["participants"] == [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]


def test_get_activities_returns_empty_participant_lists_for_new_activities(client):
    expected_empty_activities = {
        "Soccer Club",
        "Swimming Club",
        "Art Club",
        "Drama Club",
        "Debate Club",
        "Science Club",
    }

    response = client.get("/activities")

    assert response.status_code == 200
    activities = response.json()
    assert all(
        activities[name]["participants"] == []
        for name in expected_empty_activities
    )