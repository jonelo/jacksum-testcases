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

testcases = [
    {
		"desc":     "Version of Jacksum",
		"args":     [ "--version" ],
		"expected": "Jacksum 3.7.0"
	},
	{
  		"desc":		"algo=SHA-1, encoding=hex lowercase, input=0-9",
  		"args":		[ "-a", "sha1", "-x", "-q", "txt:0123456789" ],
  		"expected": "87acec17cd9dcd20a716cc2cf67417b71c8a7016"
	},
	{
  		"desc":		"algo=SHA-1, encoding=hex uppercase, input=0-9",
  		"args":		[ "-a", "sha1", "-X", "-q", "txt:0123456789" ],
  		"expected": "87ACEC17CD9DCD20A716CC2CF67417B71C8A7016"
	},
	{
		"desc":		"algo=FNV-1a_32, enoding=hex lowercase, input=0-9",
		"args":		[ "-a", "fnv-1a_32", "-x", "-q", "txt:0123456789" ],
		"expected":	"f9808ff2 10"
	},
	{
		"desc":		"Jacksum as hex dumper",
		"args":		[ "-a", "none", "-x", "-F", "#SEQUENCE", "-q", "file:samples/hello-world-windows.txt" ],
		"expected":	"48656c6c6f20576f726c64200d0a"
	},
	{
		"desc":		"-a all:blake -l",
		"args":		[ "-a", "all:blake", "-l" ],
		"expected":	"blake224"
	}

]


def get():
	return testcases
