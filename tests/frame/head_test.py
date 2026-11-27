from __future__ import annotations

from typing import TYPE_CHECKING

import narwhals as nw
from narwhals.testing import assert_frame_equal

if TYPE_CHECKING:
    from tests.utils import Constructor


def test_head(constructor: Constructor) -> None:
    data = {"a": [1, 3, 2], "b": [4, 4, 6], "z": [7.0, 8.0, 9.0]}
    expected = nw.from_native(constructor({"a": [1, 3], "b": [4, 4], "z": [7.0, 8.0]}))

    df_raw = constructor(data)
    df = nw.from_native(df_raw)

    result = df.head(2)
    assert_frame_equal(result.lazy().collect(), expected.lazy().collect())

    result = df.head(2)
    assert_frame_equal(result.lazy().collect(), expected.lazy().collect())

    # negative indices not allowed for lazyframes
    result = df.lazy().collect().head(-1)
    assert_frame_equal(result, expected.lazy().collect())
