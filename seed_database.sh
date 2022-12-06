#!/bin/bash

rm db.sqlite3
rm -rf ./chaseapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations chaseapi
python3 manage.py migrate chaseapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata teams
python3 manage.py loaddata jersey_posts
python3 manage.py loaddata comments
python3 manage.py loaddata likes