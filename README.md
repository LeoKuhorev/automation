# Lab: 19 - Automation

## Authors:

_**Leo Kukharau**_

## Feature Tasks and Requirements

- Given a document potential-contacts, find and collect all email addresses and phone numbers.
- Phone numbers may be in various formats.
  - (xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.
  - phone numbers with missing area code should presume 206
  - phone numbers should be stored in xxx-yyy-zzzz format.
- Once emails and phone numbers are found they should be stored in two separate documents.
- The information should be sorted in ascending order.
- Duplicate entries are not allowed.

## Dependencies

- python = "^3.8"
- pytest = "^6.0.0"
- pyenchant = "^3.1.1"

### Dev dependencies

- autopep8 = "^1.5.3"

[Link to code](./web_scraper/scraper.py)

[Link to PR](https://github.com/LeoKuhorev/web-scraper/pull/2)
