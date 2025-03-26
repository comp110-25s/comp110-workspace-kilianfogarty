"""Dictionary where functions skeletons will be implemented."""

__author__: str = "730803217"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Takes in a dictionary and switches the key and value"""
    inverted_dict: dict[str, str] = {}
    for key in input_dict:
        value = input_dict[key]
        if key in inverted_dict:
            raise KeyError("Key already in dictionary")
        inverted_dict[value] = key
    return inverted_dict


def count(input_list: list[str]) -> dict[str, int]:
    """Outputs dictionary where key is value from the list and value is the count"""
    output_dict: dict[str, int] = {}
    for i in input_list:
        if i in output_dict:
            output_dict[i] += 1
        else:
            output_dict[i] = 1
    return output_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Outputs color that appears most frequently in dictionary"""
    color_list: list[str] = []
    for key in color_dict:
        color_list.append(color_dict[key])
    color_dict2: dict[str, int] = count(color_list)
    highest_key: str = ""
    highest_value: int = 0
    for key in color_dict2:
        if color_dict2[key] > highest_value:
            highest_key = key
            highest_value = color_dict2[key]
    return highest_key


def bin_len(chosen_list: list[str]) -> dict[int, set[str]]:
    """Outputs dictionary that groups words of each length into sets"""
    return_dict: dict[int, set[str]] = {}
    for i in chosen_list:
        length = len(i)
        if length in return_dict:
            return_dict[length].add(i)
        else:
            return_dict[length] = set(i)
    return return_dict
