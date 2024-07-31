import pytest
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from pypalettes import load_cmap
import warnings

warnings.filterwarnings("ignore", message="Using a continuous palette for a non-sequential palette")

def test_load_cmap_discrete():
   cmap = load_cmap(name='ClaudeMonet', cmap_type='discrete')
   assert isinstance(cmap, ListedColormap)
   assert cmap.name == 'ClaudeMonet'
   assert cmap.colors == ['#184430FF', '#548150FF', '#DEB738FF', '#734321FF', '#852419FF']

def test_load_cmap_continuous():
   cmap = load_cmap(name='ClaudeMonet', cmap_type='continuous')
   assert isinstance(cmap, LinearSegmentedColormap)
   assert cmap.name == 'ClaudeMonet'

def test_load_cmap_reverse():
   cmap = load_cmap(name='ClaudeMonet', cmap_type='discrete', reverse=True)
   assert cmap.colors == ['#852419FF', '#734321FF', '#DEB738FF', '#548150FF', '#184430FF']

def test_load_cmap_keep_first_n():
   cmap = load_cmap(name='ClaudeMonet', cmap_type='discrete', keep_first_n=3)
   assert cmap.colors == ['#184430FF', '#548150FF', '#DEB738FF']

def test_load_cmap_keep():
   cmap = load_cmap(name='ClaudeMonet', cmap_type='discrete', keep=[True, False, True, False, True])
   assert cmap.colors == ['#184430FF', '#DEB738FF', '#852419FF']

def test_load_cmap_invalid_name():
   with pytest.raises(ValueError):
      load_cmap(name='invalid_name')

def test_load_cmap_invalid_cmap_type():
   with pytest.raises(ValueError):
      load_cmap(name='ClaudeMonet', cmap_type='invalid_type')

def test_load_cmap_warning():
   with pytest.warns(UserWarning):
      load_cmap(name='ClaudeMonet', cmap_type='continuous', type_warning=True)

def test_load_cmap_no_warning():
   with warnings.catch_warnings():
      warnings.simplefilter("error")
      load_cmap(name='ClaudeMonet', cmap_type='continuous', type_warning=False)

if __name__ == '__main__':
   pass