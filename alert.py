#! /usr/bin/env python

"""Displays Amber Alerts in the terminal."""

import argparse
import feedparser

RSS_URL_BASE = "https://www.missingkids.org/missingkids/servlet/XmlServlet?act=rss&LanguageCountry=en_US&orgPrefix=NCMC&state="

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--state", type=str, required=False, help="the state to display Amber Alerts for")
parser.add_argument("--limit", "-l", type=int, help="maximum number of Amber Alerts to display")

args = parser.parse_args()
limit = args.limit
rss_url = RSS_URL_BASE

if (args.state):
    state = args.state.upper()
    rss_url += state

    print(f"Fetching Amber Alerts for {state}\n")
else:
    print("Fetching recent Amber Alerts for all states\n")

feed = feedparser.parse(rss_url)

count = 0

for entry in feed.entries:
    if limit is not None and count >= limit:
        break

    name = entry.title
    published = entry.published
    link = entry.link
    description = entry.description

    print(f"Name: {name}")
    print(f"Published: {published}")
    print(f"Link: {link}")
    print(f"Description: {description}")
    print("\n")
    print("-" * 60)
    print("\n")

    count += 1
