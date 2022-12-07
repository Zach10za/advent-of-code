
def get_data(key: int) -> list:
    with open(f'data/{key}.txt', 'r') as file:
        data = list(file.readlines())
    return data


def day_1a():
    return max([sum(map(int, s.split(','))) for s in ','.join([d.strip() for d in get_data(1)]).split(',,')])


def day_1b():
    return sum(sorted([sum(map(int, s.split(','))) for s in ','.join([d.strip() for d in get_data(1)]).split(',,')])[-3:])


def day_2a():
    return sum({'A X': 4, 'B X': 1, 'C X': 7, 'A Y': 8, 'B Y': 5, 'C Y': 2, 'A Z': 3, 'B Z': 9, 'C Z': 6}[d.strip()] for d in get_data(2))


def day_2b():
    return sum({'A X': 3, 'B X': 1, 'C X': 2, 'A Y': 4, 'B Y': 5, 'C Y': 6, 'A Z': 8, 'B Z': 9, 'C Z': 7}[d.strip()] for d in get_data(2))


def day_3a():
    return sum(sum('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(c) + 1 for c in set([c for c in r[:len(r)//2] if c in r[len(r)//2:]])) for r in get_data(3))


def day_3b():
    return (lambda data: sum(sum('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(c) + 1 for c in set([c for c in c1 if c in c2 and c in c3])) for c1, c2, c3 in [data[i:i+3] for i in range(0, len(data), 3)]))([d.strip() for d in get_data(3)])


def day_4a():
    return sum(1 for (a1, a2), (b1, b2) in [[list(map(int, c.split('-'))) for c in d.split(',')] for d in get_data(4)] if (a1 <= b1 and a2 >= b2) or (b1 <= a1 and b2 >= a2))


def day_4b():
    return sum(1 for (a1, a2), (b1, b2) in [[list(map(int, c.split('-'))) for c in d.split(',')] for d in get_data(4)] if (a1 <= b1 <= a2) or (a1 <= b2 <= a2) or (b1 <= a1 <= b2) or (b1 <= a2 <= b2))


def day_5a():
    return (lambda t: (lambda f, q, n: [n := f(n, s) for s in q][-1])(lambda p, k: p + k[0], (lambda f, q, n: [n := f(n, s) for s in q][-1])(lambda g, d: (lambda n, f, t: g[:f - 1] + [g[f - 1][n:]] + g[f:t - 1] + [g[f - 1][:n][::-1] + g[t - 1]] + g[t:] if t > f else g[:t - 1] + [g[f - 1][:n][::-1] + g[t - 1]] + g[t:f - 1] + [g[f - 1][n:]] + g[f:])(*map(int, filter(lambda x: x.isdigit(), d.split(' ')))), [g for g in t if g.startswith('m')], (lambda f, q, n: [n := f(n, s) for s in q][-1])(lambda a, b: [a[i] + b[i * 4 + 1].strip() if len(b) > i * 4 and b[i * 4 + 1].strip() else a[i] for i in range(len(a))], [d for d in t if '[' in d], ['' for _ in range(int([d.strip()[-1] for d in t if d.startswith(' 1')][0]))])), ''))([d.replace('\n', '') for d in get_data(5)])


def day_5b():
    return (lambda t: (lambda f, q, n: [n := f(n, s) for s in q][-1])(lambda p, k: p + k[0], (lambda f, q, n: [n := f(n, s) for s in q][-1])(lambda g, d: (lambda n, f, t: g[:f - 1] + [g[f - 1][n:]] + g[f:t - 1] + [g[f - 1][:n] + g[t - 1]] + g[t:] if t > f else g[:t - 1] + [g[f - 1][:n] + g[t - 1]] + g[t:f - 1] + [g[f - 1][n:]] + g[f:])(*map(int, filter(lambda x: x.isdigit(), d.split(' ')))), [g for g in t if g.startswith('m')], (lambda f, q, n: [n := f(n, s) for s in q][-1])(lambda a, b: [a[i] + b[i * 4 + 1].strip() if len(b) > i * 4 and b[i * 4 + 1].strip() else a[i] for i in range(len(a))], [d for d in t if '[' in d], ['' for _ in range(int([d.strip()[-1] for d in t if d.startswith(' 1')][0]))])), ''))([d.replace('\n', '') for d in get_data(5)])


def day_6a():
    return (lambda data: (lambda n: list(filter(lambda x: x[1], [(i+n, len(set([a for a in data[i:i+n]])) == n) for i in range(len(data) - n)]))[0][0])(4))(get_data(6)[0])


def day_6b():
    return (lambda data: (lambda n: list(filter(lambda x: x[1], [(i+n, len(set([a for a in data[i:i+n]])) == n) for i in range(len(data) - n)]))[0][0])(14))(get_data(6)[0])


def day_7a():
    return sum(filter(lambda x: x <= 100000, (lambda t, r=[{}], v=[[]]: (list(map(lambda l, r=r, v=v: (v.append((v[-1][:-1] if (b := l.split(' ')[2]) == '..' else v[-1] + [f'{b}/'])) if l.startswith('$') else None, r.append((r[-1] if (j := ''.join(v[-1])) in r[-1] else {**r[-1], j: 0}) if l.startswith('$') else {**r[-1], **dict(map(lambda j: (j, r[-1][j] + int(l.split(' ', 1)[0])), (lambda a: [a := a + p for p in v[-1]])('')))}), r[-1])[2], t))))([d.strip() for d in get_data(7) if d.split(' ', 1)[0].isdigit() or d.startswith('$ cd')])[-1].values()))


def day_7b():
    return (lambda q=(lambda t, r=[{}], v=[[]]: (list(map(lambda l, r=r, v=v: (v.append((v[-1][:-1] if (b := l.split(' ')[2]) == '..' else v[-1] + [f'{b}/'])) if l.startswith('$') else None, r.append((r[-1] if (j := ''.join(v[-1])) in r[-1] else {**r[-1], j: 0}) if l.startswith('$') else {**r[-1], **dict(map(lambda j: (j, r[-1][j] + int(l.split(' ', 1)[0])), (lambda a: [a := a + p for p in v[-1]])('')))}), r[-1])[2], t))))([d.strip() for d in get_data(7) if d.split(' ', 1)[0].isdigit() or d.startswith('$ cd')])[-1]: list(filter(lambda s: s >= 30000000 - (70000000 - q['//']), sorted(q.values())))[0])()


if __name__ == '__main__':
    print('day_1a', day_1a())
    print('day_1b', day_1b())
    print('day_2a', day_2a())
    print('day_2b', day_2b())
    print('day_3a', day_3a())
    print('day_3b', day_3b())
    print('day_4a', day_4a())
    print('day_4b', day_4b())
    print('day_5a', day_5a())
    print('day_5b', day_5b())
    print('day_6a', day_6a())
    print('day_6b', day_6b())
    print('day_7a', day_7a())
    print('day_7b', day_7b())
