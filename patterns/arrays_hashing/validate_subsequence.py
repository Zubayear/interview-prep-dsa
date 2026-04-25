def is_valid_sequence(array, sequence):
    seq_idx = 0
    for value in array:
        if seq_idx == len(sequence):
            return True
        if sequence[seq_idx] == value:
            seq_idx += 1
    return seq_idx == len(sequence)
