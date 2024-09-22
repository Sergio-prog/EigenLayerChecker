import requests
from requests import Session

import config
from modules import BaseChecker


class SwellChecker(BaseChecker):
    @staticmethod
    def fetch_drop_amount(address: str, session: Session = None) -> float:
        url = "https://v3-lrt.svc.swellnetwork.io/swell.v3.WalletService/EigenlayerAirdrop" # config.SWELL_API.format(address=address)
        params = {
            "connect": "v1",
            "encoding": "json",
            "message": '{"walletAddress":"{' + address + '}"}'
        }

        headers = {
            "User-Agent": config.FAKE_POSTMAN_USER_AGENT,
            "Host": "v3-lrt.svc.swellnetwork.io",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        response = requests.get(url, params=params, headers=headers, allow_redirects=True)
        print(url, response.request.headers, response.text, response.status_code)

        response.raise_for_status()

        body = response.json()
        drop_amount = int(body.get("cumulativeAmount", 0))

        return round(drop_amount / 10 ** 18, 4)
