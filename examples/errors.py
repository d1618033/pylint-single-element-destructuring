"""
    demo of destructuring which is NOT allowed
"""


def func():
    """
    function example
    """
    one_element = [17]

    [single_element_1] = one_element

    (single_element_2,) = one_element

    (single_element_3,) = one_element
    return single_element_1, single_element_2, single_element_3


class MyClass:
    """
    class example
    """

    def __init__(self, array):
        (self.single_element_4,) = array
        [self.single_element_5] = array
        (self.single_element_6,) = array
        self.array = array
        self.single_element_7 = None
        self.single_element_8 = None

    def public_method_1(self):
        """
        example method
        """
        (self.single_element_7,) = self.array

    def public_method_2(self):
        """
        example method
        """
        [self.single_element_8] = self.array
