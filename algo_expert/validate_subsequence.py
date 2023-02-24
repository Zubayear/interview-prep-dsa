

# def validate_subsequence(li1, li2):
#     if len(li1) == len(li2) == 0:
#         return True
#     if len(li2) > len(li1):
#         return False
#     result = False
#     ptr1, ptr2 = 0, 0
#     for i in range(0, len(li1)):
#         if li1[ptr1] != li2[ptr2]:
#             result = False
#             ptr1 += 1
#         else:
#             ptr1 += 1
#             ptr2 += 1
#             result = True
#     return result

def is_valid_sequence(array, sequence):
    seq_idx = 0
    for value in array:
        if seq_idx == len(sequence):
            return True
        if sequence[seq_idx] == value:
            seq_idx += 1
    return seq_idx == len(sequence)
