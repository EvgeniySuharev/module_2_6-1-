def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(2, 'string', False)
print_params(15, 'str')
print_params(c=False)
print_params(b='новая строка', c=False)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [12, 'string', (1, 2)]
values_dict = {'a': 'one', 'b': True, 'c': 3.14}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [3.14, 'string']
print_params(*values_list_2, 42)
