def solution(today, terms, privacies):
    res = list()
    terms_dic = dict()
    t_list = today.split('.')
    t_year = int(t_list[0])
    t_month = int(t_list[1])
    t_day = int(t_list[2])

    for t in terms:
        tmp = t.split(' ')
        terms_dic[tmp[0]] = tmp[1]

    for i in range(len(privacies)):
        p_list = privacies[i].split('.')
        p_year = int(p_list[0])
        p_month = int(p_list[1])

        date_term = p_list.pop().split(' ')
        p_day = int(date_term[0])
        p_term = date_term[1]

        duration = int(terms_dic[p_term])
        d_year = duration // 12
        d_month = duration % 12

        end_year = p_year + d_year
        end_month = p_month + d_month
        end_day = p_day - 1

        if end_month > 12:
            end_month %= 12
            end_year += 1

        if end_day < 1:
            if end_month == 1:
                end_month = 12
                end_year -= 1
            else:
                end_month -= 1
            end_day = 28

        if t_year > end_year:
            res.append(i + 1)

        elif t_year == end_year and t_month > end_month:
            res.append(i + 1)

        elif t_year == end_year and t_month == end_month and t_day > end_day:
            res.append(i + 1)

    res.sort()
    return res
