class TypedList:
    def __init__(self, list_type, initial_list=[]):
        self.list_type = type(list_type)
        if not isinstance(initial_list, list):
            raise TypeError("the second element of TypedList must be list")
        for element in initial_list:
            self.__check(element)
        self.elements = initial_list

    def __check(self, element):
        if self.list_type != type(element):
            raise TypeError("attempt element of TypedList must be a list")

    def __setitem__(self, key, element):
        self.__check(element)
        self.elements[key] = element

    def __getitem__(self, key):
        return self.elements[key]

    def __len__(self):
        return len(self.elements)

    def __delitem__(self, key):
        del self.elements[key]

    def append(self, element):
        self.__check(element)
        self.elements.append(element)

    def __str__(self):
        result = ''
        for element in self.elements:
            result += str(element) + ' '
        return result


