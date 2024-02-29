from src.data.tests.user_finder import UserFinderSpy
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.controllers.user_finder_controller import UserFinderController


class HttpResquestMock:
    def __init__(self) -> None:
        self.query_params = {"first_name": "meuTeste"}


def test_handle():

    http_request_mock = HttpResquestMock()
    use_case = UserFinderSpy()
    user_finder_controller = UserFinderController(use_case)

    response = user_finder_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.body["data"] is not None
    assert response.status_code == 200
