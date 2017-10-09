data = {
    "value": 0,
    "children": [
        {
            "value": 1,
            "children": [
                {"value": 2},
                {"value": 3}
            ]
        },
        {
            "value": 4,
            "children": [
                {
                    "value": 5,
                    "children": [
                        {"value": 6}
                    ]
                },
                {
                    "value": 7,
                    "children": [
                        {"value": 8}
                    ]
                },
                {"value": 9}
            ]
        },
        {"value": 10}
    ]
}

def DFS(element, key):
    if element["value"] == key:
        return element

    if "children" in element:
        for child in element["children"]:
            temp = DFS(child, key)
            if temp != False:
                return temp

    return False

DFS(data, 1)
DFS(data, 99)
