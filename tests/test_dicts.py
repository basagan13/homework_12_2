from utils.dicts import get_val

def test_get_val():
    assert get_val({1: 'one', 2: 'two', 3: 'three',
                    4: 'four', 5:'five'}, 1, 'test') == 'one'
    assert get_val({1: 'one', 2: 'two', 3: 'three',
                    4: 'four', 5:'five'}, 0, 'test') == 'test'
    assert get_val({1: 'one', 2: 'two', 3: 'three',
                    4: 'four', 5: 'five'}, -8, 'test') == 'test'
    assert get_val({1: 'one', 2: 'two', 3: 'three',
                    4: 'four', 5: 'five'}, 'digit', 'test') == 'test'
    assert get_val({}, 1, 'test') == '{}'
