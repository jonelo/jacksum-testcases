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
NIST_COMPETITION_FILES_224 = ['ShortMsgKAT_224.txt', 'LongMsgKAT_224.txt']
NIST_COMPETITION_FILES_256 = ['ShortMsgKAT_256.txt', 'LongMsgKAT_256.txt']
NIST_COMPETITION_FILES_384 = ['ShortMsgKAT_384.txt', 'LongMsgKAT_384.txt']
NIST_COMPETITION_FILES_512 = ['ShortMsgKAT_512.txt', 'LongMsgKAT_512.txt']

testvectors_in_textfiles = [
    # SHA3 family
    # https://csrc.nist.gov/CSRC/media/Projects/Cryptographic-Algorithm-Validation-Program/documents/sha3/sha-3bytetestvectors.zip
    {'algo': 'sha3-224', 'dir': RAW_DIR + 'sha3', 'files': ['SHA3_224ShortMsg.rsp', 'SHA3_224LongMsg.rsp']},
    {'algo': 'sha3-256', 'dir': RAW_DIR + 'sha3', 'files': ['SHA3_256ShortMsg.rsp', 'SHA3_256LongMsg.rsp']},
    {'algo': 'sha3-384', 'dir': RAW_DIR + 'sha3', 'files': ['SHA3_384ShortMsg.rsp', 'SHA3_384LongMsg.rsp']},
    {'algo': 'sha3-512', 'dir': RAW_DIR + 'sha3', 'files': ['SHA3_512ShortMsg.rsp', 'SHA3_512LongMsg.rsp']},

    # BLAKE, final round of the NIST SHA-3 competition
    # https://web.archive.org/web/20170812201530/http://csrc.nist.gov/groups/ST/hash/sha-3/Round3/documents/Blake_FinalRnd.zip
    {'algo': 'blake-224', 'dir': RAW_DIR + 'blake', 'files': NIST_COMPETITION_FILES_224},
    {'algo': 'blake-256', 'dir': RAW_DIR + 'blake', 'files': NIST_COMPETITION_FILES_256},
    {'algo': 'blake-384', 'dir': RAW_DIR + 'blake', 'files': NIST_COMPETITION_FILES_384},
    {'algo': 'blake-512', 'dir': RAW_DIR + 'blake', 'files': NIST_COMPETITION_FILES_512},

    # Groestl, final round of the NIST SHA-3 competition
    # https://web.archive.org/web/20170812201530/http://csrc.nist.gov/groups/ST/hash/sha-3/Round3/documents/Groestl_FinalRnd.zip
    {'algo': 'groestl-224', 'dir': RAW_DIR + 'groestl', 'files': NIST_COMPETITION_FILES_224},
    {'algo': 'groestl-256', 'dir': RAW_DIR + 'groestl', 'files': NIST_COMPETITION_FILES_256},
    {'algo': 'groestl-384', 'dir': RAW_DIR + 'groestl', 'files': NIST_COMPETITION_FILES_384},
    {'algo': 'groestl-512', 'dir': RAW_DIR + 'groestl', 'files': NIST_COMPETITION_FILES_512},

    # JH, final round of the NIST SHA-3 competition
    # https://web.archive.org/web/20170812201530/http://csrc.nist.gov/groups/ST/hash/sha-3/Round3/documents/JH_FinalRnd.zip
    {'algo': 'jh-224', 'dir': RAW_DIR + 'jh', 'files': NIST_COMPETITION_FILES_224},
    {'algo': 'jh-256', 'dir': RAW_DIR + 'jh', 'files': NIST_COMPETITION_FILES_256},
    {'algo': 'jh-384', 'dir': RAW_DIR + 'jh', 'files': NIST_COMPETITION_FILES_384},
    {'algo': 'jh-512', 'dir': RAW_DIR + 'jh', 'files': NIST_COMPETITION_FILES_512},

    # Keccak, final round of the NIST SHA-3 competition
    # https://web.archive.org/web/20170812201530/http://csrc.nist.gov/groups/ST/hash/sha-3/Round3/documents/Keccak_FinalRnd.zip
    {'algo': 'keccak-224', 'dir': RAW_DIR + 'keccak', 'files': NIST_COMPETITION_FILES_224},
    {'algo': 'keccak-256', 'dir': RAW_DIR + 'keccak', 'files': NIST_COMPETITION_FILES_256},
    {'algo': 'keccak-384', 'dir': RAW_DIR + 'keccak', 'files': NIST_COMPETITION_FILES_384},
    {'algo': 'keccak-512', 'dir': RAW_DIR + 'keccak', 'files': NIST_COMPETITION_FILES_512},

    # Skein
    # https://web.archive.org/web/20170812201530/http://csrc.nist.gov/groups/ST/hash/sha-3/Round3/documents/Skein_FinalRnd.zip
    {'algo': 'skein-512-224', 'dir': RAW_DIR + 'skein', 'files': NIST_COMPETITION_FILES_224},
    {'algo': 'skein-512-256', 'dir': RAW_DIR + 'skein', 'files': NIST_COMPETITION_FILES_256},
    {'algo': 'skein-512-384', 'dir': RAW_DIR + 'skein', 'files': NIST_COMPETITION_FILES_384},
    {'algo': 'skein-512-512', 'dir': RAW_DIR + 'skein', 'files': NIST_COMPETITION_FILES_512},

    # ECHO
    # https://web.archive.org/web/20170604091329/http://csrc.nist.gov/groups/ST/hash/sha-3/Round2/documents/ECHO_Round2.zip
    {'algo': 'echo-224', 'dir': RAW_DIR + 'echo', 'files': NIST_COMPETITION_FILES_224},
    {'algo': 'echo-256', 'dir': RAW_DIR + 'echo', 'files': NIST_COMPETITION_FILES_256},
    {'algo': 'echo-384', 'dir': RAW_DIR + 'echo', 'files': NIST_COMPETITION_FILES_384},
    {'algo': 'echo-512', 'dir': RAW_DIR + 'echo', 'files': NIST_COMPETITION_FILES_512},

    # Fugue
    # https://web.archive.org/web/20170604091329/http://csrc.nist.gov/groups/ST/hash/sha-3/Round2/documents/Fugue_Round2.zip
    {'algo': 'fugue-224', 'dir': RAW_DIR + 'fugue', 'files': NIST_COMPETITION_FILES_224},
    {'algo': 'fugue-256', 'dir': RAW_DIR + 'fugue', 'files': NIST_COMPETITION_FILES_256},
    {'algo': 'fugue-384', 'dir': RAW_DIR + 'fugue', 'files': NIST_COMPETITION_FILES_384},
    {'algo': 'fugue-512', 'dir': RAW_DIR + 'fugue', 'files': NIST_COMPETITION_FILES_512},

    # Luffa
    # https://web.archive.org/web/20170604091329/http://csrc.nist.gov/groups/ST/hash/sha-3/Round2/documents/Luffa_Round2.zip
    {'algo': 'luffa-224', 'dir': RAW_DIR + 'luffa', 'files': NIST_COMPETITION_FILES_224},
    {'algo': 'luffa-256', 'dir': RAW_DIR + 'luffa', 'files': NIST_COMPETITION_FILES_256},
    {'algo': 'luffa-384', 'dir': RAW_DIR + 'luffa', 'files': NIST_COMPETITION_FILES_384},
    {'algo': 'luffa-512', 'dir': RAW_DIR + 'luffa', 'files': NIST_COMPETITION_FILES_512},

]

