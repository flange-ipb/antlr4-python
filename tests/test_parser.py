import pytest
from antlr4.error.Errors import ParseCancellationException

from parser.parser import parse_r


@pytest.mark.parametrize(
    "s, expected_id",
    [
        ("hello world", "world"),
    ],
)
def test_parse_r_can_parse(s, expected_id):
    assert parse_r(s) == expected_id


@pytest.mark.parametrize(
    "s, expected_error_msg",
    [
        ("abc", ""
         + "line 1:0 missing 'hello' at 'abc'\n"
         + "abc\n"
         + "^^^"),
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
