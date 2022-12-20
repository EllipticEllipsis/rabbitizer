#! /usr/bin/env python3
import argparse
import sys
import yaml


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


def write_enum(name: str, data: list):
    print(
        ENUM_HEAD.format(
            prefix= RABBITIZER_TYPE_PREFIX + data.get("prefix", ""),
            name=snake_case_to_PascalCase(name),
        )
    )
    prefix = "_".join([ x for x in [RABBITIZER_ENUM_VARIANT_PREFIX, data.get("enum_entry_prefix"), name.upper()] if x is not None ])
    for i, entry in enumerate(data["data"]):
        if type(entry) != dict:
            variant = entry
        elif entry.get("set"):
            variant = f'{entry.get("set")}_{str(entry["name"])}'.upper()
        else:
            variant = str(entry["name"]).upper()
        print(
            ENUM_ENTRY.format(
                enum_entry_prefix=prefix,
                variant=variant,
                number=i,
            )
        )

    print(
        ENUM_FOOT.format(
            prefix="Rabbitizer",
            name=snake_case_to_PascalCase(name),
        )
    )


# C tables
TABLE_ENTRY_START = "    [" + ENUM_NAME + "] = "
TABLE_FOOT = """
}};
"""

DESCRIPTOR_TABLE_HEAD = """
const {ctype} {prefix}_{name}_Descriptors[] {{
"""


def write_descriptor_table(name, data):
    ctype = data["prefix"] + "Descriptor"
    print(
        DESCRIPTOR_TABLE_HEAD.format(
            ctype=ctype,
            prefix=data["prefix"],
            name=snake_case_to_PascalCase(name),
        )
    )
    for entry in data["data"]:
        print(
            TABLE_ENTRY_START.format(
                prefix=name.upper(),
                variant=entry["name"],
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
    print(TABLE_FOOT)


NAME_TABLE_HEAD = """
const {ctype} {prefix}_{name}_Names[][2] {{
"""


def write_name_table(name, data):
    ctype = "char*"
    print(
        NAME_TABLE_HEAD.format(
            ctype=ctype,
            prefix=data["prefix"],
            name=snake_case_to_PascalCase(name),
        )
    )
    for entry in data["data"]:
        print(
            TABLE_ENTRY_START.format(
                prefix=name.upper(),
                variant=entry["name"],
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

    print(TABLE_FOOT)

CALLBACKS_TABLE_HEAD = "const {ctype} {var}[] = {{"
CALLBACKS_TABLE_ROW = "    [" + ENUM_NAME + "] = {callback_preprefix}_process_{variant},"

def write_callback_table(name, data):
    ctype = data["callback_type"]
    print(
        CALLBACKS_TABLE_HEAD.format(
            ctype=ctype,
            var=data["callback_table_var"],
        )
    )
    for entry in data["data"]:
        if entry["prefix"] != "ALL":
            print(
                CALLBACKS_TABLE_ROW.format(
                    enum_entry_prefix=data["enum_entry_prefix"],
                    variant=f'{entry["prefix"]}_{entry["operand"]}',
                    callback_preprefix=f"Rabbitizer{snake_case_to_PascalCase(name)}",
                    operand=entry["operand"],
                )
            )
    print(TABLE_FOOT)

MODE_SELECT = {
    "enum": write_enum,
    "desc": write_descriptor_table,
    "name": write_name_table,
    "call": write_callback_table,
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
