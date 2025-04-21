#! /usr/bin/env python

"""Displays Amber Alerts in the terminal."""

import argparse
import feedparser

RSS_URL_BASE = "https://www.missingkids.org/missingkids/servlet/XmlServlet?act=rss&LanguageCountry=en_US&orgPrefix=NCMC&state="

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--state", type=str, required=True, help="the state to display Amber Alerts for")

args = parser.parse_args()

state = args.state.upper()

rss_url = RSS_URL_BASE + state

print(f"Fetching Amber Alerts for {state}\n")

feed = feedparser.parse(rss_url)

for entry in feed.entries:
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
