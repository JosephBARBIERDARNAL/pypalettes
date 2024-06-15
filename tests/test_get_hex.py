import pytest
from pypalettes import get_hex

def test_get_hex():
   actual = get_hex(name='ClaudeMonet')
   expected = ['#184430FF', '#548150FF', '#DEB738FF', '#734321FF', '#852419FF']
   assert actual == expected

def test_get_hex_reverse():
   actual = get_hex(name='ClaudeMonet', reverse=True)
   expected = ['#184430FF', '#548150FF', '#DEB738FF', '#734321FF', '#852419FF'][::-1]
   assert actual == expected

def test_get_hex_keep_first_n():
   actual = get_hex(name='ClaudeMonet', keep_first_n=3)
   expected = ['#184430FF', '#548150FF', '#DEB738FF', '#734321FF', '#852419FF'][:3]
   assert actual == expected

def test_get_hex_keep():
   actual = get_hex(name='ClaudeMonet', keep=[True, False, True, False, True])
   expected = ['#184430FF', '#DEB738FF', '#852419FF']
   assert actual == expected

def test_get_hex_invalid_name():
   with pytest.raises(ValueError):
      get_hex(name='invalid_name')


if __name__ == '__main__':
   pass
