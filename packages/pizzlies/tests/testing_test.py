from __future__ import annotations

from typing import Any

import pytest
from pizzlies.testing import dict_constructor

import narwhals as nw


@pytest.mark.parametrize(
    "columns",
    [
        pytest.param(lambda np: np.arange(2), id="numpy-positions"),
        pytest.param(lambda np: np.array(["col1", "col2"]), id="numpy-labels"),
        pytest.param(lambda _: [0, 1], id="list-positions"),
        pytest.param(lambda _: ["col1", "col2"], id="list-labels"),
    ],
)
def test_dict_constructor_numpy_column_keeps_dtype(columns: Any) -> None:
    np = pytest.importorskip("numpy")
    data = {"col1": ["a", "b", "c", "d"], "col2": np.arange(4), "col3": [4, 3, 2, 1]}
    df = nw.from_native(dict_constructor(data), eager_only=True)
    result = df[:, columns(np)]
    assert result.schema == {"col1": nw.String(), "col2": nw.Int64()}
    assert result.to_native() == {"col1": ["a", "b", "c", "d"], "col2": [0, 1, 2, 3]}
