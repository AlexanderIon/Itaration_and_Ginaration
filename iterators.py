list_ = [ ['a', 'b', 'c'],
	      ['d', 'e', 'f', 'h', False],
	      [1, 2, None],
        ]



# for i in list_:
#     print(i)
#
#
# print("_________________")

# my_iter = iter(list_)
# if type(mu = next(my_iter) is list:
#         my = My
#
# print(type(next(my_iter)))
# print(type(next(my_iter)))
# print(type(next(my_iter)))
# print(type(next(my_iter)))

class Mylist(list):
    def __iter__(self):
        self.index_= 0
        self.index_1 = -1
        return self
    def __next__(self):
        while len(self) != self.index_:
            # print(len(self),self.index_)

            if type(self[self.index_]) is list:
                while self.index_1 < len(self[self.index_])-1:
                    self.index_1 += 1
                    # print(self.index_1)
                    return self[self.index_][self.index_1]
            self.index_1 = -1
            self.index_ += 1




        raise StopIteration


my = Mylist(list_)
flat_list = [item for item in my]

print(flat_list)

for i in my:
    print(i)

print("_________________")
