"""
Implement a function all_eq(lst) taking as an input a list of strings with
differing lengths and which returns a list of the strings with their lengths
equal to the length of the longest string in the input list; pad the shorter
strings with _ symbols at their end until their length is equal to the target
length. The order of the strings in the output list must be the same as in
the input list.
"""

from typing import List


def all_eq(lst: List[str]) -> List[str]:
    if not lst:
        return []

    mapping = {string: len(string) for string in lst}
    max_len = max(mapping.values())

    res = [string + (max_len - mapping[string]) * "_" for string in lst]

    return res


def main() -> int:
    print(all_eq(["dfdf", "df", "d", "dfdga", "dd"]))

    return 0


if __name__ == "__main__":
    SystemExit(main())
