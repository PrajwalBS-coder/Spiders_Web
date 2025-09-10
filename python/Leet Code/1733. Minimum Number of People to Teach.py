n = 2
languages = [[2],[1,3],[1,2],[3]]
friendships =[[1,4],[1,2],[3,4],[2,3]]
need = set()
for u, v in friendships:
    u -= 1 #to get index of list languages we subtract 1
    v -= 1 #to get index of list languages we subtract 1
    ok = False #check if there is a common language
    for x in languages[u]:
        if x in languages[v]:
            ok = True
            break
    if not ok:
        need.add(u)
        need.add(v)

ans = len(languages) + 1
for i in range(1, n + 1):
    cans = 0
    for v in need:
        if i not in languages[v]:
            cans += 1
    ans = min(ans, cans)
print(ans)