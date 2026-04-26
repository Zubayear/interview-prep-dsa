from __future__ import annotations

from collections.abc import Iterable


class _Unordered:
    def __init__(self, expected):
        self.expected = expected

    def __eq__(self, actual):
        return _match_unordered(actual, self.expected)


def unordered(expected):
    return _Unordered(expected)


def _match_unordered(actual, expected):
    if isinstance(expected, (str, bytes)) or isinstance(actual, (str, bytes)):
        return actual == expected

    if _is_sequence(actual) and _is_sequence(expected):
        actual_items = list(actual)
        expected_items = list(expected)
        if len(actual_items) != len(expected_items):
            return False

        used = [False] * len(actual_items)
        for expected_item in expected_items:
            matched = False
            for index, actual_item in enumerate(actual_items):
                if used[index]:
                    continue
                if _match_unordered(actual_item, expected_item):
                    used[index] = True
                    matched = True
                    break
            if not matched:
                return False
        return True

    return actual == expected


def _is_sequence(value):
    return isinstance(value, Iterable) and not isinstance(value, (dict, str, bytes))
