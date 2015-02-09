spellsplash       
=========
A tool to generate spelling tests based upon the users previous answers.

More specifically an implementation of Spaced Repetition (http://en.wikipedia.org/wiki/Spaced_repetition) to the area of the learning of spelling of English words.

In particular the "Leitner System" (http://en.wikipedia.org/wiki/Leitner_system) will play a part in word selection.

spellspin
-------
A library which :

* provides questions;
* checks answers;
* and records the results of individual users

spellspit
-------
A web-ui which allows interaction with `spellspin`


* * * * 
IMPORTANT
-------
**To make use of the local setting you must start the server like this :**
```
python manage.py runserver 0.0.0.0:8000 --settings=splsplsh_project.settings.local
```

**To use Gunicorn locally you must be within the Project directory (ie the same directory that contains manage.py) and execute this command**

```
gunicorn splsplsh_project.wsgi:application -b 0.0.0.0:8000  --log-file - --access-logfile -
```

The virtenv used for dev is `spsp`.
* * * * 
Using `autoenv` to set a ENV VAR of SECRET_KEY when we cd into spellsplash. Longer term
need a better solution.

Use `printenv` to confirm the SECRET_KEY is set correctly.

IMPORTANT
-------
I've tried various things to make gunicorn work here are three just as a note:

```
gunicorn wsgi --log-file=-

gunicorn splsplsh_project.wsgi --log-file=-

gunicorn splsplsh_project.splsplsh_project.wsgi --log-file=-
```

Here's one that does work but only if the current directory is ~/dev/spellsplash/splsplsh_project:
```
gunicorn splsplsh_project.wsgi:application -b 0.0.0.0:8000  --log-file -
```



* * * * 
(venv)~/dev/spellsplash $ flake8 ./spellweb
(venv)~/dev/spellsplash $ pep257 ./spellweb

* * * * 
This is just some rough and ready documentation of how to do the build until it's stabilised a little more :

```
(venv)~/dev/spellsplash $ python generate_modules.py --suffix=rst --dest-dir=./docs/modules ./spellsplash
Creating file ./docs/modules/spellsplash.rst.
Creating file ./docs/modules/modules.rst.
(venv)~/dev/spellsplash $ cd docs
(venv)~/dev/spellsplash/docs $ make html
sphinx-build -b html -d _build/doctrees   . _build/html
Running Sphinx v1.2b3
loading pickled environment... done
building [html]: targets for 0 source files that are out of date
updating environment: 2 added, 1 changed, 0 removed
reading sources... [ 33%] index
reading sources... [ 66%] modules/modules
reading sources... [100%] modules/spellsplash

/home/rshea/dev/spellsplash/docs/modules/spellsplash.rst:7: WARNING: toctree contains reference to nonexisting document u'modules/spellsplash.spellspin'
/home/rshea/dev/spellsplash/docs/modules/spellsplash.rst:7: WARNING: toctree contains reference to nonexisting document u'modules/spellsplash.spellweb'
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [ 33%] index
writing output... [ 66%] modules/modules
writing output... [100%] modules/spellsplash

writing additional files... genindex search
copying static files... done
copying extra files... dumping search index... done
dumping object inventory... done
build succeeded, 2 warnings.

Build finished. The HTML pages are in _build/html.

```
* * * * 
This is a a guide to the urls associated with authorisation at at #e7159ec

```
/accounts/activate/<activation_key>/                    registration.backends.default.views.ActivationView      registration_activate
/accounts/activate/complete/                            django.views.generic.base.TemplateView                  registration_activation_complete

/accounts/login/                                        django.contrib.auth.views.login                         auth_login
/accounts/logout/                                       django.contrib.auth.views.logout                        auth_logout

/accounts/password/change/                              django.contrib.auth.views.password_change               auth_password_change
/accounts/password/change/done/                         django.contrib.auth.views.password_change_done          auth_password_change_done

/accounts/password/reset/                               django.contrib.auth.views.password_reset                auth_password_reset
/accounts/password/reset/complete/                      django.contrib.auth.views.password_reset_complete       auth_password_reset_complete
/accounts/password/reset/confirm/<uidb36>-<token>/      django.contrib.auth.views.password_reset_confirm        auth_password_reset_confirm
/accounts/password/reset/done/                          django.contrib.auth.views.password_reset_done           auth_password_reset_done

/accounts/register/                                     registration.backends.default.views.RegistrationView    registration_register
/accounts/register/closed/                              django.views.generic.base.TemplateView                  registration_disallowed
/accounts/register/complete/                            django.views.generic.base.TemplateView                  registration_complete

/admin/logout/                                          django.contrib.admin.sites.logout                       logout
/admin/password_change/                                 django.contrib.admin.sites.password_change              password_change
/admin/password_change/done/                            django.contrib.admin.sites.password_change_done         password_change_done



/accounts/activate/<activation_key>/                    registration.backends.default.views.ActivationView      registration_activate
/accounts/activate/complete/                            django.views.generic.base.TemplateView                  registration_activation_complete

/accounts/login/                                        django.contrib.auth.views.login                         auth_login
/accounts/logout/                                       django.contrib.auth.views.logout                        auth_logout

/accounts/password/change/                              django.contrib.auth.views.password_change               auth_password_change
/accounts/password/change/                              django.contrib.auth.views.password_change               password_change
/accounts/password/change/done/                         django.contrib.auth.views.password_change_done          auth_password_change_done
/accounts/password/change/done/                         django.contrib.auth.views.password_change_done          password_change_done

/accounts/password/reset/                               django.contrib.auth.views.password_reset                auth_password_reset
/accounts/password/reset/                               django.contrib.auth.views.password_reset                password_reset
/accounts/password/reset/complete/                      django.contrib.auth.views.password_reset_complete       auth_password_reset_complete
/accounts/password/reset/complete/                      django.contrib.auth.views.password_reset_complete       password_reset_complete
/accounts/password/reset/confirm/<uidb36>-<token>/      django.contrib.auth.views.password_reset_confirm        auth_password_reset_confirm
/accounts/password/reset/confirm/<uidb64>-<token>/      django.contrib.auth.views.password_reset_confirm        auth_password_reset_confirm
/accounts/password/reset/done/                          django.contrib.auth.views.password_reset_done           auth_password_reset_done
/accounts/password/reset/done/                          django.contrib.auth.views.password_reset_done           password_reset_done

/accounts/register/                                     registration.backends.default.views.RegistrationView    registration_register
/accounts/register/closed/                              django.views.generic.base.TemplateView                  registration_disallowed
/accounts/register/complete/                            django.views.generic.base.TemplateView                  registration_complete

```
1
