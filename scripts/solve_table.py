from game.solve import create_table_3x3
from game.json_utils import save_numba_dict
from numba import types
from numba.typed import Dict

import time



lookup_table = Dict.empty(
    key_type=types.UniTuple(types.int64, 2),
    value_type=types.UniTuple(types.int64, 2)
)

s = time.perf_counter()
create_table_3x3(0, 0, player=1, table=lookup_table)
e = time.perf_counter()
print(len(lookup_table), e-s)

save_numba_dict(lookup_table, "../data/lookup_table.json")
