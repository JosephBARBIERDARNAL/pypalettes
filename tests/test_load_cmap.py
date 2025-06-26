import pytest
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from pypalettes import load_cmap


class TestLoadCmap:
    def test_load_cmap_discrete(self):
        cmap = load_cmap(name="ClaudeMonet")
        assert isinstance(cmap, ListedColormap)
        assert cmap.name == "ClaudeMonet"
        assert cmap.colors == [
            "#184430FF",
            "#548150FF",
            "#DEB738FF",
            "#734321FF",
            "#852419FF",
        ]

    def test_load_cmap_with_list(self):
        cmap = load_cmap(name=["Alacena", "Antique"])
        assert isinstance(cmap, ListedColormap)
        assert cmap.name == "['Alacena', 'Antique']"
        assert cmap.colors == [
            "#693829FF",
            "#894B33FF",
            "#A56A3EFF",
            "#CFB267FF",
            "#D9C5B6FF",
            "#9CA9BAFF",
            "#5480B5FF",
            "#3D619DFF",
            "#405A95FF",
            "#345084FF",
            "#855C75FF",
            "#D9AF6BFF",
            "#AF6458FF",
            "#736F4CFF",
            "#526A83FF",
            "#625377FF",
            "#68855CFF",
            "#9C9C5EFF",
            "#A06177FF",
            "#8C785DFF",
            "#467378FF",
            "#7C7C7CFF",
        ]
        assert (
            cmap.colors
            == load_cmap(name="Alacena").colors + load_cmap(name="Antique").colors
        )

    def test_load_cmap_continuous(self):
        cmap = load_cmap(name="ClaudeMonet", cmap_type="continuous")
        assert isinstance(cmap, LinearSegmentedColormap)
        assert cmap.name == "ClaudeMonet"

    def test_load_cmap_reverse(self):
        cmap = load_cmap(name="ClaudeMonet", reverse=True)
        assert cmap.colors == [
            "#852419FF",
            "#734321FF",
            "#DEB738FF",
            "#548150FF",
            "#184430FF",
        ]

    def test_load_cmap_keep_first_n(self):
        cmap = load_cmap(name="ClaudeMonet", keep_first_n=3)
        assert cmap.colors == ["#184430FF", "#548150FF", "#DEB738FF"]

    def test_load_cmap_keep_last_n(self):
        cmap = load_cmap(name="ClaudeMonet", keep_last_n=3)
        assert cmap.colors == ["#DEB738FF", "#734321FF", "#852419FF"]

    def test_load_cmap_keep(self):
        cmap = load_cmap(name="ClaudeMonet", keep=[True, False, True, False, True])
        assert cmap.colors == ["#184430FF", "#DEB738FF", "#852419FF"]

    def test_load_cmap_no_shuffle(self):
        cmap = load_cmap(name="Acadia", shuffle=False)
        assert isinstance(cmap, ListedColormap)
        assert cmap.name == "Acadia"
        assert len(cmap.colors) > 0
        original_colors = cmap.colors.copy()

        cmap_again = load_cmap(name="Acadia", shuffle=False)
        assert cmap.colors == cmap_again.colors == original_colors

    def test_load_cmap_shuffle_true(self):
        cmap1 = load_cmap(name="Acadia", shuffle=True)
        cmap2 = load_cmap(name="Acadia", shuffle=True)
        assert isinstance(cmap1, ListedColormap)
        assert isinstance(cmap2, ListedColormap)
        assert cmap1.name == cmap2.name == "Acadia"
        assert len(cmap1.colors) == len(cmap2.colors) > 0

    def test_load_cmap_shuffle_seed(self):
        seed = 42
        cmap1 = load_cmap(name="Acadia", shuffle=seed)
        cmap2 = load_cmap(name="Acadia", shuffle=seed)
        assert isinstance(cmap1, ListedColormap)
        assert isinstance(cmap2, ListedColormap)
        assert cmap1.name == cmap2.name == "Acadia"
        assert len(cmap1.colors) == len(cmap2.colors) > 0
        assert cmap1.colors == cmap2.colors

    def test_load_cmap_shuffle_different_seeds(self):
        cmap1 = load_cmap(name="Acadia", shuffle=42)
        cmap2 = load_cmap(name="Acadia", shuffle=24)
        assert isinstance(cmap1, ListedColormap)
        assert isinstance(cmap2, ListedColormap)
        assert cmap1.name == cmap2.name == "Acadia"
        assert len(cmap1.colors) == len(cmap2.colors) > 0

    def test_load_cmap_shuffle_continuous(self):
        cmap = load_cmap(name="Acadia", cmap_type="continuous", shuffle=True)
        assert isinstance(cmap, LinearSegmentedColormap)
        assert cmap.name == "Acadia"

    def test_load_cmap_invalid_cmap_type(self):
        with pytest.raises(ValueError):
            load_cmap(name="Acadia", cmap_type="invalid")

    def test_load_cmap_attributes(self):
        cmap = load_cmap(name="Acadia", shuffle=True)
        assert hasattr(cmap, "source")
        assert hasattr(cmap, "kind")
        assert hasattr(cmap, "hex")
        assert hasattr(cmap, "rgb")
        assert hasattr(cmap, "yiq")
        assert hasattr(cmap, "hsv")

    def test_load_cmap_shuffle_with_other_params(self):
        cmap = load_cmap(
            name="Acadia", reverse=True, keep_first_n=5, repeat=2, shuffle=True
        )
        assert isinstance(cmap, ListedColormap)
        assert cmap.name == "Acadia"
        assert len(cmap.colors) == 10

    def test_load_cmap_repeat(self):
        actual = load_cmap(name="ClaudeMonet", repeat=2).colors
        expected = [
            "#184430FF",
            "#548150FF",
            "#DEB738FF",
            "#734321FF",
            "#852419FF",
            "#184430FF",
            "#548150FF",
            "#DEB738FF",
            "#734321FF",
            "#852419FF",
        ]
        assert actual == expected

    def test_load_cmap_invalid_repeat(self):
        with pytest.raises(TypeError):
            load_cmap(name="ClaudeMonet", repeat=1.5)

    def test_load_cmap_invalid_name(self):
        with pytest.raises(ValueError):
            load_cmap(name="invalid_name")

    def test_load_cmap_random_name(self):
        cmap = load_cmap(name="random", cmap_type="continuous")
        assert isinstance(cmap, LinearSegmentedColormap)
        cmap = load_cmap(name="random")
        assert isinstance(cmap, ListedColormap)

    def test_get_hex(self):
        actual = load_cmap(name="ClaudeMonet").hex
        expected = ["#184430FF", "#548150FF", "#DEB738FF", "#734321FF", "#852419FF"]
        assert actual == expected

    def test_get_hex_with_list(self):
        actual = load_cmap(name=["ClaudeMonet", "Clay"]).hex
        expected = [
            "#184430FF",
            "#548150FF",
            "#DEB738FF",
            "#734321FF",
            "#852419FF",
            "#C48329FF",
            "#8B3B36FF",
            "#A2B4B7FF",
            "#514A2EFF",
            "#CF9860FF",
            "#8E4115FF",
        ]
        assert actual == expected

    def test_get_hex_reverse(self):
        actual = load_cmap(name="ClaudeMonet", reverse=True).hex
        expected = ["#184430FF", "#548150FF", "#DEB738FF", "#734321FF", "#852419FF"][
            ::-1
        ]
        assert actual == expected

    def test_get_hex_keep_first_n(self):
        actual = load_cmap(name="ClaudeMonet", keep_first_n=3).hex
        expected = ["#184430FF", "#548150FF", "#DEB738FF", "#734321FF", "#852419FF"][:3]
        assert actual == expected

    def test_get_hex_keep(self):
        actual = load_cmap(
            name="ClaudeMonet", keep=[True, False, True, False, True]
        ).hex
        expected = ["#184430FF", "#DEB738FF", "#852419FF"]
        assert actual == expected

    def test_get_hex_invalid_name(self):
        with pytest.raises(ValueError):
            load_cmap(name="invalid_name").hex

    def test_get_rgb(self):
        actual = load_cmap(name="ClaudeMonet").rgb
        expected = [
            (24, 68, 48),
            (84, 129, 80),
            (222, 183, 56),
            (115, 67, 33),
            (133, 36, 25),
        ]
        assert actual == expected

    def test_get_with_list(self):
        actual = load_cmap(name=["ClaudeMonet", "Clay"]).rgb
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
            (142, 65, 21),
        ]
        assert actual == expected

    def test_get_rgb_reverse(self):
        actual = load_cmap(name="ClaudeMonet", reverse=True).rgb
        expected = [
            (24, 68, 48),
            (84, 129, 80),
            (222, 183, 56),
            (115, 67, 33),
            (133, 36, 25),
        ][::-1]
        assert actual == expected

    def test_get_rgb_keep_first_n(self):
        actual = load_cmap(name="ClaudeMonet", keep_first_n=3).rgb
        expected = [
            (24, 68, 48),
            (84, 129, 80),
            (222, 183, 56),
            (115, 67, 33),
            (133, 36, 25),
        ][:3]
        assert actual == expected

    def test_get_rgb_keep(self):
        actual = load_cmap(
            name="ClaudeMonet", keep=[True, False, True, False, True]
        ).rgb
        expected = [(24, 68, 48), (222, 183, 56), (133, 36, 25)]
        assert actual == expected

    def test_get_rgb_invalid_name(self):
        with pytest.raises(ValueError):
            load_cmap(name="invalid_name").rgb

    def test_get_yiq(self):
        actual = load_cmap(name="ClaudeMonet").yiq
        expected = [
            (52.599999999999994, -19.921999999999997, -15.613999999999994),
            (110.11, -11.1917, -24.877899999999997),
            (180.73, 64.21690000000001, -31.32969999999999),
            (77.66, 39.689800000000005, -0.38739999999999597),
            (63.89, 61.6417, 17.227899999999998),
        ]
        assert actual == expected

    def test_get_yiq_invalid_name(self):
        with pytest.raises(ValueError):
            load_cmap(name="invalid_name").yiq

    def test_get_hsv(self):
        actual = load_cmap(name="ClaudeMonet").hsv
        expected = [
            (0.42424242424242425, 0.6470588235294118, 68),
            (0.31972789115646255, 0.3798449612403101, 129),
            (0.12751004016064257, 0.7477477477477478, 222),
            (0.06910569105691057, 0.7130434782608696, 115),
            (0.01697530864197531, 0.8120300751879699, 133),
        ]
        assert actual == expected

    def test_get_hsv_invalid_name(self):
        with pytest.raises(ValueError):
            load_cmap(name="invalid_name").hsv

    def test_get_kind(self):
        actual = load_cmap(name="MelonPomelo").kind
        expected = "qualitative"
        assert actual == expected

    def test_get_kind_with_list(self):
        actual = load_cmap(name=["MelonPomelo", "Clay"]).kind
        expected = ["qualitative", "qualitative"]
        assert actual == expected

    def test_get_kind_invalid_name(self):
        with pytest.raises(ValueError):
            load_cmap(name="invalid_name").kind


if __name__ == "__main__":
    pytest.main()
