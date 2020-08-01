# Lab: 19 - Automation

## Authors:

_**Leo Kukharau**_

## Description

This app is looking for emails and phone numbers in the given text file, then generates a list of unique emails and phone numbers and saves those into separate files

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

### Dev dependencies

pytest = "^5.2"  
autopep8 = "^1.5.3"  
pylint = "^2.5.3"

[Link to code](./automation/automation.py)

[Link to PR](https://github.com/LeoKuhorev/automation/pull/2)
