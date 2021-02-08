def reverse(input, reverse_build = ''):
    if len(input) == 0:
        return reverse_build

    # build destination bucket and deplete source bucket
    new_reverse_build = input[0] + reverse_build
    new_input = input[1:]

    return reverse(new_input, new_reverse_build)

print(reverse('reverse'))