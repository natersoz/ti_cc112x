"""
make_registers.py

From the yaml file, create a header file use when accessing devices
over an bus.
"""

import pprint
import argparse
import yaml

import print_types_c


def main():
    """
    'registers':
    {
        'SENSORBUS_ADDR':
        {
            {'brief': 'Address on sensor to read/write'},
            {'access': 'read-write'},
            {'address': "0x2111'2001"},
            {'fields': {'address': {'pos': 0}, {'bits': 8}}}
        },
    """
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "--file", "-f", type=str,
        help="The register yaml file to generate C header files from",
        required=True)

    args = arg_parser.parse_args()
#    print(f"YAML file: {args.file}")

    with open(args.file, mode="r", encoding="utf_8") as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)

        print_types_c.print_enums(yaml_data['types'])

        register_dict = yaml_data['registers']

        # Convert address strings to integer values
        for key, value in register_dict.items():
            if isinstance(value['address'], str):
                hex_str = value['address'].replace("'", "")
                value['address'] = int(hex_str, 16)

        # pprint.pprint(yaml_data)

if __name__ == '__main__':
    main()
