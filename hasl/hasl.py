import json
import requests
from .exceptions import *
from .version import __version__

_BASE_URL = 'https://api.sl.se/api2/'
_RI4_URL = _BASE_URL + \
           'realtimedeparturesV4.json?key={}&siteid={}&timeWindow={}'
_SI2_URL = _BASE_URL + 'deviations.json?key={}&siteid={}&lineNumber={}'
_TL2_URL = _BASE_URL + 'trafficsituation.json?key={}'

_USER_AGENT = "HASL/"+__version__


class haslapi(object):

    def __init__(self, timeout=None):
        self._timeout = timeout

    def version(self):
        return __version__

    def _get(self, url):

        api_errors = {
            1001: 'API key is over qouta',
            1002: 'API key is invalid',
            }

        try:
            resp = requests.get(url, headers={"User-agent": _USER_AGENT},
                                allow_redirects=True, timeout=self._timeout)
        except Exception as e:
            raise HASL_HTTP_Error(997, "A HTTP error occured", repr(e))

        try:
            jsonResponse = resp.json()
        except Exception as e:
            raise HASL_API_Error(998, "A parsing error occured", repr(e))

        if not jsonResponse:
            raise HASL_Error(999, "Internal error", "jsonResponse is empty")

        if jsonResponse['StatusCode'] == 0:
            return jsonResponse

        apiErrorText = api_errors.get(jsonResponse['StatusCode'])

        if apiErrorText:
            raise HASL_API_Error(jsonResponse['StatusCode'],
                                 apiErrorText,
                                 jsonResponse['Message'])
        else:
            raise HASL_API_Error(jsonResponse['StatusCode'],
                                 "Unknown API-response code encountered",
                                 jsonResponse['Message'])


class ri4api(haslapi):

    def __init__(self, api_token, siteid, window, timeout=None):
        super().__init__(timeout)
        self._api_token = api_token
        self._siteid = siteid
        self._window = window

    def request(self):
        return self._get(_RI4_URL.format(self._api_token,
                                         self._siteid, self._window))


class si2api(haslapi):

    def __init__(self, api_token, siteid, lines, timeout=None):
        super().__init__(timeout)
        self._api_token = api_token
        self._siteid = siteid
        self._lines = lines

    def request(self):
        return self._get(_SI2_URL.format(self._api_token,
                                         self._siteid, self._lines))


class tl2api(haslapi):
    def __init__(self, api_token, timeout=None):
        super().__init__(timeout)
        self._api_token = api_token

    def request(self):
        return self._get(_TL2_URL.format(self._api_token))
