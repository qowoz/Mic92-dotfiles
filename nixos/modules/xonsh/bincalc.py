#!/usr/bin/env python3

from xonsh.built_ins import XSH

def format_unit(size) -> str:
    # 2**10 = 1024
    power = 2 ** 10
    n = 0
    unit = {0: "", 1: "KB", 2: "MB", 3: "GB", 4: "TB", 5: "PB", 6: "EB"}
    while size > power:
        size /= power
        n += 1
    return f"{size:0.1f} {unit[n]}"


def contains(lower: int, upper: int, num: int) -> None:
    if lower > num:
        print(f"0x{lower - num:x} smaller than range")
    elif upper < num:
        print(f"0x{num - upper:x} above range")
    else:
        print("yes")


def inspect_num(n: int) -> None:
    print(f"hex  {hex(n)}")
    print(f"bin  {bin(n)}")
    print(f"dec  {n}")
    print(f"oct  {oct(n)}")
    print(f"unit {format_unit(n)}")


XSH.aliases["?"] = lambda args: inspect_num(int(args[0]))
