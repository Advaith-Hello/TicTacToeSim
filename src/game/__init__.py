from game.solve import create_table_3x3

from numba import types



table_type = types.DictType(
    types.UniTuple(types.int64, 2),
    types.UniTuple(types.int64, 2)
)
create_table_3x3.compile(
    (types.int64, types.int64, types.int64, table_type)
)
