from utils import concat
import pytest
@pytest.mark.parametrize("str1, str2, expected_result", [("123", "456", "123456"),
                                                         ("abc", "def", "abcdef"),
                                                         ("123abc", "456def", "123abc456def"),
                                                         ("-123", "+456", "-123+456"),
                                                         ("!123@", "_456(", "!123@_456("),
                                                         ("-123", "+456", "-123+456"),
                                                         ])
def test_concat(str1, str2, expected_result):
    assert concat(str1, str2) == expected_result

@pytest.mark.parametrize("str1, str2, expected_exception", [(1, "456", TypeError),
                                                            ("123", 1, TypeError),
                                                            (1, 1, TypeError),
                                                            (1, "q", TypeError),
                                                            ("123", [1,2,3], TypeError),
                                                            ("123", {"name": "Umalat"}, TypeError),
                                                            # возможные тесты
                                                            #("123", null, NameError),
                                                            #("123", undefined, NameError),
                                                            #(q, q, NameError),
                                                            ])

def test_exceptions(str1, str2, expected_exception):
    with pytest.raises(expected_exception):
        concat(str1, str2)