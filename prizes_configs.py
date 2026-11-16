from collections.abc import Callable
from typing import Any
from json_dict_processing import create_processor

PRIZE_CONFIG = {
    "prize_amount": (["prizeAmount"], int),
    "prize_amount_adjusted": (["prizeAmountAdjusted"], int),
    "award_year": (["awardYear"], int),
    "category_en": ["category", "en"],
    "prize_status": ["prizeStatus"]
}

def prize_processor():
    return create_processor(
        PRIZE_CONFIG,
        list_processor=True,
    )
