import requests
import urllib.request
import json
import threading

def SourceJSON(query, perpage, page_no):
    URL = "https://unsplash.com/napi/search/photos?query=" + query + "&xp=&per_page=" + str(perpage) + "&page=" + str(page_no)
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    xJSON = requests.get(URL)
    return xJSON.json()
def getTotalPages(query, perpage):
    for_total_pages = SourceJSON(query, perpage, 1)
    total_pages = for_total_pages['total_pages']
    return total_pages
def downIDM(query, perpage, FROM, TO):
    queryTXT = open(query+".txt", "a+")
    for page_no in range(FROM, TO):
        pageJSON = SourceJSON(query, perpage, page_no)
        list_of_results = pageJSON['results']
        for pic_result in list_of_results:
            downloadURL = pic_result['urls']['raw']
            authorNAME = pic_result['user']['username']
            if pic_result['alt_description']:
                picNAME = pic_result['alt_description'].upper()
            else:
                picNAME = pic_result['id']

            if "fm=png" in pic_result['urls']['full']:
                exIMG = ".png"
            else:
                exIMG = ".jpg"
            namedURL = downloadURL+"&dl="+picNAME+" by "+authorNAME+exIMG
            queryTXT.write(namedURL+"\n")
        print("Links from page #%s has been copied"%(page_no))
