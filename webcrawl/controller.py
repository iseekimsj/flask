from webcrawl.assembly import AssemblyCrawler
from webcrawl.bugmusic import BugsCrawler
from webcrawl.naver import NaverCrawler
from webcrawl.naver_stock import StockModel
from webcrawl.naver_movie import NaverMovie
from webcrawl.naver_login import NaverLogin
from webcrawl.krx import KrxCrawler

class Controller:
    def __init__(self):
        pass

    def exec(self, flag):
        if flag == 'a':
            a = AssemblyCrawler('http://likms.assembly.go.kr/bill/billDetail.do?billId=PRC_R1N9J0N1X0Y9A1O8S3R5Z3J3K9O8N7')
            a.scrap()
        elif flag == 'b':
            b = BugsCrawler('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20190810&charthour=11')
            b.scrap()
        elif flag == 'n':
            n = NaverCrawler('https://finance.naver.com/sise/')
            n.scrap()
        elif flag == 'ns':
            ns = StockModel('005930')
            ns.scrap()
        elif flag == 'nm':
            ns = NaverMovie('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
            ns.scrap()
        elif flag == 'nl':
            nl = NaverLogin('https: // nid.naver.com / nidlogin.login')
            nl.auto_login()
        elif flag == 'k':
            k = KrxCrawler('http://kind.krx.co.kr/disclosureSimpleSearch.do?method=disclosureSimpleSearchMain')
            k.scrap()
