'''
heroku-kludge.py is an attempt to resolve an issue which I found
when using Heroku and which is alluded to here : 
https://discussion.heroku.com/t/heroku-refuses-to-create-django-staticfiles-dir/430/4

One the one hand if I allow git to 'see' the 'assets' directory then
it will all go into the repos which I don't want. On the other hand
if I don't then 'collectstatic' complains about 'assest' not existing.

My current solution is this script which is run before 'collectstatic'
on Heroku and which creates 'assets' if it doesn't already exist.

There are some other solutions in the link shown above none of which are very 
attractive but this seems better, for me, to those.
'''
import os
from datetime import datetime
def getiso():
    d=datetime.now()
    return d.strftime('%Y%m%dT%H%M%S')  

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

iso_now = getiso()
STARTFILE = "./HK-START-%s" % iso_now
CREATEFILEPRE = "./HK-CREATE-PRE-%s" % iso_now
CREATEFILEPOST = "./HK-CREATE-POST-%s" % iso_now
ENDFILE = "./HK-END-%s" % iso_now
ASSETS_DIR = "./splsplsh_project/assets"

touch(STARTFILE)
if os.path.exists(ASSETS_DIR):
    pass
else:
    touch(CREATEFILEPRE)
    os.makedirs(ASSETS_DIR)
    touch(CREATEFILEPOST)
touch(ENDFILE)
