"""Boundary test cases for the Trello API 'boards/' endpoint.

Tests verify behavior at the edge values of accepted input ranges,
such as minimum and maximum board name length.
"""

import pytest


@pytest.mark.parametrize("name_length, expected_status",
        [
            pytest.param(0, 400, id="len=0"),  # dodawć id w parametrach, czy niekoniecznie?
            (1, 200),
            (16384, 200),
            (16385, 400),
        ],
)
def test_create_board_boundary_name_length(boards_client, name_length, expected_status):
    """Verify that board name length boundaries return correct status codes."""
    test_name = "A" * name_length
    response = boards_client.create_board(test_name)
    assert response.status_code == expected_status, (
        f"Expexted status code {expected_status} when creating a board, got {response.status_code}"
    )
    if response.status_code == 200:
        board_id = response.json()["id"]
        boards_client.delete_board(board_id)
