# class MyConverter:
#     __money_sum = 0
#     __uag_rate = 42.2
#     __converter_direction = 1

#     def __init__(self, input_money, convert_dir):
#         self.money_sum = input_money
#         self.converter_direction = convert_dir

#     @property
#     def converter_direction(self):
#         return self.__converter_direction
    
#     @converter_direction.setter
#     def converter_direction(self, convert_dir):
#         if convert_dir == 1 or convert_dir == 2:
#             self.__converter_direction = convert_dir
#         else:
#             raise Exception("Provide correct converter direction")
        
#     @property
#     def money_sum(self):
#         return self.__money_sum
    
#     @money_sum.setter
#     def money_sum(self, input_money):
#         if 0 < input_money < 1000000:
#             self.__money_sum = input_sum
#         else:
#             raise Exception("Provide correct money sum")
        
#     @property