import json
import time
from functools import reduce
from typing import Type

from requests import Session
from tabulate import tabulate

import config
from modules import BaseChecker
from modules.eigenlayer import EigenLayerChecker
from modules.kelp import KelpChecker
from modules.magpie import MagpieChecker
from modules.puffer import PufferChecker
from modules.renzo import RenzoChecker
from modules.stakestone import StakestoneChecker
from utils import fetch_wallets
import csv

all_checkers: dict[str, Type[BaseChecker]] = {
    "EigenLayer": EigenLayerChecker,
    "Renzo": RenzoChecker,
    "Puffer": PufferChecker,
    "Kelp": KelpChecker,
    "Stakestone": StakestoneChecker,
    "Magpie": MagpieChecker,
}


def get_all_drops_amount(address: str, session: Session = None) -> dict[str, float]:
    drop_amounts = {}
    for project_name, checker_class in all_checkers.items():
        drop_amounts[project_name] = checker_class.fetch_drop_amount(address, session)

    return drop_amounts


def generate_table():
    wallets = fetch_wallets()
    result = {}
    session = Session()

    for wallet in wallets:
        result[wallet] = get_all_drops_amount(wallet, session)
        time.sleep(0.1)

    table_headers = ["N", "Address", *all_checkers.keys()]

    total_allocation = 0
    counter = 0

    def format_func(item):
        nonlocal counter, total_allocation
        counter += 1
        allocations: list[float] = item[1].values()
        total_allocation += reduce(lambda a, b: a + b, allocations)

        return counter, item[0], *allocations

    formated_result = list(map(format_func, result.items()))

    table = tabulate(formated_result, headers=table_headers, tablefmt="rounded_outline")
    if config.WRITE_TO_HTML:
        with open(f"{config.SAVE_FILE_NAME}.html", "w") as file:
            html_table = tabulate(formated_result, headers=table_headers, tablefmt="html")
            file.write(html_table)

    # TODO:
    if config.WRITE_TO_CSV:
        def format_csv_func(item):
            allocations = dict(zip(all_checkers.keys(), item[2:]))
            return {"N": item[0], "Address": item[1], **allocations}

        formated_csv_result = list(map(format_csv_func, formated_result))

        with open(f"{config.SAVE_FILE_NAME}.csv", "w") as file:
            csv_writer = csv.DictWriter(file, fieldnames=table_headers)
            csv_writer.writeheader()
            csv_writer.writerows(formated_csv_result)

    return table, total_allocation


def main():
    print("Processing wallets...\n")
    table, allocation = generate_table()
    print(table)
    print(f"\nTotal EIGEN allocation: {allocation}")

if __name__ == "__main__":
    main()
