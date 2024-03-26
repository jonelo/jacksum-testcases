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

# Converts a NIST .rsp file or a text file stored in CAVS format to json.

import json
import sys

ERROR = 'ERROR'
WARNING = 'WARNING'
RAW_DIR = 'testvectors/raw/algorithms/'

# SHA-3 final
NIST_SHA3_FILES_224 = ['SHA3_224ShortMsg.rsp', 'SHA3_224LongMsg.rsp']
NIST_SHA3_FILES_256 = ['SHA3_256ShortMsg.rsp', 'SHA3_256LongMsg.rsp']
NIST_SHA3_FILES_384 = ['SHA3_384ShortMsg.rsp', 'SHA3_384LongMsg.rsp']
NIST_SHA3_FILES_512 = ['SHA3_512ShortMsg.rsp', 'SHA3_512LongMsg.rsp']

# SHA-3 Competition (NIST)
NIST_SHA3_COMPETITION_FILES_224 = ['ShortMsgKAT_224.txt', 'LongMsgKAT_224.txt']
NIST_SHA3_COMPETITION_FILES_256 = ['ShortMsgKAT_256.txt', 'LongMsgKAT_256.txt']
NIST_SHA3_COMPETITION_FILES_384 = ['ShortMsgKAT_384.txt', 'LongMsgKAT_384.txt']
NIST_SHA3_COMPETITION_FILES_512 = ['ShortMsgKAT_512.txt', 'LongMsgKAT_512.txt']

# Lightweight Cryptography (NIST)
NIST_LWC_COMPETITION_2023 = ['LWC_HASH_KAT_256.txt']

