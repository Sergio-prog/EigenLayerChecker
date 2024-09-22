import requests
from requests import Session

import config
from modules import BaseChecker


class EtherFiChecker(BaseChecker):
    @staticmethod
    def fetch_drop_amount(address: str, session: Session = None) -> float:
        url = config.ETHERFI_API.format(address=address)
        headers = {"User-Agent": config.FAKE_USER_AGENT}
        response = requests.post(url, headers=headers, allow_redirects=True)
        response.raise_for_status()

        body = response.json()
        print(body)

        return int(body["totalAllocation"]) / 10 ** 18


if __name__ == '__main__':
    print(EtherFiChecker.fetch_drop_amount("0x176f3dab24a159341c0509bb36b833e7fdd0a132"))
