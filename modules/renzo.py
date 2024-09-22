import requests
from requests import Session

import config
from modules import BaseChecker


class RenzoChecker(BaseChecker):
    @staticmethod
    def fetch_drop_amount(address: str, session: Session = None) -> float:
        url = config.RENZO_API.format(address=address)
        headers = {"User-Agent": config.FAKE_USER_AGENT}
        response = requests.get(url, headers=headers, allow_redirects=True)

        if response.status_code == 403:
            return 0
        else:
            response.raise_for_status()

            body = response.json()
            events = body["events"]
            drop_amount = 0
            for event in events:
                drop_amount += int(event.get("awardAmount", 0))

            return round(drop_amount / 10 ** 18, 4)
