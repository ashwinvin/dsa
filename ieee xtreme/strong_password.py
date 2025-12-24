def minimumNumber(n, password):
    conditions = [False] * 4

    for el in password:
        if not conditions[0] and el.isupper():
            conditions[0] = True
        elif not conditions[1] and el.islower():
            conditions[1] = True
        elif not conditions[2] and el.isdigit():
            conditions[2] = True
        elif not conditions[3] and el in "!@#$%^&*()-+":
            conditions[3] = True

    num_pre_conds = len([a for a in conditions if not a])
    print(len(password) - 6)
    print(num_pre_conds)
    min_nums = max(len(password) - 6, num_pre_conds)

    return min_nums


print(minimumNumber(3, "Ab1"))
