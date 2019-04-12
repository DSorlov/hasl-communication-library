import json
import logging
import os
import stat

import requests

from .exceptions import *
from .version import __version__

_BASE_URL = 'https://api.sl.se/api2/'
_DEPARTURE_URL = _BASE_URL + 'realtimedeparturesV4.json?key={}&siteid={}&timeWindow={}'
_DEVIATION_URL = _BASE_URL + 'deviations.json?key={}&siteid={}&lineNumber={}'
_USER_AGENT = "HASL/"+__version__
_AUTH_ERRS = (401, 403)

_LOGGER = logging.getLogger(__name__)


class hasl(object):

    def __init__(self, deviation_api_token, departure_api_token, siteid, lines, window, timeout=None):
        self._deviation_api_token = deviation_api_token
        self._departure_api_token = departure_api_token
        self._siteid = siteid
        self._lines = lines
        self._window = window
        self._timeout = timeout	

    def _get(self, url):
	
        resp = requests.get(url, headers={"User-agent": _USER_AGENT}, allow_redirects=True, timeout=self._timeout)
	
        if resp.status_code in (401, 403):
            _LOGGER.error("HASL: Failed fetching data for '%s'"
                          "(HTTP Status_code = %d)", url,
                          resp.status_code) 

        resp.raise_for_status()
        return resp.json()

    def get_departures(self):
        return self._get(_DEPARTURE_URL.format(self._departure_api_token,self._siteid,self._window))

    def get_deviations(self):
        return self._get(_DEVIATION_URL.format(self._deviation_api_token,self._siteid,self._lines))

