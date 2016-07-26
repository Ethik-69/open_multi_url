#! /usr/bin/python
# -*- coding:utf-8 -*-
import webbrowser
import requests
import getopt
import bs4
import sys


def open_url(text, number_of_url):
    html_res = bs4.BeautifulSoup(text)
    html_res = html_res.select('.r a')
    for i in range(number_of_url):
        webbrowser.open('http://google.com' + html_res[i].attrs['href'])


def main(keywords, number_of_url):
    res = requests.get('http://google.com/search?q=' + ' '.join(keywords))
    try:
        res.raise_for_status()
        open_url(res.text, number_of_url)
    except Exception as exc:
        print('There was a problem: %s' % (exc))


if __name__ == '__main__':
    keywords = ''
    number_of_url = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hr:n:", ["keywords=", "number="])
    except getopt.GetoptError:
        print sys.argv[0] + ' -r <keywords> -n <number of url to open>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print sys.argv[0] + '-r <keywords> -n <number of url to open>'
            sys.exit()
        elif opt in ("-r", "--keywords"):
            keywords = arg.split()
        elif opt in ("-n", "--number"):
            number_of_url = int(arg)

    main(keywords, number_of_url)
