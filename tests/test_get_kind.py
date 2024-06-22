import pytest
from pypalettes import get_kind

def test_get_kind():
   actual = get_kind('MelonPomelo')
   expected = 'qualitative'
   assert actual == expected

def test_get_kind_invalid_name():
   with pytest.raises(ValueError):
      get_kind(name='invalid_name')


if __name__ == '__main__':
   pass
