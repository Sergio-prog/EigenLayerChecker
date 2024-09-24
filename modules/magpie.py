import requests
from requests import Session

import config
from modules import BaseChecker


class MagpieChecker(BaseChecker):
    @staticmethod
    def fetch_drop_amount(address: str, session: Session = None) -> float:
        url = config.MAGPIE_API.format(address=address)

        headers = {"User-Agent": config.FAKE_USER_AGENT}
        response = requests.get(url, headers=headers, allow_redirects=True)
        response.raise_for_status()

        body = response.json()
        drop_amount = int(
            body["data"]
            .get("elStakeDropData", {})
            .get("season2", {})
            .get("eigenShare", 0)
        )

        return round(drop_amount, 4)
