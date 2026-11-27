from __future__ import annotations

from typing import TYPE_CHECKING

import narwhals as nw
from narwhals.testing import assert_frame_equal

if TYPE_CHECKING:
    from tests.utils import Constructor

data = {"a": ["foo", "bars"], "ab": ["foo", "bars"]}


def test_pipe(constructor: Constructor) -> None:
    df = nw.from_native(constructor(data))
    columns = df.collect_schema().names()
    result = df.pipe(lambda _df: _df.select([x for x in columns if len(x) == 2]))
    expected = nw.from_native(constructor({"ab": ["foo", "bars"]}))
    assert_frame_equal(result, expected)
