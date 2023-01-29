# import builtins
# import unittest
# import mock
# class Cal(object):
#     def __init__(self):
#         print("sudheer")
#         super().__init__()
#
#     def add(self):
#         return 10
#
# class Cal2(object):
#     def __init__(self):
#         super().__init__()
#         print("hanvi")
#
#     def add(self):
#         return 20
#
# class Caltesting(Cal2,Cal):
#
#     def __init__(self):
#         print("Tanuz")
#         super().__init__()
#
#     # def add(self):
#     #     return 30
#
#     def call_plus(self):
#         return self.add()
#
#
# obj =  Caltesting()
# #print(Caltesting.__mro__)
# #print(obj.call_plus())
# #print(Caltesting.__mro__)
#
# class Parser:
#
#     def html(self):
#         print("class html")
#
# def html_parser(self):
#     print("html parser")
#
# Parser.html =  html_parser
#
# s = Parser()
# s.html()
#
import builtins


def add():
     a =  input()
     b = input()
     return a+b

import unittest
import mock

class addtest(unittest.TestCase):

    @mock.Mock(builtins.input, return_value=10)
    def test(self):
        print(19)
        mock.sentinel[10,20]
        actual = add()
        expected = 30
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

