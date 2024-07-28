# MIT License
#
# Copyright (c) 2024 Johann N. Loefflmann, https://johann.loefflmann.net
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

# init constants
DATABASE_REMOTE = 'https://reveng.sourceforge.io/crc-catalogue/all.htm'
DATABASE_LOCAL = "./crc-catalogue.html"
TESTCASES_JSON = "./testvectors/json/crc-catalogue.json"

print(f"Downloading {DATABASE_REMOTE} ...")
response = requests.get(DATABASE_REMOTE, allow_redirects=True)
with open(DATABASE_LOCAL, 'wb') as f:
    f.write(response.content)

print(f"Reading {DATABASE_LOCAL} ...")
lines = []
file = open(f"{DATABASE_LOCAL}", 'r', encoding='utf-8')
lines.extend(file.readlines())
file.close()

testcases = []
for line in lines:
    # <CODE>width=4  poly=0x3  init=0x0  refin=true  refout=true  xorout=0x0  check=0x7  residue=0x0  name="CRC-4/G-704"</CODE>
    #result = re.search(r'<CODE>width=(\d+)', line)
    regexhex = r'0[xX]([0-9a-fA-F]+)'
    regexbool = r'([trufalse]+)'
    regex = (r'<CODE>\s*'
             r'width=(\d+)\s+'
             r'poly='+regexhex+'\s+'
             r'init='+regexhex+'\s+'
             r'refin='+regexbool+'\s+'
             r'refout='+regexbool+'\s+'
             r'xorout='+regexhex+'\s+'
             r'check='+regexhex+'\s+'
             r'residue='+regexhex+'\s+'
             r'name="([^\"]+)"\s*'
             r'</CODE>'
            )
    regex2 = (r'<CODE>\s*'
              r'(width=\d+\s+'
              r'[^<]+)'
              r'</CODE>'
             )

    result = re.search(regex, line)
    if result:
        crc_def_ori = re.search(regex2, line).group(1)
        algo_name = result.group(9)
        width = result.group(1)
        check = result.group(7)

        # Jacksum does only support the generic CRC with range of [1..64]
        if width == "82" and algo_name == "CRC-82/DARC":
            crc_def_jacksum = "crc82_darc"
        else:
            crc_def_jacksum = (f"crc:{width},"
                               f"{result.group(2)},"
                               f"{result.group(3)},"
                               f"{result.group(4)},"
                               f"{result.group(5)},"
                               f"{result.group(6)}"
            )
        output = (f"{algo_name};"
                  f"{crc_def_jacksum}"
        )

        # e. g. CRC11 has a check value of 5a3, this has an odd number of nibbles,
        # we prepend a 0 to make the hex string a multiple of 8 bits.
        if len(check) % 2 > 0:
            check = "0"+check
        obj = {
                'desc': f"{crc_def_ori}",
                        'args': ["-a", f"{crc_def_jacksum}",
                                 "-q", f"txt:123456789",
                                 "-E", f"hex",
                                 "-F", f"#CHECKSUM"
                                 ],
                        # 'msg': f"{msg}",
                        'expected': check
        }
        testcases.append(obj)
        print (output)

print(f"Writing {TESTCASES_JSON} ...")
with open(TESTCASES_JSON, 'w', encoding='utf-8') as file:
    json.dump(testcases, file, indent=4)
    file.close()

print(f"Removing {DATABASE_LOCAL} ...")
if os.path.exists(DATABASE_LOCAL):
    os.remove(DATABASE_LOCAL)

