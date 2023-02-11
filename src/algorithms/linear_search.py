class LinearSearch:

    def __init__(self, list: list, target: int):
        self._list = list
        self._target = target
        self._is_found = False

    @property
    def list(self) -> list:
        if len(self._list) < 0:
            raise ValueError(f"Empty list provided")
        return self._list
    
    @list.setter
    def list(self, new_list: list):
        self._list = new_list

    @property
    def is_found(self) -> bool:
        return self._is_found
    
    @is_found.setter
    def is_found(self, new_flag):
        self._is_found = new_flag

    @property
    def target(self) -> int:
        return self._target

    @target.setter
    def target(self, new_target):
        self._target = new_target
    
    def run(self):
        for number in self.list:
            if number == self.target:
                self.is_found = True
                return self.is_found
        return -1


