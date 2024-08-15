import pytest
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from pypalettes import load_cmap
import warnings

warnings.filterwarnings("ignore", message="Using a continuous palette for a non-sequential palette")

class TestLoadCmap:
   
   def test_load_cmap_discrete(self):
      cmap = load_cmap(name='ClaudeMonet')
      assert isinstance(cmap, ListedColormap)
      assert cmap.name == 'ClaudeMonet'
      assert cmap.colors == ['#184430FF', '#548150FF', '#DEB738FF', '#734321FF', '#852419FF']
   
   def test_load_cmap_with_list(self):
      cmap = load_cmap(name=['Alacena', 'Antique'])
      assert isinstance(cmap, ListedColormap)
      assert cmap.name == "['Alacena', 'Antique']"
      assert cmap.colors == [
         '#693829FF',
         '#894B33FF',
         '#A56A3EFF',
         '#CFB267FF',
         '#D9C5B6FF',
         '#9CA9BAFF',
         '#5480B5FF',
         '#3D619DFF',
         '#405A95FF',
         '#345084FF',
         '#855C75FF',
         '#D9AF6BFF',
         '#AF6458FF',
         '#736F4CFF',
         '#526A83FF',
         '#625377FF',
         '#68855CFF',
         '#9C9C5EFF',
         '#A06177FF',
         '#8C785DFF',
         '#467378FF',
         '#7C7C7CFF'
      ]
      assert cmap.colors == load_cmap(name='Alacena').colors + load_cmap(name='Antique').colors

   def test_load_cmap_continuous(self):
      cmap = load_cmap(name='ClaudeMonet', cmap_type='continuous')
      assert isinstance(cmap, LinearSegmentedColormap)
      assert cmap.name == 'ClaudeMonet'

   def test_load_cmap_reverse(self):
      cmap = load_cmap(name='ClaudeMonet', reverse=True)
      assert cmap.colors == ['#852419FF', '#734321FF', '#DEB738FF', '#548150FF', '#184430FF']

   def test_load_cmap_keep_first_n(self):
      cmap = load_cmap(name='ClaudeMonet', keep_first_n=3)
      assert cmap.colors == ['#184430FF', '#548150FF', '#DEB738FF']

   def test_load_cmap_keep(self):
      cmap = load_cmap(name='ClaudeMonet', keep=[True, False, True, False, True])
      assert cmap.colors == ['#184430FF', '#DEB738FF', '#852419FF']

   def test_load_cmap_invalid_name(self):
      with pytest.raises(ValueError):
         load_cmap(name='invalid_name')

   def test_load_cmap_invalid_cmap_type(self):
      with pytest.raises(ValueError):
         load_cmap(name='ClaudeMonet', cmap_type='invalid_type')

   def test_load_cmap_warning(self):
      with pytest.warns(UserWarning):
         load_cmap(name='ClaudeMonet', cmap_type='continuous', type_warning=True)

   def test_load_cmap_no_warning(self):
      with warnings.catch_warnings():
         warnings.simplefilter("error")
         load_cmap(name='ClaudeMonet', cmap_type='continuous', type_warning=False)

if __name__ == '__main__':
   pytest.main()