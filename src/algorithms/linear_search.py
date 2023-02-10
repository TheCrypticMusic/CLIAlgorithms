class LinearSearch:

    def __init__(self, list, target):
        self._list = list
        self._target = target
        self._is_found = False

    @property
    def list(self):
        if len(self._list) < 0:
            raise ValueError(f"Empty list provided")
        return self._list
    
    @list.setter
    def list(self, new_list):
        self._list = new_list