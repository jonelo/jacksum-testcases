# MIT License
#
# Copyright (c) 2023 Johann N. Loefflmann, https://johann.loefflmann.net
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

import general_testcases
import hmac_testcases

# user init
APP = [ "java", "-jar", "c:/Users/Johann/IdeaProjects/jacksum/target/jacksum-3.7.0.jar" ]


# test cases
testcases = []
testcases += general_testcases.get()
testcases += hmac_testcases.get()

allTestcases = 0

statistics = {
	"passed": 0,
	"failed": 0
}

def testcase(testcase, statistics):
	print (f"Test: {testcase['desc']}")
	print (f"Args: {testcase['args']}")
	try:
		ARGS = 0
		OUTPUT = 1
		process = subprocess.run(APP + testcase['args'],
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			universal_newlines=True,
			timeout = 5)

		actual = process.stdout.strip()
		actual_stderr = process.stderr.strip()
		expected = testcase['expected']
		if actual == expected:
			print (f"stdout:   {actual}")
			print (f"PASSED\n")
			statistics['passed'] += 1
		elif actual.partition('\n')[0] == expected:
			print (f"stdout:   {actual}")
			print (f"stderr:   {actual_stderr}")
			print (f"Expected: {expected}")
			print (f"PASSED (first line only)\n")
			statistics['passed'] += 1
		else:
			print (f"stdout:   {actual}")
			print (f"stderr:   {actual_stderr}")
			print (f"Expected: {expected}")
			print (f"FAILED\n")
			statistics['failed'] += 1

	except subprocess.TimoutExpired:
		print (f"Timeout expired.")
		print (f"FAILED\n")
		statistics['failed'] += 1

# all testcases
for case in testcases:
	allTestcases += 1
	testcase(case, statistics)

print (f"Result: {statistics}")
