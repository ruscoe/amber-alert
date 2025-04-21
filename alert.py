#! /usr/bin/env python

"""Displays Amber Alerts in the terminal."""

import argparse

RSS_URL_BASE = "https://www.missingkids.org/missingkids/servlet/XmlServlet?act=rss&LanguageCountry=en_US&orgPrefix=NCMC&state="

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--state", type=str, required=True, help="the state to display Amber Alerts for")

args = parser.parse_args()

state = args.state.upper()

rss_url = RSS_URL_BASE + state

print(f"Fetching Amber Alerts for {state}")
