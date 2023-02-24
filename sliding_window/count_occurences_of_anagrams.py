def count_anagram_occurances(pat, txt):
    '''
    txt = forxxorfxdofr
    pat = for
    '''
    k = len(pat)
    pat_freq = {}

    for i in pat:
        if i in pat_freq:
            pat_freq[i] += 1
        else:
            pat_freq[i] = 1
    l, r, count, res = 0, 0, len(pat_freq), []

    while r < len(txt):
        # calculation
        if txt[r] in pat_freq:
            pat_freq[txt[r]] -= 1
            if pat_freq[txt[r]] == 0:
                count -= 1
        if r - l + 1 < k:
            r += 1
        elif r - l + 1 == k:
            # find ans from calculation
            if count == 0:
                # res += 1
                res.append(l)
            if txt[l] in pat_freq:
                
                pat_freq[txt[l]] += 1
                if pat_freq[txt[l]] > 0:
                    count += 1
            # slide
            r += 1
            l += 1
    return res