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


def write_enum(ys: list):

    print(
        ENUM_HEAD.format(
            prefix=RABBITIZER_TYPE_PREFIX,
            name="InstrId",
        )
    )
    entry_prefix = RABBITIZER_ENUM_VARIANT_PREFIX + "_" + "INSTR_ID"

    i = 0
    for y in ys:
        for instr_set in y["instruction_sets"]:
            set_name = instr_set["set"]  # e.g. core
            for cl in instr_set["classes"]:  # e.g. regimm, may not have a "class" name
                class_instructions = cl["instructions"]
                for entry in class_instructions:  # actual instruction data
                    variant = set_name + "_" + entry["name"]
                    print(
                        ENUM_FULL_ENTRY.format(
                            enum_entry_prefix=entry_prefix,
                            variant=variant.upper(),
                            number=i,
                        )
                    )
                    i += 1

    print(
        ENUM_FOOT.format(
            prefix=RABBITIZER_TYPE_PREFIX,
            name="InstrId",
        )
    )


# C tables
TABLE_ENTRY_START = "    [" + ENUM_NAME + "] = "
TABLE_FOOT = """
}};
"""


NAME_TABLE_HEAD = """
const {ctype} {prefix}{name}_Names[] {{
"""


def write_name_table(ys):
    ctype = "char*"
    print(
        NAME_TABLE_HEAD.format(
            ctype=ctype,
            prefix=RABBITIZER_TYPE_PREFIX,
            name="InstrId",
        )
    )
    entry_prefix = RABBITIZER_ENUM_VARIANT_PREFIX + "_" + "INSTR_ID"
    i = 0
    for y in ys:
        for instr_set in y["instruction_sets"]:
            set_name = instr_set["set"]  # e.g. core
            for cl in instr_set["classes"]:  # e.g. regimm, may not have a "class" name
                class_instructions = cl["instructions"]
                for entry in class_instructions:  # actual instruction data
                    variant = set_name + "_" + entry["name"]
                    print(
                        TABLE_ENTRY_START.format(
                            enum_entry_prefix=entry_prefix,
                            variant=variant.upper(),
                        ),
                        end="",
                    )
                    # name string
                    if cl.get("class", "") != "userdef":
                        display_name = (
                            entry["name"].replace("_", ".").replace("sn64_", "")
                        )
                    else:
                        display_name = entry["name"]
                    print(f'"{display_name}",')

    print(TABLE_FOOT.format())


DESCRIPTOR_TABLE_HEAD = """
const {ctype} {prefix}_{name}_Descriptors[] {{
"""


def write_descriptor_table(ys):
    ctype = RABBITIZER_TYPE_PREFIX + "Instr" + "Descriptor"
    print(
        DESCRIPTOR_TABLE_HEAD.format(
            ctype=ctype,
            prefix=RABBITIZER_TYPE_PREFIX,
            name="Instr",
        )
    )
    entry_prefix = RABBITIZER_ENUM_VARIANT_PREFIX + "_" + "INSTR_ID"
    i = 0
    for y in ys:
        for instr_set in y["instruction_sets"]:
            set_name = instr_set["set"]  # e.g. core
            for cl in instr_set["classes"]:  # e.g. regimm, may not have a "class" name
                class_instructions = cl["instructions"]
                for entry in class_instructions:  # actual instruction data
                    variant = set_name + "_" + entry["name"]
                    print(
                        TABLE_ENTRY_START.format(
                            enum_entry_prefix=entry_prefix,
                            variant=variant.upper(),
                        ),
                        end="",
                    )
                    print("{ ", end="")
                    columns_list = []
                    for k, v in entry.items():
                        if k in ["name", "numeric", "index", "mnemonic"]:
                            continue
                        if k == "operands":
                            if len(v) != 0:
                                columns_list.append(
                                    ".{}={{ {} }}".format(
                                        k, ", ".join([f"RAB_OPERAND_{s}" for s in v])
                                    )
                                )
                            else:
                                columns_list.append(".{}={{ {} }}".format(k, "0"))
                        else:
                            # replace Pythonic truth by C truth
                            columns_list.append(f".{k}={v}".replace("=True", "=true"))

                    columns_str = ", ".join(columns_list)
                    print(columns_str if columns_str else "0", end="")
                    print(" },")
    print(TABLE_FOOT.format())


LOOKUP_TABLE_HEAD = """
const {ctype} {prefix}_{name}_ToId[] {{
"""


def write_lookup_tables(ys):
    for y in ys:
        entry_prefix = RABBITIZER_ENUM_VARIANT_PREFIX + "_" + "INSTR_ID"
        for instr_set in y["instruction_sets"]:

            set_name = instr_set["set"]  # e.g. core
            for cl in instr_set["classes"]:  # e.g. regimm, may not have a "class" name
                if not cl.get("class"):
                    continue
                ctype = "{prefix}{name}".format(
                    prefix=RABBITIZER_TYPE_PREFIX,
                    name="InstrId",
                )
                print(
                    LOOKUP_TABLE_HEAD.format(
                        ctype=ctype,
                        prefix=RABBITIZER_TYPE_PREFIX,
                        name=set_name + "_" + cl["class"],
                    )
                )

                class_instructions = cl["instructions"]
                for entry in class_instructions:  # actual instruction data
                    index = entry.get("index")
                    if not index or index < 0:
                        continue
                    variant = set_name + "_" + entry["name"]
                    enum_variant = ENUM_NAME.format(
                        enum_entry_prefix=entry_prefix,
                        variant=variant.upper(),
                    )
                    print(
                        "     [0x{index:02X}] = {enum_variant},".format(
                            index=entry["index"],
                            enum_variant=enum_variant,
                        )
                    )

                print(TABLE_FOOT.format())


MODE_SELECT = {
    "enum": write_enum,
    "desc": write_descriptor_table,
    "names": write_name_table,
    "lookup": write_lookup_tables,
}


def print_usage():
    print(
        f"""USAGE: {sys.argv[0]} MODE FILE1 FILE2 ...
where MODE is one of 
- `enum` to write an enumeration
- `desc` to write an array of descriptions
- `names` to write an array of names
"""
    )


def main() -> None:
    if len(sys.argv) < 3:
        print_usage()
        exit(1)

    mode = sys.argv[1]
    if mode not in MODE_SELECT:
        print(
            f"specified mode `{mode}` is not a valid mode, should be one of \n    {', '.join(MODE_SELECT)}",
            file=sys.stderr,
        )

    infiles = sys.argv[2:]
    file_count = len(infiles)
    if file_count > 10:
        print(
            "Too many files specified, (arbitrary) upper limit is 10", file=sys.stderr
        )
        exit(1)

    ys = []

    for file in infiles:
        with open(file) as f:
            ys.append(yaml.load(f, Loader=yaml.SafeLoader))
    # print(ys)

    write_file_description()

    MODE_SELECT[mode](ys)

    # for y in ys:
    #     for name, data in y.items():
    #         MODE_SELECT[mode](name, data)


if __name__ == "__main__":
    main()
