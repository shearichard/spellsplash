web: python ./heroku-kludge.py;python manage.py collectstatic --dry-run --noinput --settings=splsplsh_project.settings.heroku; gunicorn splsplsh_project.splsplsh_project.wsgi:application  --log-file - --access-logfile -
