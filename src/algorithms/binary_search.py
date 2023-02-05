class BinarySearch:

    def __init__(self, ordered_list: list[int], target: int) -> int:
        self._ordered_list = ordered_list
        self._target = target
        self._lower_bound = 0
        self._upper_bound = len(ordered_list) - 1
        self._mid_point = self.find_mid_point(self._lower_bound, self._upper_bound)
        self._is_found = False

    @property
    def ordered_list(self):
        return self._ordered_list
    
    @ordered_list.setter
    def ordered_list(self, new_ordered_list):
        self._ordered_list = new_ordered_list
    
    @property
    def target(self):
        return self._target
    
    @target.setter
    def target(self, new_target):
        self._target = new_target

    @property
    def lower_bound(self):
        return self._lower_bound
    
    @lower_bound.setter
    def lower_bound(self, new_lower_bound):
        self._lower_bound = new_lower_bound

    @property
    def upper_bound(self):
        return self._upper_bound
    
    @upper_bound.setter
    def upper_bound(self, new_upper_bound):
        self._upper_bound = new_upper_bound

    @property
    def mid_point(self):
        return self._mid_point
    
    @mid_point.setter
    def mid_point(self, new_mid_point):
        self._mid_point = new_mid_point

    @property
    def is_found(self):
        return self._is_found

    @is_found.setter
    def is_found(self, new_status):
        self._is_found = new_status

    def index_of_target(self):
        return self.ordered_list.index(self.target)


    def find_mid_point(self, lower_bound, upper_bound):
        return (lower_bound + upper_bound) // 2
    
    def run(self, loop: bool = True):

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
                self.is_found = False
                return self.is_found   
            elif self.ordered_list[self.mid_point] > self.target:
                self.upper_bound = self.mid_point - 1
                self.is_found = False
                return self.is_found   
            else:
                self.is_found = True
                return self.is_found