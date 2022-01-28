class ThreeScaleApiError(Exception):
    def __init__(self, message, *args):
        self.message = message
        super(ThreeScaleApiError, self).__init__(message, *args)


class ApiClientError(ThreeScaleApiError):
    def __init__(self, code, reason, body, message: str = None):
        self.code = code
        self.reason = reason
        self.body = body
        self._message = message
        msg = f"Response({self.code} {reason}): {body}"
        if message:
            msg += f"; {message}"
        super(ApiClientError, self).__init__(msg)
