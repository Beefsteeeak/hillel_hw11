from bs4 import BeautifulSoup

from celery import shared_task

from django.core.mail import send_mail

import requests

from .models import Author, Quote


# get quote, Author's full name, link to Author's description
def get_info(div):
    quote_desc = div.find('span', {'class': 'text'}).string
    author_fullname = div.find_all('span')[1].find('small', {'class': 'author'}).string
    url_author_desc = div.find_all('span')[1].find('a').get('href')
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
            for div in soup.find_all('div', {'class': 'row'})[1].find('div', {'class': 'col-md-8'})\
                    .find_all('div', {'class': 'quote'}):
                quote_desc, author_fullname, url_author_desc = get_info(div)

                # get Author's description from Author page
                site_author = site + url_author_desc
                r = requests.get(site_author)
                if r.status_code != requests.codes.ok:
                    print(f"{site_author} status - {r.status_code}")  # noqa:T001
                    continue
                else:
                    print(f"{site_author} status - {r.status_code}")  # noqa:T001

                    soup_author = BeautifulSoup(r.text, 'html.parser')

                    author_description = soup_author.find('div', {'class': 'author-description'}).string

                # save data in database
                author, created_auth = Author.objects.get_or_create(
                    fullname=author_fullname,
                    description=author_description
                )
                quote, created_quote = Quote.objects.get_or_create(
                    description=quote_desc,
                    author=author
                )
                # if quote is created add to counter
                if created_quote:
                    counter += 1
                # if we got 5 new quotes - exit from for
                if counter == 5:
                    break
                # check if we are on the last quote on the page
                if div == soup.find_all('div', {'class': 'row'})[1].find('div', {'class': 'col-md-8'})\
                        .find_all('div', {'class': 'quote'})[-1]:
                    # check if we have button "next"
                    if soup.find_all('div', {'class': 'row'})[1].find('div', {'class': 'col-md-8'}).find('nav')\
                            .find('ul').find('li', {'class': 'next'}):
                        site_pages = site + soup.find_all('div', {'class': 'row'})[1]\
                            .find('div', {'class': 'col-md-8'}).find('nav').find('ul').find('li', {'class': 'next'})\
                            .a.get('href')
                        r = requests.get(site_pages)
                        if r.status_code != requests.codes.ok:
                            print(f"{site_pages} status - {r.status_code}")  # noqa:T001
                            continue
                        else:
                            print(f"{site_pages} status - {r.status_code}")  # noqa:T001

                            soup = BeautifulSoup(r.text, 'html.parser')
                    # we have no quotes - send email and exit from for
                    else:
                        send_mail('quotes', 'No more quotes to parse', 'noreply@test.com', ['admin@mail.com'])
                        indicator = 1
                        break
            # exit from while
            if counter == 5 or indicator == 1:
                break
