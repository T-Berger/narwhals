from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

pytest.importorskip("numpy")
import numpy as np

import narwhals as nw
from narwhals.testing import assert_frame_equal

if TYPE_CHECKING:
    from tests.utils import ConstructorEager

data = {"a": ["foo", "bars"], "ab": ["foo", "bars"]}


def test_with_columns(constructor_eager: ConstructorEager) -> None:
    result = (
        nw.from_native(constructor_eager(data))
        .with_columns(d=np.array([4, 5]))  # pyright: ignore[reportArgumentType]
        .with_columns(e=nw.col("d") + 1)
        .select("d", "e")
    )
    expected = nw.from_native(constructor_eager({"d": [4, 5], "e": [5, 6]}))
    assert_frame_equal(result, expected)
