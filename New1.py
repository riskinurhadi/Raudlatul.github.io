from tabulate import tabulate

data = [
    ['Cabai', '/kg', 25],
    ['Bawang merah', '/kg', 30],
    ['kunyit', '/kg', 35]
]

headers = ['Name', 'Gender', 'Age']

print(tabulate(data, headers))
