from WS_Unsplash import *
import click
numTHREAD = 10
perpage = 99
@click.command()
@click.option('--query',required=True,  prompt='What do you want to download', help='Enter the query you needed to download')
def doThreading(query):
    global numTHREAD
    global perpage
    total_pages = getTotalPages(query, perpage)
    thr=[]
    if numTHREAD < total_pages:
        XXX = int(TO/numTHREAD)
    else:
        XXX = total_pages

    for i in range(0,total_pages+1,XXX):
        t1 = threading.Thread(target = downIDM, args=(query, perpage,i,i+XXX,))
        t1.start()
        thr.append(t1)
    for i in thr:
        i.join()

if __name__ == '__main__':
    doThreading()