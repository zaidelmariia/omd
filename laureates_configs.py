from json_dict_processing import create_processor
from prizes_configs import prize_processor

def process_year(date_string: str) -> int:
    """
    Извлекает год из даты в формате "YYYY-MM-DD", "YYYY-DD-MM"
    или  "YYYY-MM"
    Возвращает значение типа int
    """
    return int(date_string.split("-")[0])

CONFIG_PERSON = {
    "id": (["id"], int),
    "name": ["knownName", "en"],
    "gender": ["gender"],
    "birth_year": (["birth", "date"], process_year),
    "country_birth": ["birth", "place", "country", "en"],
    "country_now": ["birth", "place", "countryNow", "en"],
    "prizes_relevant": (["nobelPrizes"], prize_processor()),
}

CONFIG_ORG = {
    "id": (["id"], int),
    "name": ["orgName", "en"],
    "founded_year": (["founded", "date"], process_year),
    "country_founded": ["founded", "place", "country", "en"],
    "country_now": ["founded", "place", "countryNow", "en"],
    "prizes_relevant": (["nobelPrizes"], prize_processor()),
}


def person_processor():
    return create_processor(CONFIG_PERSON)


def org_processor():
    return create_processor(CONFIG_ORG)


process_persons = person_processor()
process_orgs = org_processor()
