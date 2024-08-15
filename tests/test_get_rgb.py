import pytest
from pypalettes import get_rgb

class TestGetRGB:

   def test_get_rgb(self):
      actual = get_rgb(name='ClaudeMonet')
      expected = [(24, 68, 48), (84, 129, 80), (222, 183, 56), (115, 67, 33), (133, 36, 25)]
      assert actual == expected

   def test_get_rgb_reverse(self):
      actual = get_rgb(name='ClaudeMonet', reverse=True)
      expected = [(24, 68, 48), (84, 129, 80), (222, 183, 56), (115, 67, 33), (133, 36, 25)][::-1]
      assert actual == expected

   def test_get_rgb_keep_first_n(self):
      actual = get_rgb(name='ClaudeMonet', keep_first_n=3)
      expected = [(24, 68, 48), (84, 129, 80), (222, 183, 56), (115, 67, 33), (133, 36, 25)][:3]
      assert actual == expected

   def test_get_rgb_keep(self):
      actual = get_rgb(name='ClaudeMonet', keep=[True, False, True, False, True])
      expected = [(24, 68, 48), (222, 183, 56), (133, 36, 25)]
      assert actual == expected

   def test_get_rgb_invalid_name(self):
      with pytest.raises(ValueError):
         get_rgb(name='invalid_name')


if __name__ == '__main__':
   pytest.main()
