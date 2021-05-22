from ps1 import partition_enumerator, partition_eval
import pytest
from assertpy import assert_that

class TestBruteForceCowsTransport:
    def test_brute_force_cow_transport(self):
        assert False


class TestPartitionEnumerator:
    def test_partition_enumerator(self):
        # given
        partitions = [["a", "b"], ["c", "d"]]
        expected = [(0, ["a", "b"]), (1, ["c", "d"])]
        # when
        result = partition_enumerator(partitions)
        # then
        assert_that(result).is_equal_to(expected)


class TestPartitionEval:

    @pytest.fixture(autouse=True)
    def prepare_partition_eval(self):
        self.partition_eval = partition_eval

    def test_partition_eval(self):
        # given
        spaces_menu = {'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3,
                       'Milkshake': 2, 'Millie': 5, 'Lola': 2, 'Florence': 2, 'Henrietta': 9}
        test_partition = [(12, ['Betsy', 'Henrietta'])]
        expected = [(12, 18)]
        # when
        result = self.partition_eval(spaces_menu, test_partition)
        # then
        assert_that(result).is_equal_to(expected)