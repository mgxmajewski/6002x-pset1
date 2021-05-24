from ps1 import partition_enumerator, partition_eval, find_best_solution, brute_force_cow_transport
import pytest
from assertpy import assert_that


class TestBruteForceCowsTransport:

    @pytest.fixture(autouse=True)
    def prepare_brute_force_cow_transport(self):
        self.brute_force_cow_transport = brute_force_cow_transport

    def test_brute_force_cow_transport(self):
        # given
        cows_to_transport = {'Miss Bella': 25, 'Boo': 20, 'Milkshake': 40, 'Lotus': 40, 'Horns': 25, 'MooMoo': 50}
        space_limit = 100
        expected = [['MooMoo', 'Horns', 'Miss Bella'], ['Milkshake', 'Lotus', 'Boo']]
        # when
        result = self.brute_force_cow_transport(cows_to_transport, space_limit)
        # then
        assert_that(result).is_equal_to(expected)


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
        expected = [(12, 18, ['Betsy', 'Henrietta'])]
        # when
        result = self.partition_eval(spaces_menu, test_partition)
        # then
        assert_that(result).is_equal_to(expected)


class TestFindBestSolution:

    @pytest.fixture(autouse=True)
    def prepare_find_best_solution(self):
        self.find_best_solution = find_best_solution

    def test_find_best_solution(self):
        # given
        space_limit = 10
        evaluated_partitions = [(12, 18, ['Betsy', 'Henrietta']),
                                (0, 48, ['Henrietta', 'Millie', 'Lola', 'Florence', 'Moo Moo', 'Herman', 'Betsy', 'Milkshake', 'Maggie', 'Oreo']),
                                (1007, 15, ['Millie', 'Lola', 'Florence', 'Moo Moo', 'Maggie']),
                                (876, 10, ['Florence', 'Lola', 'Maggie', 'Moo Moo'])]
        expected = [['Florence', 'Lola', 'Maggie', 'Moo Moo']]
        # when
        result = self.find_best_solution(evaluated_partitions, space_limit)
        # then
        assert_that(result).is_equal_to(expected)