testvectors_in_textfiles = [

    ### SHA3 family, final, official ###

    # https://csrc.nist.gov/CSRC/media/Projects/Cryptographic-Algorithm-Validation-Program/documents/sha3/sha-3bytetestvectors.zip
    {'algo': 'sha3-224', 'dir': RAW_DIR + 'sha3', 'files': NIST_SHA3_FILES_224},
    {'algo': 'sha3-256', 'dir': RAW_DIR + 'sha3', 'files': NIST_SHA3_FILES_256},
    {'algo': 'sha3-384', 'dir': RAW_DIR + 'sha3', 'files': NIST_SHA3_FILES_384},
    {'algo': 'sha3-512', 'dir': RAW_DIR + 'sha3', 'files': NIST_SHA3_FILES_512},

    ### NIST SHA-3 competition: 3rd round candidates ###

    # BLAKE, final round of the NIST SHA-3 competition
    # https://web.archive.org/web/20170812201530/http://csrc.nist.gov/groups/ST/hash/sha-3/Round3/documents/Blake_FinalRnd.zip
    {'algo': 'blake-224', 'dir': RAW_DIR + 'blake', 'files': NIST_SHA3_COMPETITION_FILES_224},
    {'algo': 'blake-256', 'dir': RAW_DIR + 'blake', 'files': NIST_SHA3_COMPETITION_FILES_256},
    {'algo': 'blake-384', 'dir': RAW_DIR + 'blake', 'files': NIST_SHA3_COMPETITION_FILES_384},
    {'algo': 'blake-512', 'dir': RAW_DIR + 'blake', 'files': NIST_SHA3_COMPETITION_FILES_512},

    # Groestl, final round of the NIST SHA-3 competition
    # https://web.archive.org/web/20170812201530/http://csrc.nist.gov/groups/ST/hash/sha-3/Round3/documents/Groestl_FinalRnd.zip
    {'algo': 'groestl-224', 'dir': RAW_DIR + 'groestl', 'files': NIST_SHA3_COMPETITION_FILES_224},
    {'algo': 'groestl-256', 'dir': RAW_DIR + 'groestl', 'files': NIST_SHA3_COMPETITION_FILES_256},
    {'algo': 'groestl-384', 'dir': RAW_DIR + 'groestl', 'files': NIST_SHA3_COMPETITION_FILES_384},
    {'algo': 'groestl-512', 'dir': RAW_DIR + 'groestl', 'files': NIST_SHA3_COMPETITION_FILES_512},

    # JH, final round of the NIST SHA-3 competition
    # https://web.archive.org/web/20170812201530/http://csrc.nist.gov/groups/ST/hash/sha-3/Round3/documents/JH_FinalRnd.zip
    {'algo': 'jh-224', 'dir': RAW_DIR + 'jh', 'files': NIST_SHA3_COMPETITION_FILES_224},
    {'algo': 'jh-256', 'dir': RAW_DIR + 'jh', 'files': NIST_SHA3_COMPETITION_FILES_256},
    {'algo': 'jh-384', 'dir': RAW_DIR + 'jh', 'files': NIST_SHA3_COMPETITION_FILES_384},
    {'algo': 'jh-512', 'dir': RAW_DIR + 'jh', 'files': NIST_SHA3_COMPETITION_FILES_512},

    # Keccak, final round of the NIST SHA-3 competition
    # https://web.archive.org/web/20170812201530/http://csrc.nist.gov/groups/ST/hash/sha-3/Round3/documents/Keccak_FinalRnd.zip
    {'algo': 'keccak-224', 'dir': RAW_DIR + 'keccak', 'files': NIST_SHA3_COMPETITION_FILES_224},
    {'algo': 'keccak-256', 'dir': RAW_DIR + 'keccak', 'files': NIST_SHA3_COMPETITION_FILES_256},
    {'algo': 'keccak-384', 'dir': RAW_DIR + 'keccak', 'files': NIST_SHA3_COMPETITION_FILES_384},
    {'algo': 'keccak-512', 'dir': RAW_DIR + 'keccak', 'files': NIST_SHA3_COMPETITION_FILES_512},

    # Skein
    # https://web.archive.org/web/20170812201530/http://csrc.nist.gov/groups/ST/hash/sha-3/Round3/documents/Skein_FinalRnd.zip
    {'algo': 'skein-512-224', 'dir': RAW_DIR + 'skein', 'files': NIST_SHA3_COMPETITION_FILES_224},
    {'algo': 'skein-512-256', 'dir': RAW_DIR + 'skein', 'files': NIST_SHA3_COMPETITION_FILES_256},
    {'algo': 'skein-512-384', 'dir': RAW_DIR + 'skein', 'files': NIST_SHA3_COMPETITION_FILES_384},
    {'algo': 'skein-512-512', 'dir': RAW_DIR + 'skein', 'files': NIST_SHA3_COMPETITION_FILES_512},

    ###  NIST SHA-3 competition: 2nd round candidates ###

    # ECHO
    # https://web.archive.org/web/20170604091329/http://csrc.nist.gov/groups/ST/hash/sha-3/Round2/documents/ECHO_Round2.zip
    {'algo': 'echo-224', 'dir': RAW_DIR + 'echo', 'files': NIST_SHA3_COMPETITION_FILES_224},
    {'algo': 'echo-256', 'dir': RAW_DIR + 'echo', 'files': NIST_SHA3_COMPETITION_FILES_256},
    {'algo': 'echo-384', 'dir': RAW_DIR + 'echo', 'files': NIST_SHA3_COMPETITION_FILES_384},
    {'algo': 'echo-512', 'dir': RAW_DIR + 'echo', 'files': NIST_SHA3_COMPETITION_FILES_512},

    # Fugue
    # https://web.archive.org/web/20170604091329/http://csrc.nist.gov/groups/ST/hash/sha-3/Round2/documents/Fugue_Round2.zip
    {'algo': 'fugue-224', 'dir': RAW_DIR + 'fugue', 'files': NIST_SHA3_COMPETITION_FILES_224},
    {'algo': 'fugue-256', 'dir': RAW_DIR + 'fugue', 'files': NIST_SHA3_COMPETITION_FILES_256},
    {'algo': 'fugue-384', 'dir': RAW_DIR + 'fugue', 'files': NIST_SHA3_COMPETITION_FILES_384},
    {'algo': 'fugue-512', 'dir': RAW_DIR + 'fugue', 'files': NIST_SHA3_COMPETITION_FILES_512},

    # Luffa
    # https://web.archive.org/web/20170604091329/http://csrc.nist.gov/groups/ST/hash/sha-3/Round2/documents/Luffa_Round2.zip
    {'algo': 'luffa-224', 'dir': RAW_DIR + 'luffa', 'files': NIST_SHA3_COMPETITION_FILES_224},
    {'algo': 'luffa-256', 'dir': RAW_DIR + 'luffa', 'files': NIST_SHA3_COMPETITION_FILES_256},
    {'algo': 'luffa-384', 'dir': RAW_DIR + 'luffa', 'files': NIST_SHA3_COMPETITION_FILES_384},
    {'algo': 'luffa-512', 'dir': RAW_DIR + 'luffa', 'files': NIST_SHA3_COMPETITION_FILES_512},

    # BlueMidnightWish
    # https://web.archive.org/web/20170604091329/http://csrc.nist.gov/groups/ST/hash/sha-3/Round2/documents/Blue_Midnight_Wish_Round2.zip
    {'algo': 'bluemidnightwish-224', 'dir': RAW_DIR + 'bluemidnightwish', 'files': NIST_SHA3_COMPETITION_FILES_224},
    {'algo': 'bluemidnightwish-256', 'dir': RAW_DIR + 'bluemidnightwish', 'files': NIST_SHA3_COMPETITION_FILES_256},
    {'algo': 'bluemidnightwish-384', 'dir': RAW_DIR + 'bluemidnightwish', 'files': NIST_SHA3_COMPETITION_FILES_384},
    {'algo': 'bluemidnightwish-512', 'dir': RAW_DIR + 'bluemidnightwish', 'files': NIST_SHA3_COMPETITION_FILES_512},

    # SIMD
    # https://web.archive.org/web/20170604091329/http://csrc.nist.gov/groups/ST/hash/sha-3/Round2/documents/SIMD_Round2.zip
    {'algo': 'simd-224', 'dir': RAW_DIR + 'simd', 'files': NIST_SHA3_COMPETITION_FILES_224},
    {'algo': 'simd-256', 'dir': RAW_DIR + 'simd', 'files': NIST_SHA3_COMPETITION_FILES_256},
    {'algo': 'simd-384', 'dir': RAW_DIR + 'simd', 'files': NIST_SHA3_COMPETITION_FILES_384},
    {'algo': 'simd-512', 'dir': RAW_DIR + 'simd', 'files': NIST_SHA3_COMPETITION_FILES_512},

    # CubeHash
    # https://web.archive.org/web/20170604091329/http://csrc.nist.gov/groups/ST/hash/sha-3/Round2/documents/CubeHash_Round2.zip
    {'algo': 'cubehash-224', 'dir': RAW_DIR + 'cubehash', 'files': NIST_SHA3_COMPETITION_FILES_224},
    {'algo': 'cubehash-256', 'dir': RAW_DIR + 'cubehash', 'files': NIST_SHA3_COMPETITION_FILES_256},
    {'algo': 'cubehash-384', 'dir': RAW_DIR + 'cubehash', 'files': NIST_SHA3_COMPETITION_FILES_384},
    {'algo': 'cubehash-512', 'dir': RAW_DIR + 'cubehash', 'files': NIST_SHA3_COMPETITION_FILES_512},

    # Hamsi
    # https://web.archive.org/web/20170604091329/http://csrc.nist.gov/groups/ST/hash/sha-3/Round2/documents/Hamsi_Round2.zip
    {'algo': 'hamsi-224', 'dir': RAW_DIR + 'hamsi', 'files': NIST_SHA3_COMPETITION_FILES_224},
    {'algo': 'hamsi-256', 'dir': RAW_DIR + 'hamsi', 'files': NIST_SHA3_COMPETITION_FILES_256},
    {'algo': 'hamsi-384', 'dir': RAW_DIR + 'hamsi', 'files': NIST_SHA3_COMPETITION_FILES_384},
    {'algo': 'hamsi-512', 'dir': RAW_DIR + 'hamsi', 'files': NIST_SHA3_COMPETITION_FILES_512},

    # Shabal
    # https://web.archive.org/web/20170211075400/http://csrc.nist.gov/groups/ST/hash/sha-3/Round2/documents/Shabal_Round2.zip
    {'algo': 'shabal-224', 'dir': RAW_DIR + 'shabal', 'files': NIST_SHA3_COMPETITION_FILES_224},
    {'algo': 'shabal-256', 'dir': RAW_DIR + 'shabal', 'files': NIST_SHA3_COMPETITION_FILES_256},
    {'algo': 'shabal-384', 'dir': RAW_DIR + 'shabal', 'files': NIST_SHA3_COMPETITION_FILES_384},
    {'algo': 'shabal-512', 'dir': RAW_DIR + 'shabal', 'files': NIST_SHA3_COMPETITION_FILES_512},

    # Shavite
    # https://web.archive.org/web/20170211075400/http://csrc.nist.gov/groups/ST/hash/sha-3/Round2/documents/SHAvite-3_Round2.zip
    {'algo': 'shavite-224', 'dir': RAW_DIR + 'shavite', 'files': NIST_SHA3_COMPETITION_FILES_224},
    {'algo': 'shavite-256', 'dir': RAW_DIR + 'shavite', 'files': NIST_SHA3_COMPETITION_FILES_256},
    {'algo': 'shavite-384', 'dir': RAW_DIR + 'shavite', 'files': NIST_SHA3_COMPETITION_FILES_384},
    {'algo': 'shavite-512', 'dir': RAW_DIR + 'shavite', 'files': NIST_SHA3_COMPETITION_FILES_512},

    ### NIST lightweight cryptography competition 2023: finalists ###

    # Ascon-hash
    # https://csrc.nist.gov/CSRC/media/Projects/lightweight-cryptography/documents/finalist-round/updated-submissions/ascon.zip
    {'algo': 'ascon-hash', 'dir': RAW_DIR + 'ascon-hash', 'files': NIST_LWC_COMPETITION_2023},
    {'algo': 'ascon-hasha', 'dir': RAW_DIR + 'ascon-hasha', 'files': NIST_LWC_COMPETITION_2023},
    {'algo': 'ascon-xof', 'dir': RAW_DIR + 'ascon-xof', 'files': NIST_LWC_COMPETITION_2023},
    {'algo': 'ascon-xofa', 'dir': RAW_DIR + 'ascon-xofa', 'files': NIST_LWC_COMPETITION_2023},

    # Romulus-H
    # https://csrc.nist.gov/CSRC/media/Projects/lightweight-cryptography/documents/finalist-round/updated-submissions/romulus.zip
    {'algo': 'romulus-h', 'dir': RAW_DIR + 'romulus-h', 'files': NIST_LWC_COMPETITION_2023}
]

