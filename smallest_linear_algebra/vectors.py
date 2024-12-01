import math
from typing import List,Union
from sys import exit

class row_vector:
    def __init__(self,array : List[Union[int,float]]):
        ''' Initializes an array of elements as list for row vector

        :param array: list[int] - accepts list of int values
        '''
        self.array = [float(x) for x in array]
        self.dimension = len(self.array)
        self.shape = (self.dimension,1)

    def l2_norm(self) -> float:
        '''L2 norm implementation
        
        :returns: float - length of given vector
        '''
        return math.sqrt(sum(x**2 for x in self.array))
    
    def transpose(self):
        '''Tranposing row vector into a column vector'''
        pass

    def __repr__(self) -> str:
        return f"Row Vector : ({self.array})"
    

class Vector:
    def __init__(self,array: List[Union[int,float]]):
        ''' Initializes an array of elements as list for column vector

        :param array: list[int] - accepts list of int values
        '''
        if self.is_it_column_wise(array):
            self.array = array

        self.dimension = len(array)
        self.element_wise = self.get_element_wise()
    
    def is_it_column_wise(self,array:list[int]) -> bool:
        '''
        This function checks whether the given array is column wise 
        and has only 1 element so it becomes a column vector
        :param array: list[int] - accepts list of int values
        :returns: bool - whether the given array is vector or not
        '''
        try:
            result = all(isinstance(i,list) for i in array if len(i) == 1)
        except Exception as e:
            print(f"Vector needs [{array}], but got {array}")
            exit(0)
            
        return result
    
    def get_element_wise(self) -> List[Union[int,float]]:
        return [element[0] for element in self.array]
    
    def l2_norm(self) -> float:
        return math.sqrt(sum(x**2 for x in self.element_wise))
    
    def transpose(self):
        pass

    def __repr__(self) -> str:
        return f"Vector : ({self.array})\ndefault - Column Vector"