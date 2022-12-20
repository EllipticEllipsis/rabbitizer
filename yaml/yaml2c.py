#! /usr/bin/env python3
import argparse
import sys
import yaml
from typing import Union


def snake_case_to_PascalCase(s: str) -> str:
    return "".join(t.capitalize() for t in s.split("_"))


FILE_DESCRIPTION = """/* SPDX-FileCopyrightText: © 2022 Decompollaborate */
/* SPDX-License-Identifier: MIT */
"""

RABBITIZER_TYPE_PREFIX = "Rabbitizer"
RABBITIZER_ENUM_VARIANT_PREFIX = "RAB"


def write_file_description():
    print(FILE_DESCRIPTION)


# C enum formatting
ENUM_HEAD = """
typedef enum {prefix}{name} {{
"""
ENUM_NAME = "{enum_entry_prefix}_{variant}"
ENUM_FULL_ENTRY = "    " + ENUM_NAME + " = {number},"
ENUM_ENTRY = "    " + ENUM_NAME + ","
ENUM_FOOT = """
}} {prefix}{name};
"""


def make_enum_entry_prefix(name: str, data: list) -> str:
    return "_".join(
        [
            x
            for x in [
                RABBITIZER_ENUM_VARIANT_PREFIX,
                data.get("enum_entry_prefix", ""),
                name.upper(),
            ]
            if x != ""
        ]
    )


def make_enum_entry_variant(name: str, entry: dict) -> str:
    if type(entry) != dict:
        variant = entry
    elif entry.get("set"):
        variant = f'{entry.get("set")}_{str(entry["name"])}'
    else:
        variant = str(entry["name"])
    return variant.upper()


def write_enum(name: str, data: Union[list, str]):
    print(
        ENUM_HEAD.format(
            prefix=RABBITIZER_TYPE_PREFIX + data.get("var_prefix", ""),
            name=snake_case_to_PascalCase(name),
        )
    )
    entry_prefix = make_enum_entry_prefix(name, data)

    for i, entry in enumerate(data["data"]):
        variant = make_enum_entry_variant(name, entry)
        print(
            ENUM_ENTRY.format(
                enum_entry_prefix=entry_prefix,
                variant=variant,
                number=i,
            )
        )

    print(
        ENUM_FOOT.format(
            prefix=RABBITIZER_TYPE_PREFIX + data.get("var_prefix", ""),
            name=snake_case_to_PascalCase(name),
        )
    )


# C tables
TABLE_ENTRY_START = "    [" + ENUM_NAME + "] = "
TABLE_FOOT = """
}};
"""


REGNAME_TABLE_HEAD = """
const {ctype} {prefix}{name}_Names[][2] {{
"""


def write_regname_table(name: str, data: list):
    ctype = "char*"
    print(
        NAME_TABLE_HEAD.format(
            ctype=ctype,
            prefix=RABBITIZER_TYPE_PREFIX + data.get("var_prefix", ""),
            name=snake_case_to_PascalCase(name),
        )
    )
    entry_prefix = make_enum_entry_prefix(name, data)
    for entry in data["data"]:
        variant = make_enum_entry_variant(name, entry)
        print(
            TABLE_ENTRY_START.format(
                enum_entry_prefix=entry_prefix,
                variant=variant,
            ),
            end="",
        )
        print("{ ", end="")
        print(
            '"${numeric}", "${name}"'.format(
                name=entry["name"], numeric=entry["numeric"]
            ),
            end="",
        )
        print(" },")

    print(TABLE_FOOT.format())


NAME_TABLE_HEAD = """
const {ctype} {prefix}{name}_Names[] {{
"""


def write_name_table(name: str, data: list):
    ctype = "char*"
    print(
        NAME_TABLE_HEAD.format(
            ctype=ctype,
            prefix=RABBITIZER_TYPE_PREFIX + data.get("var_prefix", ""),
            name=snake_case_to_PascalCase(name),
        )
    )
    entry_prefix = make_enum_entry_prefix(name, data)
    for entry in data["data"]:
        variant = make_enum_entry_variant(name, entry)
        print(
            TABLE_ENTRY_START.format(
                enum_entry_prefix=entry_prefix,
                variant=variant,
            ),
            end="",
        )
        print(
            '"{name}",'.format(name=variant),
        )

    print(TABLE_FOOT.format())


DESCRIPTOR_TABLE_HEAD = """
const {ctype} {prefix}_{name}_Descriptors[] {{
"""


def write_descriptor_table(name: str, data: list):
    ctype = RABBITIZER_TYPE_PREFIX + data["var_prefix"] + "Descriptor"
    print(
        DESCRIPTOR_TABLE_HEAD.format(
            ctype=ctype,
            prefix=data["var_prefix"],
            name=snake_case_to_PascalCase(name),
        )
    )
    entry_prefix = make_enum_entry_prefix(name, data)
    for entry in data["data"]:
        variant = make_enum_entry_variant(name, entry)
        print(
            TABLE_ENTRY_START.format(
                enum_entry_prefix=entry_prefix,
                variant=variant,
            ),
            end="",
        )
        print("{ ", end="")
        columns_list = [
            f".{k}={v}" for k, v in entry.items() if k not in ["name", "numeric"]
        ]
        # replace Pythonic truth by C truth
        columns_str = ", ".join(columns_list).replace("=True", "=true")
        print(columns_str if columns_str else "0", end="")
        print(" },")
    print(TABLE_FOOT.format())


CALLBACKS_TABLE_HEAD = "const {ctype} {var}[] = {{"
CALLBACKS_TABLE_ROW = (
    "    ["
    + ENUM_NAME
    + "] = "
    + RABBITIZER_TYPE_PREFIX
    + "{prefix}_process_{func_variant},"
)


def write_callback_table(name: str, data: list):
    ctype = data["callback_type"]
    print(
        CALLBACKS_TABLE_HEAD.format(
            ctype=ctype,
            var=data["callback_table_var"],
        )
    )
    entry_prefix = make_enum_entry_prefix(name, data)
    for entry in data["data"]:
        variant = make_enum_entry_variant(name, entry)
        if entry["set"] != "all":
            print(
                CALLBACKS_TABLE_ROW.format(
                    enum_entry_prefix=entry_prefix,
                    variant=variant,
                    prefix=snake_case_to_PascalCase(name),
                    func_variant=variant.lower(),
                )
            )
    print(TABLE_FOOT.format())


MODE_SELECT = {
    "enum": write_enum,
    "desc": write_descriptor_table,
    "regname": write_regname_table,
    "names": write_name_table,
    "callbacks": write_callback_table,
}


def main() -> None:
    mode = sys.argv[1]
    infile = sys.argv[2]

    with open(infile) as f:
        y = yaml.load(f, Loader=yaml.SafeLoader)
        print(y)

        write_file_description()

        for name, data in y.items():
            MODE_SELECT[mode](name, data)


if __name__ == "__main__":
    main()
