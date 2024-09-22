import requests
from requests import Session

import config
from modules import BaseChecker


class EigenLayerChecker(BaseChecker):
    @staticmethod
    def fetch_drop_amount(address: str, session: Session = None) -> float:
        url = config.EL_API.format(address=address)
        headers = {"User-Agent": config.FAKE_USER_AGENT}
        response = requests.get(url, headers=headers, allow_redirects=True)
        response.raise_for_status()

        body = response.json()
        token_amounts = body["season2"]["data"]["pipelines"]

        return token_amounts["tokenQualified"] + token_amounts["bonus"]
