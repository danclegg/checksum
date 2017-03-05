# checksum
The purpose of this project is to calculate and validate a file's checksum against the published expected hash.

## Usage
`python checksum.py -file filepath -checksum expectedHash [-encryption sha1/sha256/md5]`

## Dependencies
* argparse
* hashlib

_Notes_: The script is written in Python 3. The only argument with a default value is `encryption`, which defaults to `sha1`
