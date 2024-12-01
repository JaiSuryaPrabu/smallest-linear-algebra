from math import acos,pi
from vectors import row_vector,Vector
from typing import Union,List

PI = pi

def row_addition(a:row_vector,b:row_vector) -> row_vector:
    '''
    Vector-Vector addition for row vectors

    :param a: Vector - First vector array
    :param b: Vector - Second vector array
    :returns: Vector - Addition result of two vectors 
    '''
    result = list()
    for _,(value_a,value_b) in enumerate(zip(a.array,b.array)):
        result.append(value_a+value_b)
    return row_vector(result)
    

def row_scalar_multiplication(scalar : Union[int,float], vector : row_vector) -> row_vector :
    ''' 
    Scalar-Vector Multiplication

     :param scalar: int - value for multiplied with an vector
    :param vector: RowVector - row vector
    :returns: RowVector - returns the scaled row vector
    '''
    return row_vector([scalar * value for value in vector.array])


def row_dot_product(a:row_vector,b:row_vector) -> int:
    '''
    Vector-Vector Multiplication for Row Vector

     :param a: Vector - First vector array
    :param b: Vector - Second vector array
    :returns: int - Dot product of two vectors
    '''
    if a.dimension != b.dimension:
        # Same dimensions of vectors only used for dot product
        return None
    
    value = 0

    for _,(a_element,b_element) in enumerate(zip(a.array,b.array)):
        value += a_element * b_element
    
    return value


def row_angle(a:row_vector,b:row_vector) -> float:
    '''Angle between two row vectors

     :param a: Vector - First vector array
    :param b: Vector - Second vector array
    :returns: int - Angle between two vectors
    '''
    cos_theta = row_dot_product(a=a,b=b) / (a.l2_norm() * b.l2_norm())
    inv_cos = acos(cos_theta)
    degree = inv_cos * (180/PI)
    return degree


def addition(a:Vector,b:Vector) -> Vector:
    '''
    Vector-Vector addition for column vectors

     :param a: Vector - First vector array
    :param b: Vector - Second vector array
    :returns: Vector - Addition result of two vectors 
    '''
    result = list()
    for _,(value_a,value_b) in enumerate(zip(a.element_wise,b.element_wise)):
        result.append([value_a+value_b])
    return Vector(result)


def scalar_multiplication(scalar : Union[int,float], vector : Vector) -> Vector :
    ''' 
    Scalar-Vector Multiplication

     :param scalar: int - value for multiplied with an vector
    :param vector: 
    '''
    return Vector([[scalar * value] for value in vector.element_wise])


def dot_product(a:Vector,b:Vector) -> Union[int,float]:
    '''
    Vector-Vector Multiplication for Column Vector

     :param a: Vector - First vector array
    :param b: Vector - Second vector array
    :returns: int - Dot product of two vectors
    '''
    if a.dimension != b.dimension:
        # Same dimensions of vectors only used for dot product
        return None
    
    value = 0
    for _,(a_element,b_element) in enumerate(zip(a.element_wise,b.element_wise)):
        value += a_element * b_element
    
    return value


def angle(a:Vector,b:Vector) -> float:
    '''Angle between two column vectors
    
    :param a: Vector - First vector array
    :param b: Vector - Second vector array
    :returns: int - Angle between two vectors
    '''
    
    return (acos(dot_product(a=a,b=b) / (a.l2_norm() * b.l2_norm()))) * (180/PI)

def cross_product(a : Vector,b : Vector) -> Vector:
    ''' Cross product between two column vectors

    :param a: Vector - First vector array
    :param b: Vector - Second vector array
    :returns: Vector - Cross product of two vectors
    '''
    if a.dimension == 2 and b.dimension == 2:
        # 2D cross product
        a = a.element_wise
        b = b.element_wise

        result = (a[0]* b[1]) - (a[1]*b[0])
        return Vector([[result]])
    
    if a.dimension == 3 and b.dimension == 3:
        a = a.element_wise
        b = b.element_wise

        r1 = [a[1]*b[2]-a[2]*b[1]]
        r2 = [a[0]*b[2]-a[2]*b[0]]
        r3 = [a[0]*b[1]-a[1]*b[0]]

        return Vector([r1,r2,r3])