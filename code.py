def count(sequence):
    base_count = dict()
    for base in sequence:
        if base not in base_count:
            base_count[base] = 1
        else:
            base_count[base] += 1
    return base_count

def cal_freq(base_count):
    print('ACTG Frequency')
    total = float(sum([base_count[base] for base in base_count.keys()]))
    for base in base_count.keys():
        print(base + ':' + str(base_count[base]/total))

cal_freq(count('ATCTGACGCGCGCCGC'))
