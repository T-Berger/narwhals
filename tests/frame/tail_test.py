from __future__ import annotations

from typing import TYPE_CHECKING

import narwhals as nw
from narwhals.testing import assert_frame_equal

if TYPE_CHECKING:
    from tests.utils import ConstructorEager


def test_tail(constructor_eager: ConstructorEager) -> None:
    data = {"a": [1, 3, 2], "b": [4, 4, 6], "z": [7.0, 8.0, 9.0]}
    expected = nw.from_native(
        constructor_eager({"a": [3, 2], "b": [4, 6], "z": [8.0, 9]})
    )
    df_raw = constructor_eager(data)
    df = nw.from_native(df_raw)
    result = df.tail(2)
    assert_frame_equal(result, expected)
    result = df.tail(-1)
    assert_frame_equal(result, expected)
