# jacksum-testcases
Testcases to test Jacksum by calling its CLI in order to avoid regressions.

## Prepare it

`convert-testvectors-text2json.py` converts all text based test vectors in `testvectors/raw/` to json in testvectors/json`.
```
$ python ./convert-testvectors-text2json.py
Reading testvectors/raw/algorithms/sha3/SHA3_224ShortMsg.rsp ...
Reading testvectors/raw/algorithms/sha3/SHA3_224LongMsg.rsp ...
Writing testvectors/json/sha3-224.json ...
Reading testvectors/raw/algorithms/sha3/SHA3_256ShortMsg.rsp ...
Reading testvectors/raw/algorithms/sha3/SHA3_256LongMsg.rsp ...
Writing testvectors/json/sha3-256.json ...
...
$
```


## Run it

`run-tests.py` reads the testcases in both `testvectors/lib` and `testvectors/json`, performs the test and prints a result.

```
$ pyhton ./run-tests.py
...
```
