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

   def test_get_hex(self):
      actual = load_cmap(name='ClaudeMonet').hex
      expected = ['#184430FF', '#548150FF', '#DEB738FF', '#734321FF', '#852419FF']
      assert actual == expected
   
   def test_get_hex_with_list(self):
      actual = load_cmap(name=['ClaudeMonet', 'Clay']).hex
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
      actual = load_cmap(name='ClaudeMonet', reverse=True).hex
      expected = ['#184430FF', '#548150FF', '#DEB738FF', '#734321FF', '#852419FF'][::-1]
      assert actual == expected

   def test_get_hex_keep_first_n(self):
      actual = load_cmap(name='ClaudeMonet', keep_first_n=3).hex
      expected = ['#184430FF', '#548150FF', '#DEB738FF', '#734321FF', '#852419FF'][:3]
      assert actual == expected

   def test_get_hex_keep(self):
      actual = load_cmap(name='ClaudeMonet', keep=[True, False, True, False, True]).hex
      expected = ['#184430FF', '#DEB738FF', '#852419FF']
      assert actual == expected

   def test_get_hex_invalid_name(self):
      with pytest.raises(ValueError):
         load_cmap(name='invalid_name').hex

   def test_get_rgb(self):
      actual = load_cmap(name='ClaudeMonet').rgb
      expected = [(24, 68, 48), (84, 129, 80), (222, 183, 56), (115, 67, 33), (133, 36, 25)]
      assert actual == expected

   def test_get_with_list(self):
      actual = load_cmap(name=['ClaudeMonet', 'Clay']).rgb
      expected = [
         (24, 68, 48),
         (84, 129, 80),
         (222, 183, 56),
         (115, 67, 33),
         (133, 36, 25),
         (196, 131, 41),
         (139, 59, 54),
         (162, 180, 183),
         (81, 74, 46),
         (207, 152, 96),
         (142, 65, 21)
      ]
      assert actual == expected

   def test_get_rgb_reverse(self):
      actual = load_cmap(name='ClaudeMonet', reverse=True).rgb
      expected = [(24, 68, 48), (84, 129, 80), (222, 183, 56), (115, 67, 33), (133, 36, 25)][::-1]
      assert actual == expected

   def test_get_rgb_keep_first_n(self):
      actual = load_cmap(name='ClaudeMonet', keep_first_n=3).rgb
      expected = [(24, 68, 48), (84, 129, 80), (222, 183, 56), (115, 67, 33), (133, 36, 25)][:3]
      assert actual == expected

   def test_get_rgb_keep(self):
      actual = load_cmap(name='ClaudeMonet', keep=[True, False, True, False, True]).rgb
      expected = [(24, 68, 48), (222, 183, 56), (133, 36, 25)]
      assert actual == expected

   def test_get_rgb_invalid_name(self):
      with pytest.raises(ValueError):
         load_cmap(name='invalid_name').rgb

   def test_get_yiq(self):
      actual = load_cmap(name='ClaudeMonet').yiq
      expected = [(52.599999999999994, -19.921999999999997, -15.613999999999994),
 (110.11, -11.1917, -24.877899999999997),
 (180.73, 64.21690000000001, -31.32969999999999),
 (77.66, 39.689800000000005, -0.38739999999999597),
 (63.89, 61.6417, 17.227899999999998)]
      assert actual == expected

   def test_get_yiq_invalid_name(self):
      with pytest.raises(ValueError):
         load_cmap(name='invalid_name').yiq

   def test_get_hls(self):
      actual = load_cmap(name='ClaudeMonet').hls
      expected = [(0.42424242424242425, 46.0, -0.4888888888888889),
 (0.31972789115646255, 104.5, -0.23671497584541062),
 (0.12751004016064257, 139.0, -0.6014492753623188),
 (0.06910569105691057, 74.0, -0.5616438356164384),
 (0.01697530864197531, 79.0, -0.6923076923076923)]
      assert actual == expected

   def test_get_hls_invalid_name(self):
      with pytest.raises(ValueError):
         load_cmap(name='invalid_name').hls

   def test_get_hsv(self):
      actual = load_cmap(name='ClaudeMonet').hsv
      expected = [(0.42424242424242425, 0.6470588235294118, 68),
 (0.31972789115646255, 0.3798449612403101, 129),
 (0.12751004016064257, 0.7477477477477478, 222),
 (0.06910569105691057, 0.7130434782608696, 115),
 (0.01697530864197531, 0.8120300751879699, 133)]
      assert actual == expected

   def test_get_hsv_invalid_name(self):
      with pytest.raises(ValueError):
         load_cmap(name='invalid_name').hsv

   def test_get_kind(self):
      actual = load_cmap(name='MelonPomelo').kind
      expected = 'qualitative'
      assert actual == expected

   def test_get_kind_with_list(self):
      actual = load_cmap(name=['MelonPomelo', 'Clay']).kind
      expected = ['qualitative', 'qualitative']
      assert actual == expected

   def test_get_kind_invalid_name(self):
      with pytest.raises(ValueError):
         load_cmap(name='invalid_name').kind

if __name__ == '__main__':
   pytest.main()