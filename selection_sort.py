def selection_sort(integers_to_sort):
    """
    Implementation of the selection sort algorithm.
    """
    for slot in range(len(integers_to_sort) - 1, 0, -1):
        max_position = 0
        for location in range(1, slot + 1):
            if integers_to_sort[location] > integers_to_sort[max_position]:
                max_position = location

        temp = integers_to_sort[slot]
        integers_to_sort[slot] = integers_to_sort[max_position]
        integers_to_sort[max_position] = temp

    print(f"Sorted: {integers_to_sort}")


if __name__ == "__main__":
    selection_sort(
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
