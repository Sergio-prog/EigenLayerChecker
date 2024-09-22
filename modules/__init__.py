from abc import ABC

from requests import Session


class BaseChecker(ABC):
    """
    Base class for EIGEN token drop check. Well, idk why I wrote it now.
    """
    @staticmethod
    def fetch_drop_amount(address: str, session: Session = None) -> float | int:
        pass
