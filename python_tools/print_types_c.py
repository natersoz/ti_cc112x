"""
Given a yaml constructed dictionary, print C header files of types.
"""

import os

C_SINGLE_LINE_COMMENT_PREFIX = "/// "
C_MULTI_LINE_COMMENT_PREFIX  = "/**"
C_MULTI_LINE_COMMENT_SUFFIX  = " */"

def print_comment_single_line(comment, indent):
    """
    Print a single line comment.
    """
    print(" " * indent, C_SINGLE_LINE_COMMENT_PREFIX, f"{comment.strip(os.linesep)}")


def print_comment_multi_line(comment, indent):
    """
    Print a multiple line comment.
    """
    line_count = comment.count(os.linesep)
    comment_lines = comment.split(os.linesep)
    print(" " * indent, C_MULTI_LINE_COMMENT_PREFIX)
    for line in comment_lines:
        # Don't print lines that are zero length.
        if len(line) > 0:
            print(" " * indent, " *", f"{line}")
    print(" " * indent, C_MULTI_LINE_COMMENT_SUFFIX)


def print_comment(comment, indent):
    """
    Print a C comment.
    """
    line_count = comment.count(os.linesep)
    if line_count < 2:
        print_comment_single_line(comment, indent)
    else:
        print_comment_multi_line(comment, indent)


def print_enums(types_list):
    """
    format:
    [
        {'enum':
            {'GPIO_CONFIG',
                'values':
                {
                        'ADC_DATA_TEST': {'description': 'ADC data, test purposes only.\n',
                                        'value': 46},
                        'ANTENNA_SELECT': {'description': 'Antenna diversity control.\n',
                                        'value': 36},
                        ...
                    }
            },
        ...
        },
        {'enum' : ...}
        ...
    ]
    """
    for the_type in types_list:
        if "enum" in the_type.keys():
            print(f"enum {the_type['enum']}")
            if "values" in the_type.keys():
                print("{")
                indent = 4
                for key, value in the_type["values"].items():
                    if "description" in value.keys():
                        # import pdb; pdb.set_trace()
                        print_comment(value['description'], 4)
                    if "value" in value.keys():
                        print(" " * indent, f"{key} = {value['value']},")
                    else:
                        print(" " * indent, f"{key},")

                print("};")
