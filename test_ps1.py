from ps1 import partition_enumerator
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

