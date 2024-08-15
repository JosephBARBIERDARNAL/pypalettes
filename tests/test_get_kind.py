import pytest
from pypalettes import get_kind

class TestGetKind:

   def test_get_kind(self):
      actual = get_kind(name='MelonPomelo')
      expected = 'qualitative'
      assert actual == expected

   def test_get_kind_with_list(self):
      actual = get_kind(name=['MelonPomelo', 'Clay'])
      expected = ['qualitative', 'qualitative']
      assert actual == expected

   def test_get_kind_invalid_name(self):
      with pytest.raises(ValueError):
         get_kind(name='invalid_name')


if __name__ == '__main__':
   pytest.main()
