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
ASSETS_DIR = "./splsplsh_project/assets"
import os
if os.path.exists(ASSETS_DIR):
    pass
else:
    os.makedirs(ASSETS_DIR)
