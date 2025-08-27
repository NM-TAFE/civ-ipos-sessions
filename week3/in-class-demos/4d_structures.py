data = [
    {
        "group1": [
            {"id": 1, "value": "A"},
            {"id": 2, "value": "B"}
        ],
        "group2": [
            {"id": 3, "value": "C"},
            {"id": 4, "value": "D"}
        ]
    },
    {
        "group3": [
            {"id": 5, "value": "E"},
            {"id": 6, "value": "F"}
        ],
        "group4": [
            {"id": 7, "value": "G"},
            {"id": 8, "value": "H"}
        ]
    }
]

# Traversing(moving through) the structure
for i, dictionary in enumerate(data):  # list of dictionaries
    for key, sublist in dictionary.items():  # keys and lists
        for j, subdict in enumerate(sublist):  # list of dictionaries
            for sub_key, value in subdict.items():  # keys and values
                print(f"data[{i}]['{key}'][{j}]['{sub_key}'] = {value}")


def traverse(data, path="data"):
    match data:
        case dict():
            for key, value in data.items():
                traverse(value, f"{path}['{key}']")
        case list():
            for index, item in enumerate(data):
                traverse(item, f"{path}[{index}]")
        case _:
            # Default case, not a collection
            print(f"{path} = {data}")

traverse(data)