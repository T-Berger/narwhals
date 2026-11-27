from __future__ import annotations

from typing import TYPE_CHECKING

import narwhals as nw
from narwhals.testing import assert_frame_equal

if TYPE_CHECKING:
    from tests.utils import ConstructorEager


def test_clone(constructor_eager: ConstructorEager) -> None:
    data = {"a": [1, 2], "b": [3, 4]}
    expected = nw.from_native(constructor_eager(data), eager_only=True)
    expected_mod = nw.from_native(
        constructor_eager({"a": [1, 2], "b": [3, 4], "c": [4, 6]}), eager_only=True
    )
    df = nw.from_native(constructor_eager(data), eager_only=True)
    df_clone = df.clone()
    assert df is not df_clone
    assert df._compliant_frame is not df_clone._compliant_frame
    assert_frame_equal(df_clone, expected)
    df_clone_mod = df_clone.with_columns((nw.col("a") + nw.col("b")).alias("c"))
    assert_frame_equal(df, expected)
    assert_frame_equal(df_clone, expected)
    assert_frame_equal(df_clone_mod, expected_mod)
