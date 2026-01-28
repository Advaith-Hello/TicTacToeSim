from numba.typed import Dict
from numba import types

import json



def save_numba_dict(n_dict, path):
    py_dict = {(int(k[0]), int(k[1])): (int(v[0]), int(v[1])) for k, v in n_dict.items()}
    json_dict = {f"{k[0]}_{k[1]}": [v[0], v[1]] for k, v in py_dict.items()}
    with open(path, "w") as f:
        json.dump(json_dict, f)


def load_numba_dict(path):
    n_dict = Dict.empty(
        key_type=types.UniTuple(types.int64, 2),
        value_type=types.UniTuple(types.int64, 2)
    )

    with open(path, "r") as f:
        json_dict = json.load(f)

    for k_str, v_list in json_dict.items():
        k0, k1 = map(int, k_str.split("_"))
        n_dict[(k0, k1)] = (int(v_list[0]), int(v_list[1]))

    return n_dict
