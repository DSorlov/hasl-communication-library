import json
import logging
import os
import stat

import requests

from .exceptions import *
from .version import __version__

_BASE_URL = 'https://api.sl.se/api2/'
_RI4_URL = _BASE_URL + 'realtimedeparturesV4.json?key={}&siteid={}&timeWindow={}'
_SI2_URL = _BASE_URL + 'deviations.json?key={}&siteid={}&lineNumber={}'
_TL2_URL = _BASE_URL + 'trafficsituation.json?key={}'
_USER_AGENT = "HASL/"+__version__
_AUTH_ERRS = (401, 403)

_LOGGER = logging.getLogger(__name__)

class haslapi(object):

    def __init__(self, timeout=None):
        self._timeout = timeout          

    def _get(self, url):
    
        resp = requests.get(url, headers={"User-agent": _USER_AGENT}, allow_redirects=True, timeout=self._timeout)
    
        if resp.status_code in (401, 403):
            _LOGGER.error("HASL: Failed fetching data for '%s'"
                          "(HTTP Status_code = %d)", url,
                          resp.status_code) 

        resp.raise_for_status()
        return resp.json()

class ri4api(haslapi):

    def __init__(self, api_token, siteid, window, timeout=None):
        super().__init__(timeout)
        self._api_token = api_token
        self._siteid = siteid
        self._window = window

    def request(self):
        return self._get(_RI4_URL.format(self._api_token,self._siteid,self._window))

class si2api(haslapi):

    def __init__(self, api_token, siteid, lines, timeout=None):
        super().__init__(timeout)
        self._api_token = api_token
        self._siteid = siteid
        self._lines = lines

    def request(self):
        return self._get(_SI2_URL.format(self._api_token,self._siteid,self._lines))
        
class tl2api(haslapi):
    def __init__(self, api_token, timeout=None):
        super().__init__(timeout)
        self._api_token = api_token
        
    def request(self):
        return self._get(_TL2_URL.format(self._api_token))


