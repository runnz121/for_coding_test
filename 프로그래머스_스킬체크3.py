import re

def solution(word, pages):
    answer = 0
    idx = {}
    score = {}
    link = {}

    for i in range(len(pages)):
        lp = pages[i].lower()
        #print(lp)
        #  ([\S]*) -> 이렇게 소괄호 해준 부분이 그룹핑 1번 부분 전체가 그룹핑 0번부분
        url = re.search(r'<meta[^>]*content="https://([\S]*)"/>',lp).group(1)
        idx[url] = i
        wordCnt = 0
        for find in re.findall(r'[a-zA-Z]+',lp):
            if find == word:
                wordCnt += 1
        s = set()
        for e in re.findall(r'<a href="https://[\S]*">',lp):
            s.add(re.search(r'"https://([\S]*)"',e).group(1))
        s = list(s)
        score[url] = list()
        score[url].append(wordCnt)
        score[url].append(len(s))

        for e in s:
            if e not in link:
                link[e] = list()
            link[e].append(url)
    result = []
    for k, v in score.items():
        scores = v[0]
        if k in link:
            for u in link[k]:
                scores += score[u][0] / score[u][1]
        result.append([scores, idx[k]])


    #print(sorted(result, reverse=True, key=lambda x: (x[0], x[1])))
    return sorted(result, reverse=True, key=lambda x: (x[0], x[1]))[0][1]

word = 'blind'
word1 = 'Muzi'
pages =["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
pages1=["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
solution(word, pages)

# 기본점수 : 텍스트에 검색어가 등장하는 횟수
# 외부링크 수 : 현재 웹페이지에서 다른 외부페이지로 연결된 링크갯수
# 링크점수 : 기본점수 // 외부링크수 -> 다른 웹페이지에서 이 웹피이지로 링크가 걸렸는데, 그 다른 웹피이즈의 기분점수 + 외부링크수의 합
# 매칭점수 : 기본점수 + 링크점수