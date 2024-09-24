import requests
from requests import Session

import config
from modules import BaseChecker


class StakestoneChecker(BaseChecker):
    @staticmethod
    def fetch_drop_amount(address: str, session: Session = None) -> float:
        url = config.STAKESTONE_API.format(address=address)

        headers = {"User-Agent": config.FAKE_USER_AGENT}
        response = requests.get(url, headers=headers, allow_redirects=True)
        response.raise_for_status()

        body = response.json()

        drop_amounts = body["data"].get("pipelines", {})
        drop_amount = drop_amounts.get("tokenQualified", 0) + drop_amounts.get(
            "bonus", 0
        )

        return round(drop_amount, 4)
