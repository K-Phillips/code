# lightlemmatizer.py

def lemmatize(token_list):

    out_tokens = []

    for t in token_list:
        if t.endswith('ies'):
            t = t[:-3] + 'y'
        elif t.endswith("'s"):
            t = t[:-2]
        elif (t.endswith('s') or t.endswith("s'")) and not t.endswith('us') and not t.endswith('as') and not t.endswith('ss') and not t.endswith('is'):
            if t.endswith('s'):
                t = t[:-1]
            elif t.endswith("s'"):
                t = t[:-2]
        elif t.endswith("'"):
            t = t[:-1]

        out_tokens.append(t)

    return out_tokens