import pytest
from pypalettes import get_hex

class TestGetHex:
   
   def test_get_hex(self):
      actual = get_hex(name='ClaudeMonet')
      expected = ['#184430FF', '#548150FF', '#DEB738FF', '#734321FF', '#852419FF']
      assert actual == expected
   
   def test_get_hex_with_list(self):
      actual = get_hex(name=['ClaudeMonet', 'Clay'])
      expected = [
         '#184430FF',
         '#548150FF',
         '#DEB738FF',
         '#734321FF',
         '#852419FF',
         '#C48329FF',
         '#8B3B36FF',
         '#A2B4B7FF',
         '#514A2EFF',
         '#CF9860FF',
         '#8E4115FF'
      ]
      assert actual == expected

   def test_get_hex_reverse(self):
      actual = get_hex(name='ClaudeMonet', reverse=True)
      expected = ['#184430FF', '#548150FF', '#DEB738FF', '#734321FF', '#852419FF'][::-1]
      assert actual == expected

   def test_get_hex_keep_first_n(self):
      actual = get_hex(name='ClaudeMonet', keep_first_n=3)
      expected = ['#184430FF', '#548150FF', '#DEB738FF', '#734321FF', '#852419FF'][:3]
      assert actual == expected

   def test_get_hex_keep(self):
      actual = get_hex(name='ClaudeMonet', keep=[True, False, True, False, True])
      expected = ['#184430FF', '#DEB738FF', '#852419FF']
      assert actual == expected

   def test_get_hex_invalid_name(self):
      with pytest.raises(ValueError):
         get_hex(name='invalid_name')

if __name__ == '__main__':
   pytest.main()