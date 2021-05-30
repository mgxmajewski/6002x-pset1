from ps1 import partition_enumerator, partition_eval, find_best_solution, brute_force_cow_transport, \
    greedy_cow_transport, sort_cows
import pytest
from assertpy import assert_that
import collections


class TestBruteForceCowsTransport:

    @pytest.fixture(autouse=True)
    def prepare_brute_force_cow_transport(self):
        self.brute_force_cow_transport = brute_force_cow_transport

    # case1
    cows_to_transport_1 = {'Miss Bella': 25, 'Boo': 20, 'Milkshake': 40, 'Lotus': 40, 'Horns': 25, 'MooMoo': 50}
    space_limit_1 = 100
    expected_1 = [['MooMoo', 'Miss Bella', 'Horns'], ['Milkshake', 'Lotus', 'Boo']]
    case_1 = cows_to_transport_1, space_limit_1, expected_1

    # case2
    cows_to_transport_2 = {'Daisy': 50, 'Buttercup': 72, 'Betsy': 65}
    space_limit_2 = 75
    expected_2 = [['Buttercup'], ['Betsy'], ['Daisy']]
    case_2 = cows_to_transport_2, space_limit_2, expected_2

    # case3
    cows_to_transport_3 = {'Starlight': 54, 'Buttercup': 11, 'Luna': 41, 'Betsy': 39}
    space_limit_3 = 145
    expected_3 = [['Buttercup', 'Starlight', 'Betsy', 'Luna']]
    case_3 = cows_to_transport_3, space_limit_3, expected_3

    @pytest.mark.parametrize("cows_to_transport, space_limit, expected", [case_1, case_2, case_3])
    def test_brute_force_cow_transport(self, cows_to_transport, space_limit, expected):
        # given

        # when
        brute_force = self.brute_force_cow_transport(cows_to_transport, space_limit)

        # then
        def eval_lists(brute_force_result, expected_solution):
            unordered_transports_comparisons = []
            for transport in range(len(expected_solution)):
                print()
                print(brute_force_result[transport], expected_solution[transport])
                compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
                unordered_transports_comparisons.append(compare(brute_force_result[transport],
                                                                expected_solution[transport]))
            if all([x == True for x in unordered_transports_comparisons]):
                return True
            else:
                return False

        result = eval_lists(brute_force, expected)
        assert_that(result).is_true()

    def test_partition_enumerator(self):
        # given
        partitions = [["a", "b"], ["c", "d"]]
        expected = [(0, ["a", "b"]), (1, ["c", "d"])]
        # when
        result = partition_enumerator(partitions)
        # then
        assert_that(result).is_equal_to(expected)

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

    @pytest.fixture(autouse=True)
    def prepare_find_best_solution(self):
        self.find_best_solution = find_best_solution

    def test_find_best_solution(self):
        # given
        space_limit = 10
        evaluated_partitions = [(12, 18, ['Betsy', 'Henrietta']),
                                (0, 48,
                                 ['Henrietta', 'Millie', 'Lola', 'Florence', 'Moo Moo', 'Herman', 'Betsy', 'Milkshake',
                                  'Maggie', 'Oreo']),
                                (1007, 15, ['Millie', 'Lola', 'Florence', 'Moo Moo', 'Maggie']),
                                (876, 10, ['Florence', 'Lola', 'Maggie', 'Moo Moo'])]
        expected = ['Florence', 'Lola', 'Maggie', 'Moo Moo']
        # when
        result = self.find_best_solution(evaluated_partitions, space_limit)
        print(result)
        # then
        assert_that(result).is_equal_to(expected)


class TestGreedyCowTransport:

    @pytest.fixture(autouse=True)
    def prepare_greedy_cow_transport(self):
        self.greedy_cow_transport = greedy_cow_transport

    def test_greedy_cow_transport(self):
        assert False

    @pytest.fixture(autouse=True)
    def prepare_sort_cows(self):
        self.sort_cows = sort_cows

    def test_sort_cows(self):
        # given
        cows = {'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3, 'Milkshake': 2, 'Millie': 5, 'Lola': 2, 'Florence': 2, 'Henrietta': 9}
        expected = {'Betsy': 9, 'Henrietta': 9, 'Herman': 7, 'Oreo': 6, 'Millie': 5, 'Maggie': 3, 'Moo Moo': 3,
                    'Milkshake': 2, 'Lola': 2, 'Florence': 2}
        # when
        result = self.sort_cows(cows)

        #then
        assert_that(result).is_equal_to(expected)


