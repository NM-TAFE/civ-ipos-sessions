# 4D structure: List of Dicts -> List -> Dict -> Values
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

# Traversing the 4D structure
for i, dictionary in enumerate(data):  # Loop through the list of dictionaries
    for key, sublist in dictionary.items():  # Loop through dictionary keys and lists
        for j, subdict in enumerate(sublist):  # Loop through the list of dictionaries
            for sub_key, value in subdict.items():  # Loop through dictionary items
                print(f"data[{i}]['{key}'][{j}]['{sub_key}'] = {value}")
