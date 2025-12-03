from part_1 import find_invalid_ids, is_even_length


class TestPart1:
    def test1(self):
        print("Tested")
        assert True


class TestEvenLength:
    def test_is_even_length(self):
        assert is_even_length(11) is True
        assert is_even_length(4444) is True
        assert is_even_length(123123) is True

    def test_is_not_even_length(self):
        assert is_even_length(111) is False
        assert is_even_length(555) is False
        assert is_even_length(999) is False
        assert is_even_length(10001) is False
        assert is_even_length(7867543) is False


class TestFindInvalidIDs:
    def test_find_invalid_ids(self):
        assert find_invalid_ids(11, 22) == [11, 22]
        assert find_invalid_ids(95, 115) == [99]
        assert find_invalid_ids(998, 1012) == [1010]
        assert find_invalid_ids(1188511880, 1188511890) == [1188511885]
        assert find_invalid_ids(222220, 222224) == [222222]
        assert find_invalid_ids(446443, 446449) == [446446]
        assert find_invalid_ids(38593856, 38593862) == [38593859]

    def test_find_no_invalid_ids(self):
        assert find_invalid_ids(1, 10) == []
        assert find_invalid_ids(1234, 1239) == []
        assert find_invalid_ids(567890, 567895) == []
        assert find_invalid_ids(1698522, 1698528) == []
