class BinarySearch:

    """
    A class that performs the binary search algorithm on an ordered list of integers to find a specified target integer.

    Attributes:
    - ordered_list (list[int]): A list of integers that must be sorted in ascending order.
    - target (int): The integer that we want to find within the ordered list.
    - lower_bound (int): The lower bound of the search range.
    - upper_bound (int): The upper bound of the search range.
    - mid_point (int): The index of the midpoint of the search range.
    - is_found (bool): The status of whether the target has been found in the ordered list.

    Methods:
    - index_of_target(self) -> int: Returns the index of the target in the ordered list.
    - find_mid_point(self, lower_bound: int, upper_bound: int) -> int: Finds the midpoint index between the lower bound and upper bound.
    - run(self, loop: bool = True) -> bool: Runs the binary search algorithm to find the target.
    """

    def __init__(self, ordered_list: list[int], target: int):

        """
        Initialize a BinarySearch object.

        Args:
        - ordered_list (list[int]): A list of integers that must be sorted in ascending order.
        - target (int): The integer that we want to find within the ordered list.

        Raises:
        - ValueError: If the ordered list is not sorted in ascending order or if the target is not present in the list.
        """

        self._ordered_list = self._check_ordered_list_input(ordered_list)
        self._target = self._check_target_input(target, ordered_list)
        self._lower_bound = 0
        self._upper_bound = len(ordered_list) - 1
        self._mid_point = self.find_mid_point(self._lower_bound, self._upper_bound)
        self._is_found = False

    def _check_ordered_list_input(self, ordered_list):
        if ordered_list != sorted(ordered_list):
            unordered_list = ordered_list
            raise ValueError(
                f"List is not sorted. Binary Search only works with sorted lists\nList provided: {unordered_list} "
            )
        return ordered_list

    def _check_target_input(self, target, ordered_list):
        if target in ordered_list:
            return target
        else:
            raise ValueError(
                f"Target is not present within the ordered list \
                \nOrdered List: {ordered_list}\nTarget: {target}"
            )

    @property
    def ordered_list(self) -> list[int]:

        """
        Get the ordered list.

        Returns:
        - list[int]: The ordered list.
        """
        return self._ordered_list

    @ordered_list.setter
    def ordered_list(self, new_ordered_list: list[int]) -> None:
        """
        Set a new ordered list.

        Args:
        - new_ordered_list (list[int]):  The ordered list.

        Raises:
        - ValueError: If the new ordered list is not sorted in ascending order.
        """
        self._check_ordered_list_input(new_ordered_list)
        self._ordered_list = new_ordered_list

    @property
    def target(self) -> int:
        """
        Get the target integer.

        Returns:
        - int: The target integer.
        """
        return self._target

    @target.setter
    def target(self, new_target: int) -> None:
        """
        Set a new target integer.

        Args:
        - new_target (int): A new integer that we want to find within the ordered list.

        Raises:
        - ValueError: If the new target is not present in the ordered list.
        """
        self._check_target_input(new_target, self.ordered_list)
        self._target = new_target

    @property
    def lower_bound(self) -> int:
        """
        Get the lower bound of the search range.

        Returns:
        - int: The lower bound of the search range.
        """
        return self._lower_bound

    @lower_bound.setter
    def lower_bound(self, new_lower_bound: int) -> None:
        """
        Set a new lower bound for the search range.

        Args:
        - new_lower_bound (int): A new integer that is the lower bound of the search range.
        """
        self._lower_bound = new_lower_bound

    @property
    def upper_bound(self) -> int:
        """
        Get the upper bound of the search range.

        Returns:
        - int: The upper bound of the search range.
        """
        return self._upper_bound

    @upper_bound.setter
    def upper_bound(self, new_upper_bound: int) -> None:
        """
        Set a new upper bound for the search range.

        Args:
        - new_upper_bound (int): A new integer that is the upper bound
        """
        self._upper_bound = new_upper_bound

    @property
    def mid_point(self) -> int:
        """
        Get the midpoint index of the search range.

        Returns:
        - int: The index of the midpoint of the search range.
        """
        return self._mid_point

    @mid_point.setter
    def mid_point(self, new_mid_point: int) -> None:
        """
        Set a new midpoint index for the search range.

        Args:
        - new_mid_point (int): A new integer that is the index of the midpoint of the search range.
        """
        self._mid_point = new_mid_point

    @property
    def is_found(self) -> bool:
        """
        Get the status of whether the target was found.

        Returns:
        - bool: True if the target was found, False otherwise.
        """
        return self._is_found

    @is_found.setter
    def is_found(self, new_status: bool) -> None:
        """
        Set a new status of whether the target was found.

        Args:
        - new_status (bool): A new status of whether the target was found (True or False).
        """
        self._is_found = new_status

    def index_of_target(self) -> int:
        """
        Get the index of the target in the ordered list.

        Returns:
        - int: The index of the target in the ordered list.
        """
        return self.ordered_list.index(self.target)

    def find_mid_point(self, lower_bound: int, upper_bound: int) -> int:
        """
        Find the midpoint index between the lower bound and upper bound.

        Args:
        - lower_bound (int): The lower bound of the search range.
        - upper_bound (int): The upper bound of the search range.

        Returns:
        - int: The index of the midpoint between the lower and upper bounds.
        """
        return (lower_bound + upper_bound) // 2

    def run(self, loop: bool = True) -> bool:

        """
        Run the binary search algorithm to find the target.

        Args:
        - loop (bool): If True, run the search in a loop until the target is found or the search range is exhausted.
            If False, run a single iteration of the search.

        Returns:
            bool
        """

        if loop:

            while self.lower_bound <= self.upper_bound:
                self.mid_point = self.find_mid_point(self.lower_bound, self.upper_bound)
                if self.ordered_list[self.mid_point] < self.target:
                    self.lower_bound = self.mid_point + 1

                elif self.ordered_list[self.mid_point] > self.target:
                    self.upper_bound = self.mid_point - 1

                else:
                    return self.mid_point

        else:
            self.mid_point = self.find_mid_point(self.lower_bound, self.upper_bound)
            if self.ordered_list[self.mid_point] < self.target:
                self.lower_bound = self.mid_point + 1
                return self.is_found
            elif self.ordered_list[self.mid_point] > self.target:
                self.upper_bound = self.mid_point - 1
                return self.is_found
            else:
                self.is_found = True
                return self.is_found