MSG_LEN_PREFIX = "Len ="  # followed by the length of the message in bits, optional
MSG_PREFIX = "Msg ="  # followed by the message in hex lowercase encoding, required
MD_LEN_PREFIX = "[L ="  # followed by the length of the MD in bits, optional
MD_PREFIX = "MD ="  # followed by the message digest in hex lowercase encoding, required
COUNT_PREFIX = "Count ="  # followed by the value of a counter, optional

HEXDIGITS_LOWERCASE = set('0123456789abcdef')
HEXDIGITS_UPPERCASE = set('0123456789ABCDEF')


def is_hex_lowercase(s):
    return all(c in HEXDIGITS_LOWERCASE for c in s)


def is_hex_uppercase(s):
    # if s is long, then it is faster to check against a set
    return all(c in HEXDIGITS_UPPERCASE for c in s)


def testvectors_text2json(record):
    algorithm = record['algo']
    directory = record['dir']
    filenames = record['files']

    lines = []
    for filename in filenames:
        path = f"{directory}/{filename}"
        print(f"Reading {path} ...")
        file = open(path, 'r', encoding='utf-8')
        lines.extend(file.readlines())
        file.close()

    md_length_in_bits = 0
    expected_next = MD_LEN_PREFIX
    testcases = []
    ignore_next_md = False
    msg_length_is_a_property = False

    for line in lines:

        if line.strip() and not line.startswith("#"):  # ignore empty and commented lines
            line = line.strip()

            # handling an expected MD_LEN_PREFIX
            if expected_next == MD_LEN_PREFIX and line.startswith(MD_LEN_PREFIX):
                md_length_in_bits = line[len(MD_LEN_PREFIX) + 1:len(line) - 1]
                expected_next = MSG_LEN_PREFIX

            # MD_LEN_PREFIX is not there, it is an older format
            elif expected_next == MD_LEN_PREFIX and line.startswith(MSG_LEN_PREFIX):
                md_length_in_bits = None  # [ L = xxx ] is optional
                msg_length_is_a_property = True
                msg_length_in_bits = line[len(MSG_LEN_PREFIX) + 1:]
                expected_next = MSG_PREFIX

            elif expected_next == MD_LEN_PREFIX and line.startswith(COUNT_PREFIX):
                expected_next = MSG_PREFIX

            # handling an expected MSG_LEN_PREFIX
            elif expected_next == MSG_LEN_PREFIX and line.startswith(MSG_LEN_PREFIX):
                msg_length_is_a_property = True
                msg_length_in_bits = line[len(MSG_LEN_PREFIX) + 1:]
                expected_next = MSG_PREFIX

            # multiple files have been concatenated, and the MD_LEN_PREFIX appears again
            elif expected_next == MSG_LEN_PREFIX and line.startswith(MD_LEN_PREFIX):
                md_length_in_bits = line[len(MD_LEN_PREFIX) + 1:len(line) - 1]
                expected_next = MSG_LEN_PREFIX

            elif expected_next == MSG_LEN_PREFIX and line.startswith(COUNT_PREFIX):
                expected_next = MSG_PREFIX

            elif expected_next == MSG_PREFIX and line.startswith(MSG_PREFIX):
                msg = line[len(MSG_PREFIX) + 1:]
                if not msg_length_is_a_property:
                    msg_length_in_bits = len(msg) * 4

                # print(f" --> {msg_length_in_bits}")
                # cut to actual length
                if int(msg_length_in_bits) == 0:
                    msg = ""
                if int(msg_length_in_bits) % 8 > 0:
                    # print(f"{WARNING}: Len has to be a multiple of 8 bits, but found {msg_length_in_bits} bits.",
                    # file=sys.stderr)
                    ignore_next_md = True
                expected_next = MD_PREFIX

            elif expected_next == MD_PREFIX and line.startswith(MD_PREFIX):
                if not ignore_next_md:
                    md = line[len(MD_PREFIX) + 1:]
                    md_length_in_bits = len(md) * 4
                    # print (f"Len = {msg_length_in_bits}, Msg = {msg}, md = {md}")
                    if is_hex_lowercase(md):
                        hex_encoding = "hex"
                    elif is_hex_uppercase(md):
                        hex_encoding = "hex-uppercase"
                    else:
                        print(f"{ERROR}: unexpected encoding in digest {md}")
                    obj = {
                        'desc': f"Algo = {algorithm}, MDLen = {md_length_in_bits}, MsgLen = {msg_length_in_bits}",
                        'args': ["-a", f"{algorithm}",
                                 "-q", f"hex:{msg}",
                                 "-E", f"{hex_encoding}"
                                 ],
                        # 'msg': f"{msg}",
                        'expected': md
                    }
                    testcases.append(obj)
                else:
                    pass
                    # print(f"{WARNING}: ignoring the MD, because the message length is not a multiple of 8 bits.",
                    # file=sys.stderr)
                ignore_next_md = False
                expected_next = MSG_LEN_PREFIX

            else:
                print(f"{ERROR}: Line is unexpected: >>>{line}<<<", file=sys.stderr)
                # exit(1)

    if expected_next != MSG_LEN_PREFIX:
        print(f"{ERROR}: Last record is incomplete, {expected_next} was expected.")

    return json.dumps(testcases, indent=2)


def main():
    for textfile in testvectors_in_textfiles:
        with open(f"testvectors/json/{textfile['algo']}.json", 'w', encoding='utf-8') as f:
            json_data = testvectors_text2json(textfile)
            print(f"Writing {f.name} ...")
            f.write(json_data)
            f.close()


main()
