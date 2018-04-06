#!python
# coding: utf-8
print("Content-Type: text/html; charset=utf-8\n")
import cgi, urllib.request, re, urllib.parse
data = cgi.FieldStorage()

url = "http://www.op.gg/summoner/userName="

#url2 = "http://localhost:8080/Servlet/ex/list.jsp?"

realUrl = ""
file_dir = "C:/Apache24/htdocs/OPG/recode.txt"
root_dir = "C:/Apache24/htdocs/OPG/"


readData = ""
userID = ""
ranking = ""
percent = ""  
tierInfo = ""
leaguePoint = ""
leagueInfo = ""
winRatio = ""

if "userName" in data:
    param = urllib.parse.quote_plus(data["userName"].value)
    realUrl = url + param
    #readData = urllib.request.urlopen(realUrl).read()
    readData = urllib.request.urlretrieve(realUrl, file_dir)
    userID = urllib.parse.unquote_plus(param, encoding="utf8")

with open(file_dir, "r", encoding="utf8") as f: 
    readData = f.read()

tierList = re.findall(r"(\<span class=\"tierRank\"\>)([\s\S]+?)(\<\/span\>)", readData)
for tier in tierList:
    tierInfo = tier[1]
    #print("당신의 티어는 "+ temp + "입니다.")

winRatioList = re.findall(r"(<div class=\"Text\">)([\s\S]+?)(</div>)", readData)
for winRatio in winRatioList:
    winRatio = winRatio[1]
    #print("최근 20게임 승률? "+a)

leagueName = re.findall(r"(\<div class=\"LeagueName\"\>)([\s\S]+?)(\<\/div\>)", readData)
for leagueNM in leagueName:
    leagueInfo = leagueNM[1]
    #print("<br> 당신의 리그는" + lnm + "입니다.")

LeaguePoints = re.findall(r"(\<span class=\"LeaguePoints\"\>)([\s\S]+?)(\<\/span\>)",readData)
for point in LeaguePoints :
    leaguePoint = point[1]

#print("<br>당신의 리그 점수는 :" + temp + "입니다.")

LedderRanking = re.findall(r"(\<span class=\"ranking\"\>)([\s\S]+?)(\<\/span\>)([\s\S]+?)(\<\/a\>)", readData)
for ranking in LedderRanking:
    ranking = ranking[1]
    percent = ranking[3]

#print("<br>당신의 래더랭킹은 : " + temp +"  상위"+temp2 +  "입니다.")

profileIcon = re.findall(r"(\<img.*?class\=\"ProfileImage\"\>)", readData)
tierImg = re.findall(r"(\<img.*?class\=\"Image\"\>)", readData)




with open(root_dir+"sample.html", "r", encoding="utf8") as f:
    ranking = ranking == "" and "랭킹이 없습니다." or ranking
    percent = percent == "" and "순위권 밖입니다." or percent
    leaguePoint = leaguePoint == "" and "0" or leaguePoint
    tierImg = tierImg[2]




html = '''
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" type="text/css" href="sample.css">
    </head>
    <body>
        <div class="content_con">
            <h1>&lt;소환사 검색결과&gt;</h1>
            <div class="top_con">
                <div class="profileIcon">
                    {profileIcon}
                </div>
                <div class="userID titleP">
                    <p>유저아이디</p>
                    <p class="realP">{userID}</p>
                </div>
                <div class="ranking titleP">
                    <p>래더랭킹</p>
                    <p class="realP">{ranking} 상위 {percent}입니다.</p>
                </div>
            </div>
            <div class="bottom_con">
                <div class="tierImg">
                    {tierImg}
                </div>
                <div class="tierInfo titleP">
                    <p>티어정보</p>
                    <p class="realP">{tierInfo}</p>
                </div>
                <div class="leaguePoint titleP">
                    <p>리그포인트</p>
                    <p class="realP">{leaguePoint}</p>
                </div>
                <div class="leagueInfo titleP">
                    <p>리그정보</p>
                    <p class="realP">{leagueInfo}</p>
                </div>
                <div class="winRatio titleP">
                    <p>승률</p>
                    <p class="realP">{winRatio}</p>
                </div>
            </div>
            <br>
        <!-- 티어, 승률, 리그, 리그포인트, 레더랭킹, 프로필이미지, 아이디, 티어이미지-->
        <a href="http://192.168.1.120/OPG">처음으로</a>
        </div>
        
    </body>
</html>
'''.format(profileIcon=profileIcon[0], userID=userID, ranking=ranking, percent=percent, tierImg=tierImg, tierInfo=tierInfo, leaguePoint=leaguePoint, leagueInfo=leagueInfo, winRatio=winRatio)


print(html)
