#!/usr/bin/env python3
""" safe_first_element """

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """
    Return the first element of the given sequence or
    None if the sequence is empty.

    Parameters:
        lst (Sequence[Any]): The sequence to get the first element from.

    Returns:
        Union[Any, NoneType]: The first element of the sequence or
        None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
