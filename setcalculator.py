# question = int(input('How many set objects do you want to have? (0-5) '))
# if question > 0 and question <= 5:
#     for values in range(question):
#         set_values = set(input('Enter the values of your set object >>> '))
#         union_set = set_values.union()
#         print(union_set)

# else:
#     print('You have exceeded the range of numbers you were given')

# set_value1 = set(input('Enter the first value: '))
# set_value2 = set(input('Enter the second value: '))

# union_set = set_value1.union(set_value2)
# intersection_set = set_value1.intersection(set_value2)
# difference_set = set_value1.difference(set_value1)
# disjoint_set = set_value1.isdisjoint(set_value2)
# subset_set = set_value1.issubset(set_value2)
# superset_set = set_value1.issuperset(set_value2)

# print(f'''
#             The union is : {union_set}
#             The intersection is : {intersection_set}
#             The difference is : {difference_set}
#             The disjoint is : {disjoint_set}
#             The subset is : {subset_set}
#             The superset is : {superset_set}
# ''')
# list_of_sets = []
# num_of_sets = int(input('How man number of sets do you want to work with? '))
# for each in range(1, num_of_sets+1):
#     set_items= []
#     items = int(input(f'How many values do you want your set{each} to have? '))
#     for values in range(1, items+1):
#         item = input(f'Enter your value{values}: ')
#         set_items.append(item)
#     list_of_sets.append(set_items)
# # set_list = set(list_of_sets)
# union_set = set.union(*({list_of_sets,}))
# print(union_set)

list_of_sets = []
num_of_sets = int(input('How man number of sets do you want to work with? '))
for each in range(1, num_of_sets+1):
    set_items= []
    items = int(input(f'How many values do you want your set{each} to have? '))
    for values in range(1, items+1):
        item = input(f'Enter your value{values}: ')
        set_items.append(item)
    set_box = set(set_items)
    list_of_sets.append(set_box)
    intersection_set = set.intersection(*list_of_sets)
    union_set = set.union(*list_of_sets)
    difference_set = set.difference(*list_of_sets)
    # subset_set = set.issubset(*list_of_sets)
    # disjoint_set = set.isdisjoint(*list_of_sets)
    # superset_set = set.issuperset(*list_of_sets)
print(f'''
            This is the union of the sets: {union_set}
            This is the intersection of the sets: {intersection_set}
            This is the difference of the sets: {difference_set}
''')