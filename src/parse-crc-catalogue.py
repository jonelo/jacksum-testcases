# MIT License
#
# Copyright (c) 2024-2025 Johann N. Loefflmann, https://johann.loefflmann.net
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Reads the html page https://reveng.sourceforge.io/crc-catalogue/all.htm
# gets all crc definitions, and creates:
# - crc-catalogue.json: a json, containing testcases for Jacksum
# - on stdout: crc definitions for Jacksum's feature to find algorithms

import requests
import re
import os
import json

# Constants
DATABASE_REMOTE = 'https://reveng.sourceforge.io/crc-catalogue/all.htm'
DATABASE_LOCAL = "./crc-catalogue.html"
TESTCASES_JSON = "./testvectors/json/crc-catalogue.json"

# Regex definitions
REGEXHEX  = r'0[xX]([0-9a-fA-F]+)'     # Hex with 0x/0X-Prefix
REGEXBOOL = r'(true|false)'            # Boolean-values

CRC_PATTERN = re.compile(fr'''
    <CODE>\s*
    width=(\d+)\s+
    poly={REGEXHEX}\s+
    init={REGEXHEX}\s+
    refin={REGEXBOOL}\s+
    refout={REGEXBOOL}\s+
    xorout={REGEXHEX}\s+
    check={REGEXHEX}\s+
    residue={REGEXHEX}\s+
    name="([^"]+)"\s*
    </CODE>
''', re.VERBOSE | re.IGNORECASE)

CRC_ORIGINAL_PATTERN = re.compile(r'''
    <CODE>\s*
    (width=\d+\s+[^<]+)
    </CODE>
''', re.VERBOSE | re.IGNORECASE)

# Download html database
print(f"Downloading {DATABASE_REMOTE} ...")
response = requests.get(DATABASE_REMOTE, allow_redirects=True)
with open(DATABASE_LOCAL, 'wb') as f:
    f.write(response.content)

# Read lines
print(f"Reading {DATABASE_LOCAL} ...")
with open(DATABASE_LOCAL, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    f.close()

# Helper function
def parse_crc_line(line):
    match = CRC_PATTERN.search(line)
    if not match:
        return None

    crc_def_ori = CRC_ORIGINAL_PATTERN.search(line).group(1)
    width = match.group(1)
    algo_name = match.group(9)
    check = match.group(7)

    # Jacksum does only support the generic CRC with range of [1..64]
    if width == "82" and algo_name == "CRC-82/DARC":
        crc_def_jacksum = "crc82_darc"
    else:
        crc_def_jacksum = f"crc:{width}," + ",".join([
            match.group(2),  # poly
            match.group(3),  # init
            match.group(4),  # refin
            match.group(5),  # refout
            match.group(6)   # xorout
        ])

    # The output on stdout is for the "net/jacksum/actions/findalgo/engines/crc-catalogue.txt"
    print(f"{algo_name};{crc_def_jacksum}")

    # e. g. CRC11 has a check value of 5a3, this has an odd number of nibbles,
    # we prepend a 0 to make the hex string a multiple of 8 bits.
    if len(check) % 2 != 0:
        check = "0" + check

    return {
        'desc': crc_def_ori,
        'args': [
            "-a", crc_def_jacksum,
            "-q", "txt:123456789",
            "-E", "hex",
            "-F", "#CHECKSUM"
        ],
        'expected': check,
        #'name': algo_name  # optional, for debugging
    }


# Build testcases
testcases = []
for line in lines:
    # Example line:
    # <CODE>width=4  poly=0x3  init=0x0  refin=true  refout=true  xorout=0x0  check=0x7  residue=0x0  name="CRC-4/G-704"</CODE>
    result = parse_crc_line(line)
    if result:
        testcases.append(result)
        #print(f"{result['name']};{result['args'][1]}")

# Write output
print(f"Writing {TESTCASES_JSON} ...")
with open(TESTCASES_JSON, 'w', encoding='utf-8') as f:
    json.dump(testcases, f, indent=4)
    f.close()

# Cleanup
print(f"Removing {DATABASE_LOCAL} ...")
os.remove(DATABASE_LOCAL)