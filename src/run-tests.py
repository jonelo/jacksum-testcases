# MIT License
#
# Copyright (c) 2023-2024 Johann N. Loefflmann, https://johann.loefflmann.net
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

import subprocess
import json

# locations of the testvectors
from testvectors.lib import general_testcases
from testvectors.lib import hmac_testcases

TESTVECTORS_JSON = 'testvectors/json'

# user init
APP = ["java", "-jar", "jacksum-3.7.0.jar"]
TEST_ALGOS = [
    # SHA3 family
    'sha3-224', 'sha3-256', 'sha3-384', 'sha3-512',
    # All 3rd round candidates of the NIST SHA-3 competition
    'blake-224', 'blake-256', 'blake-384', 'blake-512',
    'groestl-224', 'groestl-256', 'groestl-384', 'groestl-512',
    'jh-224', 'jh-256', 'jh-384', 'jh-512',
    'keccak-224', 'keccak-256', 'keccak-384', 'keccak-512',
    # the testvectors submitted to the NIST competition use an internal state of 512 bits
    'skein-512-224', 'skein-512-256', 'skein-512-384', 'skein-512-512',
    # Some 2nd round candidates of the NIST SHA-3 competition
    'echo-224', 'echo-256', 'echo-384', 'echo-512',
    'fugue-224', 'fugue-256', 'fugue-384', 'fugue-512',
    'luffa-224', 'luffa-256', 'luffa-384', 'luffa-512'
]


def read_testcases_from_json(filename):
    with open(filename) as json_file:
        return json.load(json_file)


# test cases
testcases = []
testcases.extend(general_testcases.get())
testcases.extend(hmac_testcases.get())

for algo in TEST_ALGOS:
    testcases += read_testcases_from_json(f'{TESTVECTORS_JSON}/{algo}.json')
    pass

counter = 0

statistics = {
    "passed": 0,
    "failed": []
}


def testcase(counter, testcase, statistics):
    print(f"Test #{counter}: {testcase['desc']}")
    print(f"Args: {testcase['args']}")
    try:
        process = subprocess.run(APP + testcase['args'],
                                 stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 universal_newlines=True,
                                 timeout=5)

        actual = process.stdout.strip()
        actual_stderr = process.stderr.strip()
        expected = testcase['expected']
        if actual == expected:
            print(f"stdout:   {actual}")
            print(f"PASSED\n")
            statistics['passed'] += 1
        elif actual.partition('\n')[0] == expected:
            print(f"stdout:   {actual}")
            print(f"stderr:   {actual_stderr}")
            print(f"Expected: {expected}")
            print(f"PASSED (first line only)\n")
            statistics['passed'] += 1
        else:
            print(f"stdout:   {actual}")
            print(f"stderr:   {actual_stderr}")
            print(f"Expected: {expected}")
            print(f"FAILED\n")
            statistics['failed'].extend([counter])

    except subprocess.TimoutExpired:
        print(f"Timeout expired.")
        print(f"FAILED\n")
        statistics['failed'].extend([counter])


# perform all testcases
for case in testcases:
    counter += 1
    testcase(counter, case, statistics)

# print some statistics and summary
print(f"Result: {statistics}")
if len(statistics['failed']) == 0:
    print(f"ALL PASSED :)\n")
else:
    sum = len(statistics['failed'])
    if sum == 1:
        plural = ""
    else:
        plural = "s"
    print(f"{sum} testcase{plural} FAILED :(")
