from webcrawl.controller import Controller

if __name__ == '__main__':
    print('a. 국회 크롤링')
    print('b. 벅스 크롤링')
    print('n. 네이버 크롤링')
    print('ns. 네이버 주가 크롤링')
    print('nm. 네이버 영화 크롤링')
    print('nl. 네이버 자동 로그인')
    print('k. 기업공시 크롤링')
    print('0. 종료 ')


    while 1:
        flag = input('크롤링 사이트: ')

        ctl = Controller()
        ctl.exec(flag)

        if flag == '0': break

