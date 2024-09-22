from typing import Type

from requests import Session
from tabulate import tabulate

import config
from modules import BaseChecker
from modules.eigenlayer import EigenLayerChecker
from modules.kelp import KelpChecker
from modules.puffer import PufferChecker
from modules.renzo import RenzoChecker
from utils import fetch_wallets

all_checkers: dict[str, Type[BaseChecker]] = {
    "EigenLayer": EigenLayerChecker,
    "Renzo": RenzoChecker,
    "Puffer": PufferChecker,
    "Kelp": KelpChecker,
}


def get_all_drops_amount(address: str, session: Session = None) -> dict[str, float]:
    drop_amounts = {}
    for project_name, checker_class in all_checkers.items():
        drop_amounts[project_name] = checker_class.fetch_drop_amount(address, session)

    return drop_amounts


def main():
    wallets = fetch_wallets()
    result = {}
    session = Session()

    for wallet in wallets:
        result[wallet] = get_all_drops_amount(wallet, session)

    table_headers = ["Address", *all_checkers.keys()]

    def format_func(item):
        return item[0], *item[1].values()

    formated_result = list(map(format_func, result.items()))

    table = tabulate(formated_result, headers=table_headers, tablefmt="rounded_outline")
    if config.WRITE_TO_HTML:
        with open(f"{config.SAVE_FILE_NAME}.html", "w") as file:
            html_table = tabulate(formated_result, headers=table_headers, tablefmt="html")
            file.write(html_table)

    return table


if __name__ == '__main__':
    print(main())
