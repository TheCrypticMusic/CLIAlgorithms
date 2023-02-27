class LinearSearch:

    def __init__(self, list: list, target: int):
        self._list = list
        self._target = target
        self._is_found = False
        self._current_number = list[0]
        self._list_index = 0

    @property
    def list(self) -> list:
        if len(self._list) < 0:
            raise ValueError(f"Empty list provided")
        return self._list
    
    @list.setter
    def list(self, new_list: list):
        self._list = new_list

    @property
    def list_index(self):
        if self._list_index > len(self.list):
            raise ValueError("Incorrect Index")
        return self._list_index

    @list_index.setter
    def list_index(self, new_index):
        self._list_index = new_index

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

    @property
    def current_number(self):
        return self._current_number
    
    @current_number.setter
    def current_number(self, new_current_number):
        self._current_number = new_current_number

    @property
    def target_index(self):
        return self.list.index(self.target)
    
    def run(self, loop: bool):

        if loop:
            pass
            ## For loop goes here
        else:
            if self.current_number == self.target:
                self.is_found = True
                return self.is_found
            else:
                self.list_index += 1
                self.current_number = self.list[self.list_index]
            
        


