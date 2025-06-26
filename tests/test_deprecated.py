import pytest
from pypalettes import get_hex, get_kind, get_rgb, get_source
from pypalettes.deprecated import make_warning_message


class TestGetRGB:
    def test_get_rgb(self):
        with pytest.warns(DeprecationWarning):
            actual = get_rgb(name="ClaudeMonet")
        expected = [
            (24, 68, 48),
            (84, 129, 80),
            (222, 183, 56),
            (115, 67, 33),
            (133, 36, 25),
        ]
        assert actual == expected

    def test_get_with_list(self):
        with pytest.warns(DeprecationWarning):
            actual = get_rgb(name=["ClaudeMonet", "Clay"])
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
        with pytest.warns(DeprecationWarning):
            actual = get_rgb(name="ClaudeMonet", reverse=True)
        expected = [
            (24, 68, 48),
            (84, 129, 80),
            (222, 183, 56),
            (115, 67, 33),
            (133, 36, 25),
        ][::-1]
        assert actual == expected

    def test_get_rgb_keep_first_n(self):
        with pytest.warns(DeprecationWarning):
            actual = get_rgb(name="ClaudeMonet", keep_first_n=3)
        expected = [
            (24, 68, 48),
            (84, 129, 80),
            (222, 183, 56),
            (115, 67, 33),
            (133, 36, 25),
        ][:3]
        assert actual == expected

    def test_get_rgb_keep_last_n(self):
        with pytest.warns(DeprecationWarning):
            actual = get_rgb(name="ClaudeMonet", keep_last_n=3)
        expected = [
            (24, 68, 48),
            (84, 129, 80),
            (222, 183, 56),
            (115, 67, 33),
            (133, 36, 25),
        ][-3:]
        assert actual == expected

    def test_get_rgb_keep(self):
        with pytest.warns(DeprecationWarning):
            actual = get_rgb(name="ClaudeMonet", keep=[True, False, True, False, True])
        expected = [(24, 68, 48), (222, 183, 56), (133, 36, 25)]
        assert actual == expected

    def test_get_rgb_invalid_name(self):
        with pytest.raises(ValueError):
            with pytest.warns(DeprecationWarning):
                get_rgb(name="invalid_name")


class TestGetKind:
    def test_get_kind(self):
        with pytest.warns(DeprecationWarning):
            actual = get_kind(name="MelonPomelo")
        expected = "qualitative"
        assert actual == expected

    def test_get_kind_with_list(self):
        with pytest.warns(DeprecationWarning):
            actual = get_kind(name=["MelonPomelo", "Clay"])
        expected = ["qualitative", "qualitative"]
        assert actual == expected

    def test_get_kind_invalid_name(self):
        with pytest.raises(ValueError):
            with pytest.warns(DeprecationWarning):
                get_kind(name="invalid_name")


class TestGetSource:
    def test_get_source(self):
        with pytest.warns(DeprecationWarning):
            actual = get_source(name="Acadia")
        expected = "The R package: {nationalparkcolors}"
        assert actual == expected

    def test_get_source_with_list(self):
        with pytest.warns(DeprecationWarning):
            actual = get_source(name=["Acadia", "Sunset"])
        expected = ["The R package: {nationalparkcolors}", "The R package: {PNWColors}"]
        assert actual == expected

    def test_get_source_invalid_name(self):
        with pytest.raises(ValueError):
            with pytest.warns(DeprecationWarning):
                get_source(name="invalid_name")


class TestGetHex:
    def test_get_hex(self):
        with pytest.warns(DeprecationWarning):
            actual = get_hex(name="ClaudeMonet")
        expected = ["#184430FF", "#548150FF", "#DEB738FF", "#734321FF", "#852419FF"]
        assert actual == expected

    def test_get_hex_with_list(self):
        with pytest.warns(DeprecationWarning):
            actual = get_hex(name=["ClaudeMonet", "Clay"])
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
        with pytest.warns(DeprecationWarning):
            actual = get_hex(name="ClaudeMonet", reverse=True)
        expected = ["#184430FF", "#548150FF", "#DEB738FF", "#734321FF", "#852419FF"][
            ::-1
        ]
        assert actual == expected

    def test_get_hex_keep_first_n(self):
        with pytest.warns(DeprecationWarning):
            actual = get_hex(name="ClaudeMonet", keep_first_n=3)
        expected = ["#184430FF", "#548150FF", "#DEB738FF", "#734321FF", "#852419FF"][:3]
        assert actual == expected

    def test_get_hex_keep(self):
        with pytest.warns(DeprecationWarning):
            actual = get_hex(name="ClaudeMonet", keep=[True, False, True, False, True])
        expected = ["#184430FF", "#DEB738FF", "#852419FF"]
        assert actual == expected

    def test_get_hex_invalid_name(self):
        with pytest.raises(ValueError):
            with pytest.warns(DeprecationWarning):
                get_hex(name="invalid_name")


class TestWarningMessage:
    def sample_func(self):
        pass

    def test_make_warning_message_basic(self):
        expected = """
The sample_func() function is deprecated and will be removed in a future version.
Please, use: load_cmap('example').some_attribute
"""
        actual = make_warning_message(self.sample_func, "example", "some_attribute")
        assert actual == expected

    def test_make_warning_message_empty_name(self):
        expected = """
The sample_func() function is deprecated and will be removed in a future version.
Please, use: load_cmap('').some_attribute
"""
        actual = make_warning_message(self.sample_func, "", "some_attribute")
        assert actual == expected

    def test_make_warning_message_empty_attribute(self):
        expected = """
The sample_func() function is deprecated and will be removed in a future version.
Please, use: load_cmap('example').
"""
        actual = make_warning_message(self.sample_func, "example", "")
        assert actual == expected

    def test_make_warning_message_special_characters(self):
        expected = """
The sample_func() function is deprecated and will be removed in a future version.
Please, use: load_cmap('ex@mpl3').att#r1but3
"""
        actual = make_warning_message(self.sample_func, "ex@mpl3", "att#r1but3")
        assert actual == expected

    def test_make_warning_message_different_function(self):
        def another_func(self):
            pass

        expected = """
The another_func() function is deprecated and will be removed in a future version.
Please, use: load_cmap('another_example').other_attribute
"""
        actual = make_warning_message(
            another_func, "another_example", "other_attribute"
        )
        assert actual == expected


if __name__ == "__main__":
    pytest.main()
