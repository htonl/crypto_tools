import base64
import binascii
from frequency_analysis import detect_language
from frequency_analysis import score_hexbytes
from frequency_analysis import 

# @Method b64_hex
#
# @arg hexbytes - hexbytes to b64
#
# return b64 of @hexbytes as @bytes
def b64_hex(hexbytes):
    return base64.b64encode(hexbytes)

# @Method xor_fl
#
# @arg b0 - hexbyte buffer 1
# @arg b1 - hexbyte buffer 2
#
# return xor of 2 equal len buf
# return error if not equal len
def xor_fl(b0, b1):
    if len(b0) != len(b1):
        return -1
    return bytes(a ^ b for (a, b) in zip(b0, b1)) 

# @Method print_byte_as_hex
#
# @arg hexbytes - hexbytes to print as hex
#
# print bytes as a string of hex
def print_byte_as_hex(hexbytes):
    print(binascii.hexlify(hexbytes)) 

# @Method freq_analysis
#
# @arg hexbytes - hexbytes to detect language and score
#
# return tuple (language, score)
def freq_analysis(hexbytes):
    return (detect_language(hexbytes), score_hexbytes(hexbytes))