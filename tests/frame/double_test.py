from __future__ import annotations

from typing import TYPE_CHECKING

import narwhals as nw
from narwhals.testing import assert_frame_equal

if TYPE_CHECKING:
    from tests.utils import Constructor


def test_double(constructor: Constructor) -> None:
    data = {"a": [1, 3, 2], "b": [4, 4, 6], "z": [7.0, 8.0, 9.0]}
    df = nw.from_native(constructor(data))

    result = df.with_columns(nw.all() * 2)
    expected = nw.from_native(
        constructor({"a": [2, 6, 4], "b": [8, 8, 12], "z": [14.0, 16.0, 18.0]})
    )
    assert_frame_equal(result, expected)

    result = df.with_columns(nw.col("a").alias("o"), nw.all() * 2)
    expected = nw.from_native(
        constructor(
            {"a": [2, 6, 4], "b": [8, 8, 12], "z": [14.0, 16.0, 18.0], "o": [1, 3, 2]}
        )
    )
    assert_frame_equal(result, expected)