L_PREFIX = "[L = "  # followed by the length of the MD in bits, optional
LEN_PREFIX = "Len = "  # followed by the length of the message in bits
MSG_PREFIX = "Msg = "  # followed by the message in hex lowercase encoding
MD_PREFIX = "MD = "  # followed by the message digest in hex lowercase encoding

HEXDIGITS_UPPERCASE = set('0123456789ABCDEF')
HEXDIGITS_LOWERCASE = set('0123456789abcdef')

def is_hex_uppercase(s):
    # if s is long, then it is faster to check against a set
    return all(c in HEXDIGITS_UPPERCASE for c in s)

def is_hex_lowercase(s):
    return all(c in HEXDIGITS_LOWERCASE for c in s)

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
    expected_next = L_PREFIX
    testcases = []
    ignore_next_md = False

    for line in lines:

        if line.strip() and not line.startswith("#"):  # ignore empty and commented lines
            line = line.strip()

            if expected_next == L_PREFIX and line.startswith(L_PREFIX):
                md_length_in_bits = line[len(L_PREFIX):len(line) - 1]
                expected_next = LEN_PREFIX

            elif expected_next == L_PREFIX and line.startswith(LEN_PREFIX):
                md_length_in_bits = None  # [ L = xxx ] is optional
                msg_length = line[len(LEN_PREFIX):]
                expected_next = MSG_PREFIX

            elif expected_next == LEN_PREFIX and line.startswith(LEN_PREFIX):
                msg_length = line[len(LEN_PREFIX):]
                expected_next = MSG_PREFIX

            elif expected_next == MSG_PREFIX and line.startswith(MSG_PREFIX):
                msg = line[len(MSG_PREFIX):]
                # cut to actual length
                if int(msg_length) == 0:
                    msg = ""
                if int(msg_length) % 8 > 0:
                    # print(f"{WARNING}: Len has to be a multiple of 8 bits, but found {msg_length} bits.",
                    # file=sys.stderr)
                    ignore_next_md = True
                expected_next = MD_PREFIX

            elif expected_next == MD_PREFIX and line.startswith(MD_PREFIX):
                if not ignore_next_md:
                    md = line[len(MD_PREFIX):]
                    md_length_in_bits = len(md) * 4
                    # print (f"Len = {msg_length}, Msg = {msg}, md = {md}")
                    if is_hex_lowercase(md):
                        hex_encoding = "hex"
                    elif is_hex_uppercase(md):
                        hex_encoding = "hex-uppercase"
                    else:
                        print(f"{ERROR}: unexpected encoding in digest {md}")
                    obj = {
                        'desc': f"Algo = {algorithm}, MDLen = {md_length_in_bits}, MsgLen = {msg_length}",
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
                expected_next = LEN_PREFIX

            elif line.startswith(L_PREFIX):  # multiple files have been concatenated, and the L_PREFIX appears again
                md_length_in_bits = line[len(L_PREFIX):len(line) - 1]
                expected_next = LEN_PREFIX

            else:
                print(f"{ERROR}: Line is unexpected: {line}", file=sys.stderr)

    if expected_next != LEN_PREFIX:
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
