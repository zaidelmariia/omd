from collections import Counter
from statistics import mean, median
from typing import Any


def mean_value(
    records: list[dict[str, Any]],
    field: str,
) -> float | None:
    """Возвращает среднее арифметическое по полю или None, если список пуст."""
    values = [r.get(field) for r in records]
    values = [v for v in values if v is not None]
    if not values:
        return None
    return mean(values)


def median_value(
    records: list[dict[str, Any]],
    field: str,
) -> float | None:
    """Возвращает медиану по полю или None, если список пуст."""
    values = [r.get(field) for r in records]
    values = [v for v in values if v is not None]
    if not values:
        return None
    return median(values)


def min_value(
    records: list[dict[str, Any]],
    field: str,
) -> int | float | None:
    """Возвращает минимальное числовое значение по полю."""
    values = [r.get(field) for r in records]
    values = [v for v in values if v is not None]
    if not values:
        return None
    return min(values)


def max_value(
    records: list[dict[str, Any]],
    field: str,
) -> int | float | None:
    """Возвращает максимальное числовое значение по полю."""
    values = [r.get(field) for r in records]
    values = [v for v in values if v is not None]
    if not values:
        return None
    return max(values)


def count_by_value(
    records: list[dict[str, Any]],
    field: str,
    include_missing: bool = False,
) -> Counter:
    """Считает записи для каждого уникального значения поля."""
    values = [record.get(field) for record in records]
    if not include_missing:
        values = [v for v in values if v is not None]
    return Counter(values)


def top_n_by_field(
    records: list[dict[str, Any]],
    field: str,
    n: int,
    descending: bool = True,
) -> list[dict[str, Any]]:
    """Возвращает до N записей, отсортированных по значению поля."""
    records = [
        record
        for record in records
        if record.get(field) is not None
    ]
    return sorted(
        records,
        key=lambda r: r[field],
        reverse=descending,
    )[:n]


def top_n_counts(
    records: list[dict[str, Any]],
    field: str,
    n: int,
) -> list[tuple[Any, int]]:
    """Возвращает N наиболее частых непустых значений поля."""
    counts = count_by_value(records, field)
    return counts.most_common(n)
