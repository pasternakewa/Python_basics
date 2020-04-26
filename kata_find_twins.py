# Given an array of integers, task is to find two same numbers and return one of them, for example in array [2, 3, 6, 34, 7, 8, 2] answer is 2.
# If there are no twins in the city - return None or the equivalent in the language that you are using.
"""
# tests:
Test.describe("elimination()")
Test.it("should pass some basic tests")
Test.assert_equals(elimination([2, 5, 34, 1, 22, 1]), 1, "twins are 1s")
Test.assert_equals(elimination([2, 2, 34, 1, 22]), 2, "twins are 2s")
Test.assert_equals(elimination([2, 5, 34, 1, 22]), None, "There are no twins in the city")
"""

def elimination(arr):
    twin_name = None
    for index, number in enumerate(arr):
        if number in arr[index + 1:]:
            twin_name = number
    return twin_name
