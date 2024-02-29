# pylint: disable=R0913


class HttpResponse:

    def __init__(self, status_code=None, body=None) -> None:
        self.status_code = status_code
        self.body = body
