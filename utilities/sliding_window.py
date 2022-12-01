from typing import List, TypeVar

T = TypeVar('T')


def window(window_size: int, list_to_be_windowed: List[T]) -> List[List[T]]:
    windowed = list(map(lambda index: list_to_be_windowed[index: index + window_size],
                        range(len(list_to_be_windowed) - window_size + 1)))
    return windowed


def windowstr(window_size: int, string_to_be_windowed: str) -> List[str]:
    windowed = list(map(lambda index: string_to_be_windowed[index: index + window_size],
                        range(len(string_to_be_windowed) - window_size + 1)))
    return windowed
