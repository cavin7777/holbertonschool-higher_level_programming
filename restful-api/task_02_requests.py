#!/usr/bin/python3

import csv
import requests


def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(r.url)
    print(f"Status Code: {r.status_code}")

    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(r.url)
    print(f"Status Code: {r.status_code}")

    if r.status_code == 200:
        posts = r.json()
        posts_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(posts_data)
