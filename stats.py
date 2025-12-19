
def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    n = 0
    o = 0
    p = 0
    q = 0
    r = 0
    s = 0
    t = 0
    u = 0
    v = 0
    w = 0
    x = 0
    y = 0
    z = 0
    space = 0
    period = 0
    comma = 0
    exclamation = 0
    question = 0
    for char in text:
        char = char.lower()
        if char == ' ':
            space += 1
        elif char == '.':
            period += 1
        elif char == ',':
            comma += 1
        elif char == '!':
            exclamation += 1
        elif char == '?':
            question += 1
        elif char == 'a':
            a += 1
        elif char == 'b':
            b += 1
        elif char == 'c':
            c += 1
        elif char == 'd':
            d += 1
        elif char == 'e':
            e += 1
        elif char == 'f':
            f += 1
        elif char == 'g':
            g += 1
        elif char == 'h':
            h += 1
        elif char == 'i':
            i += 1
        elif char == 'j':
            j += 1
        elif char == 'k':
            k += 1
        elif char == 'l':
            l += 1
        elif char == 'm':
            m += 1
        elif char == 'n':
            n += 1
        elif char == 'o':
            o += 1
        elif char == 'p':
            p += 1
        elif char == 'q':
            q += 1
        elif char == 'r':
            r += 1
        elif char == 's':
            s += 1
        elif char == 't':
            t += 1
        elif char == 'u':
            u += 1
        elif char == 'v':
            v += 1
        elif char == 'w':
            w += 1
        elif char == 'x':
            x += 1
        elif char == 'y':
            y += 1
        elif char == 'z':
            z += 1
    letters = {
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'e': e,
        'f': f,
        'g': g,
        'h': h,
        'i': i,
        'j': j,
        'k': k,
        'l': l,
        'm': m,
        'n': n,
        'o': o,
        'p': p,
        'q': q,
        'r': r,
        's': s,
        't': t,
        'u': u,
        'v': v,
        'w': w,
        'x': x,
        'y': y,
        'z': z,
        ' ': space,
        '.': period,
        ',': comma,
        '!': exclamation,
        '?': question
    }
    return letters

def sort_on(letters):
    return letters["num"]
        
def sorted_char_count(text):
    count_dict = char_count(text)
    sortedDicts = [
        {"char": "a", "num": count_dict['a']},
        {"char": "b", "num": count_dict['b']},
        {"char": "c", "num": count_dict['c']},
        {"char": "d", "num": count_dict['d']},
        {"char": "e", "num": count_dict['e']},
        {"char": "f", "num": count_dict['f']},
        {"char": "g", "num": count_dict['g']},
        {"char": "h", "num": count_dict['h']},
        {"char": "i", "num": count_dict['i']},
        {"char": "j", "num": count_dict['j']},
        {"char": "k", "num": count_dict['k']},
        {"char": "l", "num": count_dict['l']},
        {"char": "m", "num": count_dict['m']},
        {"char": "n", "num": count_dict['n']},
        {"char": "o", "num": count_dict['o']},
        {"char": "p", "num": count_dict['p']},
        {"char": "q", "num": count_dict['q']},
        {"char": "r", "num": count_dict['r']},
        {"char": "s", "num": count_dict['s']},
        {"char": "t", "num": count_dict['t']},
        {"char": "u", "num": count_dict['u']},
        {"char": "v", "num": count_dict['v']},
        {"char": "w", "num": count_dict['w']},
        {"char": "x", "num": count_dict['x']},
        {"char": "y", "num": count_dict['y']},
        {"char": "z", "num": count_dict['z']},
        {"char": " ", "num": count_dict[' ']},
        {"char": ".", "num": count_dict['.']},
        {"char": ",", "num": count_dict[',']},
        {"char": "!", "num": count_dict['!']},
        {"char": "?", "num": count_dict['?']}
    ]    
    sortedDicts.sort(key=sort_on, reverse=True)

    return sortedDicts
