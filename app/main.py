import os
import sys
from struct import unpack
# from dataclasses import dataclass

# import sqlparse - available if you need it!

database_file_path = sys.argv[1]
command = sys.argv[2]

if command == ".dbinfo":
    with open(database_file_path, "rb") as database_file:
        database_file.seek(16)  # Skip the first 16 bytes of the header
        page_size = int.from_bytes(database_file.read(2), byteorder="big")
        print(f"database page size: {page_size}")

        database_file.seek(100, os.SEEK_SET)
        page_header = database_file.read(8)
        _, _, num_cells, _, _ = unpack(">BHHHB", page_header)
        print(f"number of tables: {num_cells}")

else:
    print(f"Invalid command: {command}")
