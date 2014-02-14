from paver.easy import *
from paver.setuputils import setup

import paver.doctools

setup(
    name="spellsplash",
    packages=['spellweb'],
    version="0.1",
    url="http://mainlydata.kubadev.com/",
    author="Richard Shea",
    author_email="rshea@thecubagroup.com",
    install_requires= ['nose']
)
options(
    sphinx=Bunch(
        builddir="./docs/_build",
        sourcedir="./docs/modules"
    ),
    sphinxAutodocInit=Bunch(
        suffix="rst",
        destdir="docs.modules",
        modulepath="spellweb",
        sourceFileBuildScript="generate_modules.py"
    ),
    minilib=Bunch(
        extra_files=['doctools','.\generate_modules']
    ), 
    
) 

@task
def nosetests():
    """Runs the tests and stops the build if tests fail"""

    import nose

    '''
    I'm not sure exactly how this works but if we don't supply some sort
    of argv value nose ends up reading the argv which invoked paver
    and that in turn means nose gets very confused. I've added the 
    --verbose directive as it seems the least invasive but I think anything
    would do
    '''
    
    testResults = nose.run(module=None, argv=['--verbose'])
    if testResults:
        pass
    else:
        raise BuildFailure

@task
@needs('paver.doctools.html')
def html(options):
    """Build the docs and put them into our package."""
    pass


@task
def sphinxAutodocInit(options):
    """Regenerate the sphinx module level source files"""
    sh("python %s --force --suffix=%s --dest-dir=%s %s" % (options.sourceFileBuildScript, options.suffix, options.destdir, options.modulepath))


@task
@needs(['nosetests','sphinxAutodocInit','html', 'distutils.command.sdist'])
def sdist():
    """Generate docs and source distribution."""
    pass

    




