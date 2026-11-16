from collections.abc import Callable, Iterable
from collections import defaultdict
from typing import Any


def filter_by_lambda(
    data: list[dict],
    condition: Callable[[dict], bool]
) -> list[dict]:
    return [record for record in data if condition(record)]


def group_by_attributes(
    data: Iterable[dict],
    attributes: list[str],
) -> dict[tuple, list[dict]]:
    """Группирует записи по указанным полям."""

    groups = defaultdict(list)
    for record in data:
        group_key = tuple(record.get(field) for field in attributes)
        groups[group_key].append(record)
    return groups


def aggregate_groups(
    groups: dict[tuple, list[dict]],
    aggregation: Callable,
    *args: Any,
    **kwargs: Any,
) -> dict[tuple, Any]:
    """Применяет одну агрегирующую функцию к каждой группе."""
    aggregated: dict[tuple, Any] = {}
    for group_key, records in groups.items():
        aggregated[group_key] = aggregation(records, *args, **kwargs)
    return aggregated



def flatten_nested_list(
    data: list[dict],
    list_field: list
):
    result = []
    for record in data:
        record_wo_list = {k: v for k, v in record.items() if k != list_field}
        nested_list = record[list_field]
        for item in nested_list:
            result.append({
                **record_wo_list,
                **item
            })
    return result
