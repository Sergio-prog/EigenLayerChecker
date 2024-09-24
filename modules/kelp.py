import requests
from requests import Session

import config
from modules import BaseChecker


class KelpChecker(BaseChecker):
    @staticmethod
    def fetch_drop_amount(address: str, session: Session = None) -> float:
        url = config.KELP_API.format(address=address)
        headers = {"User-Agent": config.FAKE_USER_AGENT}
        response = requests.get(url, headers=headers, allow_redirects=True)

        if response.status_code == 404:
            return 0

        response.raise_for_status()

        body = response.json()
        drop_amount = int(body.get("data", {}).get("el", 0))

        return round(drop_amount / 10**18, 4)
