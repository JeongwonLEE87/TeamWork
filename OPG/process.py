#!python
# coding: utf-8
print("Content-Type: text/html; charset=utf-8\n")
import cgi, urllib.request, re, urllib.parse
data = cgi.FieldStorage()

url = "http://www.op.gg/summoner/userName="

#url2 = "http://localhost:8080/Servlet/ex/list.jsp?"

realUrl = ""
file_dir = "C:/Apache24/htdocs/OPG/recode.txt"

if "userName" in data:
    #print(data["userName"].value, "<br>")
    param = urllib.parse.quote_plus(data["userName"].value)
    realUrl = url + param
    #print(realUrl)
    urllib.request.urlretrieve(realUrl, file_dir)

readData = ""
temp = ""
temp2 = ""
with open(file_dir, "r", encoding="utf8") as f: 
    readData = f.read()

tierList = re.findall(r"(\<span class=\"tierRank\"\>)([\s\S]+?)(\<\/span\>)", readData)
for tier in tierList:
    temp = tier[1]
    print("당신의 티어는 "+ temp + "입니다.")

winRatioList = re.findall(r"(\<div id=\"WinRatioGraph\-summary\".*)(\<\/div>)([\s\S]+?)(\<\/div>)", readData)
for winRatio in winRatioList:
    a = winRatio[2].lstrip()
    print("<br>최근 20게임 승률? "+a)

leagueName = re.findall(r"(\<div class=\"LeagueName\"\>)([\s\S]+?)(\<\/div\>)", readData)
for leagueNM in leagueName:
    lnm = leagueNM[1]
    print("<br> 당신의 리그는" + lnm + "입니다.")

LeaguePoints = re.findall(r"(\<span class=\"LeaguePoints\"\>)([\s\S]+?)(\<\/span\>)",readData)
for point in LeaguePoints :
    temp = point[1]

print("<br>당신의 리그 점수는 :" + temp + "입니다.")

LedderRanking = re.findall(r"(\<span class=\"ranking\"\>)([\s\S]+?)(\<\/span\>)([\s\S]+?)(\<\/a\>)", readData)
for ranking in LedderRanking:
    temp = ranking[1]
    temp2 = ranking[3]

print("<br>당신의 래더랭킹은 : " + temp +"  상위"+temp2 +  "입니다.")
