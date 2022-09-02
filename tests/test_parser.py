import pytest
from antlr4.error.Errors import ParseCancellationException

from parser.parser import parse_r, parse_name


@pytest.mark.parametrize(
    "s, expected_ids",
    [
        ("hello all people", ["all people"]),
        ("hello abc def and ghi jkl and mno pqr stu", ["abc def", "ghi jkl", "mno pqr stu"]),
    ],
)
def test_parse_r_can_parse(s, expected_ids):
    assert parse_r(s) == expected_ids


@pytest.mark.parametrize(
    "s, expected_ids",
    [
        ("first middle middle last", ["first", "middle", "middle", "last"]),
    ],
)
def test_parse_name_can_parse(s, expected_ids):
    assert parse_name(s) == expected_ids


@pytest.mark.parametrize(
    "s, expected_error_msg",
    [
        ("abc", ""
         + "line 1:0 missing 'hello' at 'abc'\n"
         + "abc\n"
         + "^^^"),
        ("hello hello world", ""
         + "line 1:6 extraneous input 'hello' expecting ID\n"
         + "hello hello world\n"
         + "      ^^^^^"),
        ("hello abCde", ""
         + "line 1:8 token recognition error at: 'C'\n"
         + "hello abCde\n"
         + "        ^"),
    ],
)
def test_parse_r_raises_exception(s, expected_error_msg):
    with pytest.raises(ParseCancellationException) as excinfo:
        parse_r(s)
    assert str(excinfo.value) == expected_error_msg
