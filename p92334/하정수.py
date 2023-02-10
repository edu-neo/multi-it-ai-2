def solution(id_list, report, k):
    answer = []
    for i in id_list:
        answer.append(0)
    for idc in id_list:
        rep_set = set(report)
        count = 0
        for i in rep_set:
            if idc == i.split()[1]:
                count += 1
        if count >= k:
            for sent in range(len(id_list)):
                for re in rep_set:
                    re = re.split()
                    if idc == re[1]:
                        if id_list[sent] == re[0]:
                            answer[sent] += 1
            pass
    return answer

# def solution(id_list, report, k):
#     answer = [0] * len(id_list)
#     reports = {x : 0 for x in id_list}
#
#     for r in set(report):
#         reports[r.split()[1]] += 1
#
#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1
#
#     return answer

# def solution(id_list, report, k):
#     answer = [0 for _ in range(len(id_list))]
#     # 신고 내역
#     history = {}
#     # 신고 횟수
#     report_count = {}
#     for user in id_list:
#         report_count[user] = 0
#         history[user] = []
#
#     for from_to in report:
#         from_user, to_user = from_to.split()
#         if to_user not in history[from_user]:
#             history[from_user].append(to_user)
#             report_count[to_user] += 1
#
#     # enumerate => 리스트에서 idx와 값을 동시에 꺼내기
#     for idx, user in enumerate(id_list):
#         for report_user in history[user]:
#             if report_count[report_user] >= k:
#                 answer[idx] += 1
#
#
#     return answer



print(
    solution(
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
        2))