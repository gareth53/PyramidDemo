RssRunKeeper README
==================

Getting Started
---------------

- cd <directory containing this file>

- $VENV/bin/python setup.py develop

- $VENV/bin/initialize_RssRunKeeper_db development.ini

- $VENV/bin/pserve development.ini

My RSS Manager

An app that generates RSS feeds for sites and services that don't provide RSS feeds
as a matter of course.
So, essentially, this is a collection of API wrappers which all output RSS data

URL Patterns:

/services
/services/runkeeper.rss
/services/twitter.rss

What models do I need?
Or is it all just config?


