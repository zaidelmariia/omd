from collections.abc import Callable
from typing import Any


def extract_nested_value(
    obj: dict[str, Any],
    keys: list[str],
) -> Any | None:
    """
    Возвращает значение из вложенного словаря по цепочке ключей.
    Если объект не является словарём или один из ключей отсутствует,
    возвращается None.
    """
    for key in keys:
        if isinstance(obj, dict) and key in obj:
            obj = obj[key]
        else:
            return None
    return obj


def process_dictionary_with_config(
    dictionary: dict[str, Any],
    config: dict[str, list[str] | tuple[list[str], Callable[[Any], Any]]],
) -> dict[str, Any]:
    """
    Обрабатывает словарь по конфигурации и возвращает новый словарь.
    Для каждого ключа конфигурации:
    - если значение представляет собой список, берётся путь к данным
    - если значение представляет собой кортеж, берётся путь и функция обработки
    - во всех остальных случаях возвращается None.
    """
    result = {}

    for key, value in config.items():
        if isinstance(value, tuple):
        # Извлечь значение и обработать
            path, processing_function = value
            extracted_value = extract_nested_value(
                dictionary,
                path,
            )
            if extracted_value is None:
                result[key] = None
            else:
                result[key] = processing_function(
                    extracted_value
                )
        elif isinstance(value, list):
        # Только извлечь значение
            path = value
            result[key] = extract_nested_value(dictionary, path)
        else:
            result[key] = None

    return result


def process_list_of_dicts_with_config(
    list_of_dicts: list[dict[str, Any]],
    config: dict[str, list[str] | tuple[list[str], Callable[[Any], Any]]],
) -> list[dict[str, Any]]:
    """"
    Обрабатывает список словарей по конфигурации
    Возвращает список словарей
    Для каждого словаря в списке:
    Для каждого ключа конфигурации:
    - если значение представляет собой список, берётся путь к данным
    - если значение представляет собой кортеж, берётся путь и функция обработки
    - во всех остальных случаях возвращается None.
    """
    result = []

    for dictionary in list_of_dicts:
        processed_dictionary = (
            process_dictionary_with_config(
                dictionary,
                config,
            )
        )
        result.append(processed_dictionary)

    return result


def create_processor(
    config: dict[str, list[str] | tuple[list[str], Callable]],
    list_processor: bool = False,
) -> Callable:
    """
    Создаёт функцию-обработчик на основе конфигурации.
    Если list_processor равен True,
    возвращается обработчик для списка словарей,
    иначе — для одного словаря. В обоих случаях готовая функция применяет
    выбранную функцию обработки к данным и конфигу.
    """
    if list_processor:
        processing_function = (
            process_list_of_dicts_with_config
        )
    else:
        processing_function = (
            process_dictionary_with_config
        )

    def processor(data):
        return processing_function(data, config)

    return processor