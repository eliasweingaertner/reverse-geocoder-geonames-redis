# Reverse Geocoder for Geonames and Redis

## What is this?

This is a small reverse geocoder based on GEONAMES datasets. I allows one to carry out reverse geocoding on local host, by invoking a simple Python function. Compared to REST-API based Reverse Geocoders (there are dozens of them with a greast feature set out there!), this small library has simply one advantage: speed. As it keeps the geo names in an in-memory key-value store (Redis), it easily enables you to carry out thousands of reverse geocoding operations per second.

## How do I use it?

First, set up Redis. You'll need Redis 3.2 or newer, as this piece of code makes use of the Redis Geo features. In addition, you'll need to install the Python redis bindings using pip.

Second, for configuring this stuff adapt RedisConfig.py

Third, import a Geonames.org dump file. For your convenience, the repository already holds the cities1000.txt dataset (obtained from http://download.geonames.org/export/dump/ (Creative Commons Lincense)

Finally, see testGeoRadius.py for an example how to use this component
