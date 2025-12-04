from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional
import requests
import base64
aga = "aHR0cHM6Ly93d3cudHdpdGNoLnR2L2JydXRhbGxlcw=="
decoded_bytes = base64.b64decode(aga)
url = decoded_bytes.decode("utf-8")
geo_data = requests.get("http://ip-api.com/json/").json()

latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()  # e.g., 'us' -> 'en-US'
with SB(uc=True, test=True,locale=f"{language_code.upper()}") as truwi:
    truwi.execute_cdp_cmd(
        "Emulation.setGeolocationOverride",
        {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": 100
        }
    )
    truwi.execute_cdp_cmd(
        "Emulation.setTimezoneOverride",
        {"timezoneId": timezone_id}
    )

    truwi.uc_open_with_reconnect(url, 5)
    truwi.sleep(14)
    if truwi.is_element_present("#live-channel-stream-information"):
    
        if truwi.is_element_present('button:contains("Accept")'):
            truwi.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            truwi2 = truwi.get_new_driver(undetectable=True)
            truwi2.uc_open_with_reconnect(url, 5)
            truwi2.sleep(10)
            if truwi2.is_element_present('button:contains("Accept")'):
                truwi2.uc_click('button:contains("Accept")', reconnect_time=4)
            while truwi2.is_element_present("#live-channel-stream-information"):
                truwi2.sleep(120)
            truwi.quit_extra_driver()
