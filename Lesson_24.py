# import pickle
#
# with open('data.pickle', 'rb') as f:
#     l = pickle.load(f)
#
# l1 = list(filter(lambda x: x % 3 == 0, l))
# print(sum(l1) / len(l1))


# dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}  # -> dict_2 = {'red': 3, 'green': 5, 'black': 5, 'white': 5}
# print({i: len(i) for i in dict_1.values()})


# d = {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}  # -> {'a': [1, 3, 7], 'b': [], 'c': [9, 9, 5]}
# for key, val in d.items():
#     d[key] = list(filter(lambda x: x % 2 != 0, val))
# print(d)

