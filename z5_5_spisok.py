def del_elem(x: list):
    s1 = int(input("eliminated element :"))
    if x.count(s1) >= 2:
        return x.remove(s1)
    else:
        print("there are no such element in this list")


if __name__ == '__main__':
    del_elem()
