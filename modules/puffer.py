import requests
from requests import Session

import config
from modules import BaseChecker


class PufferChecker(BaseChecker):
    @staticmethod
    def fetch_drop_amount(address: str, session: Session = None) -> float:
        url = config.PUFFER_API.format(address=address)
        headers = {"User-Agent": config.FAKE_USER_AGENT}
        response = requests.get(url, headers=headers, allow_redirects=True)
        response.raise_for_status()

        body = response.json()

        if not body:
            return 0

        drop_amount = int(body[-1].get("amount", 0)) / 10 ** 18
        return round(drop_amount, 4)


if __name__ == '__main__':
    print(PufferChecker.fetch_drop_amount("0x176F3DAb24a159341c0509bB36B833E7fdd0a132"))
