class LinearSearch:
    """
    A class for performing linear search on a list of integers.

    Attributes:
        data (list): The list of integers to search through.
        target (int): The integer to search for.
        is_found (bool): A flag indicating whether or not the target was found.
        current_number (int): The current integer being compared to the target.
        data_index (int): The current index of the integer being compared.

    Methods:
        run(loop=True): Performs linear search on the list of integers.
            If loop is True (default), uses a for loop to iterate over the list.
            If loop is False, iterates over the list using the current_number and data_index attributes.
            Loop = False is to be used with the CLI.py file as it's used in a while loop within that file.
            Returns True if target is found, False otherwise.
    """

    def __init__(self, data: list, target: int):
        """
        Initialises a LinearSearch object with the provided data and target.

        Args:
            data (list): The list of integers to search through.
            target (int): The integer to search for.
        """
        self._data = data
        self._target = target
        self._is_found = False
        self._current_number = data[0]
        self._data_index = 0

    @property
    def data(self) -> list:
        """
        The list of integers to search through.

        Raises:
            ValueError: If the list is empty.

        Returns:
            list: The list of integers to search through.
        """
        if len(self._data) < 0:
            raise ValueError(f"Empty list provided")
        return self._data

    @data.setter
    def data(self, new_data: list) -> None:
        self._data = new_data

    @property
    def data_index(self) -> int:
        """
        The current index of the integer being compared.

        Raises:
            ValueError: If the index exceeds the length of the data list.

        Returns:
            int: The current index of the integer being compared.
        """
        if self._data_index > len(self.data):
            raise ValueError("Incorrect Index")
        return self._data_index

    @data_index.setter
    def data_index(self, new_index: int) -> None:
        self._data_index = new_index

    @property
    def is_found(self) -> bool:
        """
        A flag indicating whether or not the target was found.

        Returns:
            bool: True if target is found, False otherwise.
        """
        return self._is_found

    @is_found.setter
    def is_found(self, new_flag: bool) -> None:
        """
        Set a new status of whether the target was found.

        Args:
        - new_status (bool): A new status of whether the target was found (True or False).
        """
        self._is_found = new_flag

    @property
    def target(self) -> int:
        """
        The integer to search for.

        Returns:
            int: The integer to search for.
        """
        return self._target

    @target.setter
    def target(self, new_target: int) -> None:
        """
        Set a new target integer.

        Args:
        - new_target (int): A new integer that we want to find within the list
        """
        self._target = new_target

    @property
    def current_number(self) -> int:
        """
        The current integer being compared to the target.

        Returns:
            int: The current integer being compared to the target.
        """
        return self._current_number

    @current_number.setter
    def current_number(self, new_current_number: int) -> None:
        self._current_number = new_current_number

    @property
    def target_index(self) -> int:
        """
        The index of the target integer in the data list.

        Returns:
            int: The index of the target integer in the data list.
        """
        return self.data.index(self.target)

    def run(self, loop: bool = True) -> bool:

        if loop:
            for number in self.data:
                if number == self.target:
                    self.is_found = True
                    return self.is_found
            return False

        else:
            if self.current_number == self.target:
                self.is_found = True
                return self.is_found
            else:
                self.data_index += 1
                self.current_number = self.data[self.data_index]
