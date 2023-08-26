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


# Test Cases from
# https://www.rfc-editor.org/rfc/rfc4231
# Section 4. Test Vectors

testcases = [

# Test Case 1
	{
	    "desc":     "RFC 4231, Test Case 1, HMAC-SHA-224",
	    "args":     [ "-a", "hmac:sha224",
	                  "-k", "hex:0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b",
	                  "-q", "hex:4869205468657265", # "Hi There"
	                  "-E", "hex"
	                ],
	    "expected": "896fb1128abbdf196832107cd49df33f"
	                "47b4b1169912ba4f53684b22"
	},
	{
	    "desc":     "RFC 4231, Test Case 1, HMAC-SHA-256",
	    "args":     [ "-a", "hmac:sha256",
	                  "-k", "hex:0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b",
	                  "-q", "hex:4869205468657265", # "Hi There"
	                  "-E", "hex"
	                ],
	    "expected": "b0344c61d8db38535ca8afceaf0bf12b"
	                "881dc200c9833da726e9376c2e32cff7"
	},
	{
	    "desc":     "RFC 4231, Test Case 1, HMAC-SHA-384",
	    "args":     [ "-a", "hmac:sha384",
	                  "-k", "hex:0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b",
	                  "-q", "hex:4869205468657265", # "Hi There"
	                  "-E", "hex"
	                ],
	    "expected": "afd03944d84895626b0825f4ab46907f"
	                "15f9dadbe4101ec682aa034c7cebc59c"
	                "faea9ea9076ede7f4af152e8b2fa9cb6"
	},
	{
	    "desc":     "RFC 4231, Test Case 1, HMAC-SHA-512",
	    "args":     [ "-a", "hmac:sha512",
	                  "-k", "hex:0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b",
	                  "-q", "hex:4869205468657265", # "Hi There"
	                  "-E", "hex"
	                ],
	    "expected": "87aa7cdea5ef619d4ff0b4241a1d6cb0"
	                "2379f4e2ce4ec2787ad0b30545e17cde"
	                "daa833b7d6b8a702038b274eaea3f4e4"
	                "be9d914eeb61f1702e696c203a126854"
	},


# Test Case 2
# Test with a key shorter than the length of the HMAC output.

	{
	    "desc":     "RFC 4231, Test Case 2, HMAC-SHA-224",
	    "args":     [ "-a", "hmac:sha224",
	                  "-k", "hex:4a656665",                        # "Jefe"
	                  "-q", "hex:7768617420646f2079612077616e7420" # "what do ya want "
	                        "666f72206e6f7468696e673f",            # "for nothing?"
	                  "-E", "hex"
	                ],
	    "expected": "a30e01098bc6dbbf45690f3a7e9e6d0f"
	                "8bbea2a39e6148008fd05e44"
	},
	{
	    "desc":     "RFC 4231, Test Case 2, HMAC-SHA-256",
	    "args":     [ "-a", "hmac:sha256",
	                  "-k", "hex:4a656665",                        # "Jefe"
	                  "-q", "hex:7768617420646f2079612077616e7420" # "what do ya want "
	                        "666f72206e6f7468696e673f",            # "for nothing?"
	                  "-E", "hex"
	                ],
	    "expected": "5bdcc146bf60754e6a042426089575c7"
	                "5a003f089d2739839dec58b964ec3843"
	},
	{
	    "desc":     "RFC 4231, Test Case 2, HMAC-SHA-384",
	    "args":     [ "-a", "hmac:sha384",
	                  "-k", "hex:4a656665",                        # "Jefe"
	                  "-q", "hex:7768617420646f2079612077616e7420" # "what do ya want "
	                        "666f72206e6f7468696e673f",            # "for nothing?"
	                  "-E", "hex"
	                ],
	    "expected": "af45d2e376484031617f78d2b58a6b1b"
	                "9c7ef464f5a01b47e42ec3736322445e"
	                "8e2240ca5e69e2c78b3239ecfab21649"
	},
	{
	    "desc":     "RFC 4231, Test Case 2, HMAC-SHA-512",
	    "args":     [ "-a", "hmac:sha512",
	                  "-k", "hex:4a656665",                        # "Jefe"
	                  "-q", "hex:7768617420646f2079612077616e7420" # "what do ya want "
	                        "666f72206e6f7468696e673f",            # "for nothing?"
	                  "-E", "hex"
	                ],
	    "expected": "164b7a7bfcf819e2e395fbe73b56e0a3"
	                "87bd64222e831fd610270cd7ea250554"
	                "9758bf75c05a994a6d034f65f8f0e6fd"
	                "caeab1a34d4a6b4b636e070a38bce737"
	},

# Test Case 3
# Test with a combined length of key and data that is larger than 64
# bytes (= block-size of SHA-224 and SHA-256).

	{
	    "desc":     "RFC 4231, Test Case 3, HMAC-SHA-224",
	    "args":     [ "-a", "hmac:sha224",
	                  "-k", "hex:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	                            "aaaaaaaa",
	                  "-q", "hex:dddddddddddddddddddddddddddddddd"
	                            "dddddddddddddddddddddddddddddddd"
	                            "dddddddddddddddddddddddddddddddd"
	                            "dddd",
	                  "-E", "hex"
	                ],
	    "expected": "7fb3cb3588c6c1f6ffa9694d7d6ad264"
	                "9365b0c1f65d69d1ec8333ea"
	},
	{
	    "desc":     "RFC 4231, Test Case 3, HMAC-SHA-256",
	    "args":     [ "-a", "hmac:sha256",
	                  "-k", "hex:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	                            "aaaaaaaa",
	                  "-q", "hex:dddddddddddddddddddddddddddddddd"
	                            "dddddddddddddddddddddddddddddddd"
	                            "dddddddddddddddddddddddddddddddd"
	                            "dddd",
	                  "-E", "hex"
	                ],
	    "expected": "773ea91e36800e46854db8ebd09181a7"
	                "2959098b3ef8c122d9635514ced565fe"
	},
	{
	    "desc":     "RFC 4231, Test Case 3, HMAC-SHA-384",
	    "args":     [ "-a", "hmac:sha384",
	                  "-k", "hex:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	                            "aaaaaaaa",
	                  "-q", "hex:dddddddddddddddddddddddddddddddd"
	                            "dddddddddddddddddddddddddddddddd"
	                            "dddddddddddddddddddddddddddddddd"
	                            "dddd",
	                  "-E", "hex"
	                ],
	    "expected": "88062608d3e6ad8a0aa2ace014c8a86f"
	                "0aa635d947ac9febe83ef4e55966144b"
	                "2a5ab39dc13814b94e3ab6e101a34f27"
	},
	{
	    "desc":     "RFC 4231, Test Case 3, HMAC-SHA-512",
	    "args":     [ "-a", "hmac:sha512",
	                  "-k", "hex:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	                            "aaaaaaaa",
	                  "-q", "hex:dddddddddddddddddddddddddddddddd"
	                            "dddddddddddddddddddddddddddddddd"
	                            "dddddddddddddddddddddddddddddddd"
	                            "dddd",
	                  "-E", "hex"
	                ],
	    "expected": "fa73b0089d56a284efb0f0756c890be9"
	                "b1b5dbdd8ee81a3655f83e33b2279d39"
	                "bf3e848279a722c806b485a47e67c807"
	                "b946a337bee8942674278859e13292fb"
	},


# Test Case 4
# Test with a combined length of key and data that is larger than 64
# bytes (= block-size of SHA-224 and SHA-256).

	{
	    "desc":     "RFC 4231, Test Case 4, HMAC-SHA-224",
	    "args":     [ "-a", "hmac:sha224",
	                  "-k", "hex:0102030405060708090a0b0c0d0e0f10"
	                            "111213141516171819",
	                  "-q", "hex:cdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcd"
	                            "cdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcd"
	                            "cdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcd"
	                            "cdcd",
	                  "-E", "hex"
	                ],
	    "expected": "6c11506874013cac6a2abc1bb382627c"
	                "ec6a90d86efc012de7afec5a"
	},
	{
	    "desc":     "RFC 4231, Test Case 4, HMAC-SHA-256",
	    "args":     [ "-a", "hmac:sha256",
	                  "-k", "hex:0102030405060708090a0b0c0d0e0f10"
	                            "111213141516171819",
	                  "-q", "hex:cdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcd"
	                            "cdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcd"
	                            "cdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcd"
	                            "cdcd",
	                  "-E", "hex"
	                ],
	    "expected": "82558a389a443c0ea4cc819899f2083a"
	                "85f0faa3e578f8077a2e3ff46729665b"
	},
	{
	    "desc":     "RFC 4231, Test Case 4, HMAC-SHA-384",
	    "args":     [ "-a", "hmac:sha384",
	                  "-k", "hex:0102030405060708090a0b0c0d0e0f10"
	                            "111213141516171819",
	                  "-q", "hex:cdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcd"
	                            "cdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcd"
	                            "cdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcd"
	                            "cdcd",
	                  "-E", "hex"
	                ],
	    "expected": "3e8a69b7783c25851933ab6290af6ca7"
	                "7a9981480850009cc5577c6e1f573b4e"
	                "6801dd23c4a7d679ccf8a386c674cffb"
	},
	{
	    "desc":     "RFC 4231, Test Case 4, HMAC-SHA-512",
	    "args":     [ "-a", "hmac:sha512",
	                  "-k", "hex:0102030405060708090a0b0c0d0e0f10"
	                            "111213141516171819",
	                  "-q", "hex:cdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcd"
	                            "cdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcd"
	                            "cdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcd"
	                            "cdcd",
	                  "-E", "hex"
	                ],
	    "expected": "b0ba465637458c6990e5a8c5f61d4af7"
	                "e576d97ff94b872de76f8050361ee3db"
	                "a91ca5c11aa25eb4d679275cc5788063"
	                "a5f19741120c4f2de2adebeb10a298dd"
	},

# Test Case 5
#
# Test with a truncation of output to 128 bits.

	{
	    "desc":     "RFC 4231, Test Case 5, HMAC-SHA-224-128",
	    "args":     [ "-a", "hmac:sha224:128",
	                  "-k", "hex:0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c"
	                            "0c0c0c0c",
	                  "-q", "hex:546573742057697468205472756e6361" # "Test With Trunca""
	                            "74696f6e",                        # "tion"
	                  "-E", "hex"
	                ],
	    "expected": "0e2aea68a90c8d37c988bcdb9fca6fa8"
	},
	{
	    "desc":     "RFC 4231, Test Case 5, HMAC-SHA-256-128",
	    "args":     [ "-a", "hmac:sha256:128",
	                  "-k", "hex:0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c"
	                            "0c0c0c0c",
	                  "-q", "hex:546573742057697468205472756e6361" # "Test With Trunca""
	                            "74696f6e",                        # "tion"
	                  "-E", "hex"
	                ],
	    "expected": "a3b6167473100ee06e0c796c2955552b"
	},
	{
	    "desc":     "RFC 4231, Test Case 5, HMAC-SHA-384-128",
	    "args":     [ "-a", "hmac:sha384:128",
	                  "-k", "hex:0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c"
	                            "0c0c0c0c",
	                  "-q", "hex:546573742057697468205472756e6361" # "Test With Trunca""
	                            "74696f6e",                        # "tion"
	                  "-E", "hex"
	                ],
	    "expected": "3abf34c3503b2a23a46efc619baef897"
	},
	{
	    "desc":     "RFC 4231, Test Case 5, HMAC-SHA-512-128",
	    "args":     [ "-a", "hmac:sha512:128",
	                  "-k", "hex:0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c"
	                            "0c0c0c0c",
	                  "-q", "hex:546573742057697468205472756e6361" # "Test With Trunca""
	                            "74696f6e",                        # "tion"
	                  "-E", "hex"
	                ],
	    "expected": "415fad6271580a531d4179bc891d87a6"
	},


# Test Case 6
#
# Test with a key larger than 128 bytes (= block-size of SHA-384 and
# SHA-512).

	{
	    "desc":     "RFC 4231, Test Case 6, HMAC-SHA-224",
	    "args":     [ "-a", "hmac:sha224",
	                  "-k", "hex:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaa",
	                  "-q", "hex:54657374205573696e67204c61726765" # "Test Using Large"
	                            "72205468616e20426c6f636b2d53697a" # "r Than Block-Siz"
	                            "65204b6579202d2048617368204b6579" # "e Key - Hash Key"
	                            "204669727374",                    # " First"
	                  "-E", "hex"
	                ],
	    "expected": "95e9a0db962095adaebe9b2d6f0dbce2"
	                "d499f112f2d2b7273fa6870e"
	},
	{
	    "desc":     "RFC 4231, Test Case 6, HMAC-SHA-256",
	    "args":     [ "-a", "hmac:sha256",
	                  "-k", "hex:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaa",
	                  "-q", "hex:54657374205573696e67204c61726765" # "Test Using Large"
	                            "72205468616e20426c6f636b2d53697a" # "r Than Block-Siz"
	                            "65204b6579202d2048617368204b6579" # "e Key - Hash Key"
	                            "204669727374",                    # " First"
	                  "-E", "hex"
	                ],
	    "expected": "60e431591ee0b67f0d8a26aacbf5b77f"
	                "8e0bc6213728c5140546040f0ee37f54"
	},
	{
	    "desc":     "RFC 4231, Test Case 6, HMAC-SHA-384",
	    "args":     [ "-a", "hmac:sha384",
	                  "-k", "hex:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaa",
	                  "-q", "hex:54657374205573696e67204c61726765" # "Test Using Large"
	                            "72205468616e20426c6f636b2d53697a" # "r Than Block-Siz"
	                            "65204b6579202d2048617368204b6579" # "e Key - Hash Key"
	                            "204669727374",                    # " First"
	                  "-E", "hex"
	                ],
	    "expected": "4ece084485813e9088d2c63a041bc5b4"
	                "4f9ef1012a2b588f3cd11f05033ac4c6"
	                "0c2ef6ab4030fe8296248df163f44952"
	},
	{
	    "desc":     "RFC 4231, Test Case 6, HMAC-SHA-512",
	    "args":     [ "-a", "hmac:sha512",
	                  "-k", "hex:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaa",
	                  "-q", "hex:54657374205573696e67204c61726765" # "Test Using Large"
	                            "72205468616e20426c6f636b2d53697a" # "r Than Block-Siz"
	                            "65204b6579202d2048617368204b6579" # "e Key - Hash Key"
	                            "204669727374",                    # " First"
	                  "-E", "hex"
	                ],
	    "expected": "80b24263c7c1a3ebb71493c1dd7be8b4"
	                "9b46d1f41b4aeec1121b013783f8f352"
	                "6b56d037e05f2598bd0fd2215d6a1e52"
	                "95e64f73f63f0aec8b915a985d786598"
	},

# Test Case 7
#
# Test with a key and data that is larger than 128 bytes (= block-size
# of SHA-384 and SHA-512).

	{
	    "desc":     "RFC 4231, Test Case 7, HMAC-SHA-224",
	    "args":     [ "-a", "hmac:sha224",
	                  "-k", "hex:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaa",
	                  "-q", "hex:54686973206973206120746573742075" # "This is a test u"
	                            "73696e672061206c6172676572207468" # "sing a larger th"
	                            "616e20626c6f636b2d73697a65206b65" # "an block-size ke"
	                            "7920616e642061206c61726765722074" # "y and a larger t"
	                            "68616e20626c6f636b2d73697a652064" # "han block-size d"
	                            "6174612e20546865206b6579206e6565" # "ata. The key nee"
	                            "647320746f2062652068617368656420" # "ds to be hashed "
	                            "6265666f7265206265696e6720757365" # "before being use"
	                            "642062792074686520484d414320616c" # "d by the HMAC al"
	                            "676f726974686d2e",                # "gorithm."
	                  "-E", "hex"
	                ],
	    "expected": "3a854166ac5d9f023f54d517d0b39dbd"
	                "946770db9c2b95c9f6f565d1"
	},
	{
	    "desc":     "RFC 4231, Test Case 7, HMAC-SHA-256",
	    "args":     [ "-a", "hmac:sha256",
	                  "-k", "hex:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaa",
	                  "-q", "hex:54686973206973206120746573742075" # "This is a test u"
	                            "73696e672061206c6172676572207468" # "sing a larger th"
	                            "616e20626c6f636b2d73697a65206b65" # "an block-size ke"
	                            "7920616e642061206c61726765722074" # "y and a larger t"
	                            "68616e20626c6f636b2d73697a652064" # "han block-size d"
	                            "6174612e20546865206b6579206e6565" # "ata. The key nee"
	                            "647320746f2062652068617368656420" # "ds to be hashed "
	                            "6265666f7265206265696e6720757365" # "before being use"
	                            "642062792074686520484d414320616c" # "d by the HMAC al"
	                            "676f726974686d2e",                # "gorithm."
	                  "-E", "hex"
	                ],
	    "expected": "9b09ffa71b942fcb27635fbcd5b0e944"
	                "bfdc63644f0713938a7f51535c3a35e2"
	},
	{
	    "desc":     "RFC 4231, Test Case 7, HMAC-SHA-384",
	    "args":     [ "-a", "hmac:sha384",
	                  "-k", "hex:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaa",
	                  "-q", "hex:54686973206973206120746573742075" # "This is a test u"
	                            "73696e672061206c6172676572207468" # "sing a larger th"
	                            "616e20626c6f636b2d73697a65206b65" # "an block-size ke"
	                            "7920616e642061206c61726765722074" # "y and a larger t"
	                            "68616e20626c6f636b2d73697a652064" # "han block-size d"
	                            "6174612e20546865206b6579206e6565" # "ata. The key nee"
	                            "647320746f2062652068617368656420" # "ds to be hashed "
	                            "6265666f7265206265696e6720757365" # "before being use"
	                            "642062792074686520484d414320616c" # "d by the HMAC al"
	                            "676f726974686d2e",                # "gorithm."
	                  "-E", "hex"
	                ],
	    "expected": "6617178e941f020d351e2f254e8fd32c"
	                "602420feb0b8fb9adccebb82461e99c5"
	                "a678cc31e799176d3860e6110c46523e"
	},
	{
	    "desc":     "RFC 4231, Test Case 7, HMAC-SHA-512",
	    "args":     [ "-a", "hmac:sha512",
	                  "-k", "hex:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	                            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                "aaaaaa",
	                  "-q", "hex:54686973206973206120746573742075" # "This is a test u"
	                            "73696e672061206c6172676572207468" # "sing a larger th"
	                            "616e20626c6f636b2d73697a65206b65" # "an block-size ke"
	                            "7920616e642061206c61726765722074" # "y and a larger t"
	                            "68616e20626c6f636b2d73697a652064" # "han block-size d"
	                            "6174612e20546865206b6579206e6565" # "ata. The key nee"
	                            "647320746f2062652068617368656420" # "ds to be hashed "
	                            "6265666f7265206265696e6720757365" # "before being use"
	                            "642062792074686520484d414320616c" # "d by the HMAC al"
	                            "676f726974686d2e",                # "gorithm."
	                  "-E", "hex"
	                ],
	    "expected": "e37b6a775dc87dbaa4dfa9f96e5e3ffd"
	                "debd71f8867289865df5a32d20cdc944"
	                "b6022cac3c4982b10d5eeb55c3e4de15"
	                "134676fb6de0446065c97440fa8c6a58"
	},

]

def get():
	return testcases