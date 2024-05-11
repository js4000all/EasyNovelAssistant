"""
Utility functions for textareas.
"""

import typing as ty

def remove_comment_lines(lines: ty.Iterable[str]) -> ty.Iterator[str]:
    """
    Remove comments from a list of strings, and return the rest as an iterator.
    Comments are considered to be:
    * lines that start with "//" or "@".
    * lines below the first line that starts with "@end".
      * Naturally, if this symbol is written multiple times, only the first one will be considered.
    """
    for line in lines:
        s = line.strip()
        if s.startswith("@end"):
            break
        if s.startswith("//") or s.startswith("@"):
            continue
        yield line
