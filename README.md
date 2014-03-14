spellsplash       
=========
A tool to generate spelling questions based upon the users previous answers.



More specifically an implementation of Spaced Repetition (http://en.wikipedia.org/wiki/Spaced_repetition) to the area of the learning of spelling of English words.

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

python manage.py runserver 0.0.0.0:8000 --settings=splsplsh_project.settings.local


* * * * 
Using `autoenv` to set a ENV VAR of SECRET_KEY when we cd into spellsplash. Longer term
need a better solution.

Use `printenv` to confirm the SECRET_KEY is set correctly.

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
