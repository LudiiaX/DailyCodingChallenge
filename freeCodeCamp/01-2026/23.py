import re
def is_valid_hex(s):
    return True if re.match(r"^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$", s) else False


print(is_valid_hex("#123"))
print(is_valid_hex("#123abc"))
print(is_valid_hex("#ABCDEF"))
print(is_valid_hex("#0a1B2c"))
print(is_valid_hex("#12G"))
print(is_valid_hex("#1234567"))
print(is_valid_hex("#12 3"))
print(is_valid_hex("fff"))