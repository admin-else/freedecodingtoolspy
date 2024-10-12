import re
import base64
import zlib
import string

START1_OBF_LINE = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'"
START2_OBF_LINE = "exec((_)(b'"
END_OBF_LINE = "'))"
BASE64_CHARS = string.ascii_letters + string.digits + "+/="

def ismadeof(s1, s2):
   return all(char in s2 for char in s1) 

def parse_obf_code(obf_code, start):
    lines = [line for line in obf_code.split("\n") if not line.startswith("#") and not ismadeof(line, string.whitespace)]
    if len(lines) != 1:
        return False
    line = lines[0]
    if not line.startswith(start) or not line.endswith(END_OBF_LINE):
        return False
    data = line[len(start):-len(END_OBF_LINE)]
    if not ismadeof(data, BASE64_CHARS):
        return False
    return data

def _decode(obf_code, start):
    data = parse_obf_code(obf_code, start)
    if not data:
        return obf_code
    data = data[::-1] # reverse it
    data = base64.b64decode(data)
    data = zlib.decompress(data)
    data = data.decode() # it has to be text
    return _decode(data, START2_OBF_LINE)

def decode(obf_code):
    return _decode(obf_code, START1_OBF_LINE)
