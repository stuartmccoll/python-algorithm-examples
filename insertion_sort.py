def insertion_sort(integers_to_sort):
	"""
	Implementation of the insertion sort algorithm.
	"""

    for idx in range(1, len(integers_to_sort)):
        current_item = integers_to_sort[idx]
        position = idx

        print(f"Current item is: {current_item} and position is: {position}")

        while position > 0 and integers_to_sort[position - 1] > current_item:
            print(f"Item at {position - 1} is > than {current_item}")
            integers_to_sort[position] = integers_to_sort[position - 1]
            print(f"Item at {position} is now {integers_to_sort[position - 1]}")
            position = position - 1

        integers_to_sort[position] = current_item

    print(f"Sorted list: {integers_to_sort}")


if __name__ == "__main__":
    insertion_sort(
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
