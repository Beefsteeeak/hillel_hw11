from bs4 import BeautifulSoup

from celery import shared_task

from django.core.mail import send_mail

import requests

from .models import Author, Quote


def get_info(obj):
    quote_desc = obj.find('span', {'class': 'text'}).string
    author_fullname = obj.span.small.string
    url_author_desc = obj.span.a.get('href')
    return quote_desc, author_fullname, url_author_desc


@shared_task
def parse_quote():
    site = 'https://quotes.toscrape.com/'
    r = requests.get(site)
    if r.status_code != requests.codes.ok:
        print(f"{site} status - {r.status_code}")  # noqa:T001
    else:
        print(f"{site} status - {r.status_code}")  # noqa:T001

        counter = 0
        indicator = 0
        soup = BeautifulSoup(r.text, 'html.parser')

        while True:
            for div in soup.find('div', {'class': 'col-md-8'}).find_all('div', {'class': 'quote'}):
                quote_desc, author_fullname, url_author_desc = get_info(div)
                author, created_auth = Author.objects.get_or_create(
                    fullname=author_fullname,
                    description='!!!!'
                )
                quote, created_quote = Quote.objects.get_or_create(
                    description=quote_desc,
                    author=author
                )
                if created_quote:
                    counter += 1
                if counter == 5:
                    break
                if div == soup.find('div', {'class': 'col-md-8'}).find_all('div', {'class': 'quote'})[-1]:
                    if soup.find('div', {'class': 'col-md-8'}).find('nav').find('ul').find('li', {'class': 'next'}):
                        site = site + soup.find('div', {'class': 'col-md-8'}).nav.ul.find('li', {'class': 'next'})\
                            .a.get('href')
                    else:
                        send_mail('quotes', 'No more quotes to parse', 'noreply@test.com', ['admin@mail.com'])
                        indicator = 1
                        break
            if counter == 5 or indicator == 1:
                break
