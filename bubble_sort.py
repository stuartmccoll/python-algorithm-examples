def bubble_sort(integers_to_sort):
    """
    Implementation of the bubble sort algorithm.
    """
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        print(integers_to_sort)
        for idx, item in enumerate(integers_to_sort[:-1]):
            if integers_to_sort[idx] > integers_to_sort[idx + 1]:
                sort(integers_to_sort, idx, idx + 1)
                is_sorted = False
        print("List after bubble sorting: {}".format(integers_to_sort))


def sort(incoming_list, b, c):
    """
    Sort two items into the correct order.
    """
    print(
        "Swapping order of item {} and item {}".format(
            incoming_list[b], incoming_list[c]
        )
    )
    temp = incoming_list[b]
    incoming_list[b] = incoming_list[c]
    incoming_list[c] = temp
    return incoming_list


if __name__ == "__main__":
    bubble_sort(
        [
            224231,
            6022641,
            69145,
            4620850,
            9291768,
            4635909,
            7135129,
            2124532,
            167599,
            5099268,
            9963337,
            6464161,
            1224576,
            612252,
            5800304,
            3431366,
            6168911,
            332445,
            5353615,
            4127839,
            8759185,
            2650205,
            7730538,
            5593380,
            3167304,
            3824544,
            3003204,
            403594,
            277686,
            2011089,
            5101658,
            2921801,
            4193880,
            637927,
            7532851,
            4287132,
            6502416,
            3889159,
            9290923,
            3028257,
            1753891,
            5142597,
            7488330,
            2268979,
            8894074,
            4819985,
            4459282,
            733245,
            3013731,
            7264664,
        ]
    )

