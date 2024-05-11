import typing as ty
import pytest
import util_textarea as uta

# Test cases for the util_textarea module

@pytest.mark.parametrize("input_lines, expected_output", [
    # Test case for Empty input
    ([], []),
    # Test case for Single line comment
    ([
        "This is a line of code",
        "// This is a comment",
        "Another line of code"
    ], [
        "This is a line of code",
        "Another line of code"
    ]),
    # Test case for Single line comment with @ symbol
    ([
        "This is a line of code",
        "@ This is a comment",
        "Another line of code"
    ], [
        "This is a line of code",
        "Another line of code"
    ]),
    # Test case for Multi-line comment with @end symbol
    ([
        "This is a line of code",
        "@end",
        "This is a multi-line comment",
        "This is a multi-line comment",
    ], [
        "This is a line of code",
    ]),
    # Test case for Multi-line comment with @end symbol multiple times
    ([
        "This is a line of code",
        "@end",
        "This is a multi-line comment",
        "@end",
        "This is a multi-line comment",
    ], [
        "This is a line of code",
    ]),
    # Additional test case 1: Single line comment with leading whitespace
    ([
        "  This is a line of code",
        "  // This is a comment",
        "  Another line of code"
    ], [
        "  This is a line of code",
        "  Another line of code"
    ]),
    # Additional test case 2: Multi-line comment with @end symbol with leading and trailing characters
    ([
        "  This is a line of code",
        "  @end this position is ignored",
        "  This is a multi-line comment",
        "  This is a multi-line comment",
    ], [
        "  This is a line of code",
    ]),
])
def test_remove_comments(input_lines: ty.List[str], expected_output: ty.List[str]) -> None:
    assert list(uta.remove_comment_lines(input_lines)) == expected_output
