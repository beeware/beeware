=============================
Contributing to this tutorial
=============================

This tutorial is written using `Sphinx and reStructuredText
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__.
This guide will help you contribute fixes or new content to this tutorial.

Translations of this tutorial are managed using `Weblate
<https://hosted.weblate.org/engage/beeware/>`__. If you'd like to contribute to
the translation effort, join the ``#translations`` channel on `Discord
<https://beeware.org/bee/chat/>`__ and introduce yourself!

Set up your development environment
===================================

.. Docs are always built on Python 3.12. See also the RTD and tox config.

To build the BeeWare tutorial you **must** have a Python 3.12 interpreter
installed and available on your path (i.e., ``python3`` must start a Python
3.12 interpreter).

.. tabs::

  .. group-tab:: macOS

    .. code-block:: console

      $ python3 --version
      $ pip3 --version

  .. group-tab:: Linux

    .. code-block:: console

      $ python3 --version
      $ pip3 --version

  .. group-tab:: Windows

    .. code-block:: doscon

      C:\...>python3 --version
      C:\...>pip3 --version

Install Enchant
---------------

You'll also need to install the Enchant spell checking library.

.. tabs::

  .. group-tab:: macOS

    Enchant can be installed using `Homebrew <https://brew.sh>`__:

    .. code-block:: console

      (venv) $ brew install enchant

    If you're on an Apple Silicon machine (M-series), you'll also need to manually set the location
    of the Enchant library:

    .. code-block:: console

      (venv) $ export PYENCHANT_LIBRARY_PATH=/opt/homebrew/lib/libenchant-2.2.dylib

  .. group-tab:: Linux

    Enchant can be installed as a system package:

    **Ubuntu / Debian**

    .. code-block:: console

      $ sudo apt update
      $ sudo apt install enchant-2

    **Fedora**

    .. code-block:: console

      $ sudo dnf install enchant

    **Arch / Manjaro**

    .. code-block:: console

      $ sudo pacman -Syu enchant

    **OpenSUSE Tumbleweed**

    .. code-block:: console

      $ sudo zypper install enchant

  .. group-tab:: Windows

    Enchant is installed automatically when you set up your development
    environment.

Create a virtual environment
----------------------------

The recommended way of setting up your development environment for BeeWare
is to install a virtual environment, install the required dependencies and
start coding. To set up a virtual environment, run:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: console

      $ python3 -m venv venv
      $ source venv/bin/activate

  .. group-tab:: Linux

    .. code-block:: console

      $ python3 -m venv venv
      $ source venv/bin/activate

  .. group-tab:: Windows

    .. code-block:: doscon

      C:\...>python3 -m venv venv
      C:\...>venv\Scripts\activate

Your prompt should now have a ``(venv)`` prefix in front of it.

Clone the BeeWare repository
----------------------------

For updates to BeeWare documentation:

Next, go to `the BeeWare page on GitHub <https://github.com/beeware/beeware>`__, fork
the repository into your own account, and then clone a copy of that repository
onto your computer by clicking on "Clone or Download". If you have the GitHub
desktop application installed on your computer, you can select "Open in
Desktop"; otherwise, copy the URL provided, and use it to clone using the
command line:

.. tabs::

  .. group-tab:: macOS

    Fork the BeeWare repository, and then::

      (venv) $ git clone https://github.com/<your username>/beeware.git

    (substituting your GitHub username)

  .. group-tab:: Linux

    Fork the BeeWare repository, and then::

      (venv) $ git clone https://github.com/<your username>/beeware.git

    (substituting your GitHub username)

  .. group-tab:: Windows

    Fork the BeeWare repository, and then:

    .. code-block:: doscon

      (venv) C:\...>git clone https://github.com/<your username>/beeware.git

    (substituting your GitHub username)

Install BeeWare tutorial docs dependencies
------------------------------------------

Now that you have the source code, you can install BeeWare docs requirements into
your development environment. Since we're installing from source, we can't
rely on pip to resolve the dependencies to source packages,
so we have to manually install each package:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: console

      (venv) $ cd beeware
      (venv) $ python -m pip install -e ".[dev]"

  .. group-tab:: Linux

    .. code-block:: console

      (venv) $ cd beeware
      (venv) $ python -m pip install -e .[dev]

  .. group-tab:: Windows

    .. code-block:: doscon

      (venv) C:\...>cd beeware
      (venv) C:\...>python -m pip install -e .[dev]

Install pre-commit
------------------

BeeWare uses a tool called `Pre-Commit <https://pre-commit.com>`__ to identify
simple issues and standardize code formatting. It does this by installing a git
hook that automatically runs a series of code linters prior to finalizing any
git commit. To enable pre-commit, run:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: console

      (venv) $ pre-commit install
      pre-commit installed at .git/hooks/pre-commit

  .. group-tab:: Linux

    .. code-block:: console

      (venv) $ pre-commit install
      pre-commit installed at .git/hooks/pre-commit

  .. group-tab:: Windows

    .. code-block:: doscon

      (venv) C:\...>pre-commit install
      pre-commit installed at .git/hooks/pre-commit

When you commit any change, pre-commit will run automatically. If there are any
issues found with the commit, this will cause your commit to fail. Where possible,
pre-commit will make the changes needed to correct the problems it has found:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: console

      (venv) $ git add some/interesting_file.py
      (venv) $ git commit -m "Minor change"
      black....................................................................Failed
      - hook id: black
      - files were modified by this hook

      reformatted some/interesting_file.py

      All done! ✨ 🍰 ✨
      1 file reformatted.

      flake8...................................................................Passed
      check toml...........................................(no files to check)Skipped
      check yaml...........................................(no files to check)Skipped
      check for case conflicts.................................................Passed
      check docstring is first.................................................Passed
      fix end of files.........................................................Passed
      trim trailing whitespace.................................................Passed
      isort....................................................................Passed
      pyupgrade................................................................Passed
      docformatter.............................................................Passed

  .. group-tab:: Linux

    .. code-block:: console

      (venv) $ git add some/interesting_file.py
      (venv) $ git commit -m "Minor change"
      black....................................................................Failed
      - hook id: black
      - files were modified by this hook

      reformatted some/interesting_file.py

      All done! ✨ 🍰 ✨
      1 file reformatted.

      flake8...................................................................Passed
      check toml...........................................(no files to check)Skipped
      check yaml...........................................(no files to check)Skipped
      check for case conflicts.................................................Passed
      check docstring is first.................................................Passed
      fix end of files.........................................................Passed
      trim trailing whitespace.................................................Passed
      isort....................................................................Passed
      pyupgrade................................................................Passed
      docformatter.............................................................Passed

  .. group-tab:: Windows

    .. code-block:: doscon

      (venv) C:\...>git add some/interesting_file.py
      (venv) C:\...>git commit -m "Minor change"
      black....................................................................Failed
      - hook id: black
      - files were modified by this hook

      reformatted some\interesting_file.py

      All done! ✨ 🍰 ✨
      1 file reformatted.

      flake8...................................................................Passed
      check toml...........................................(no files to check)Skipped
      check yaml...........................................(no files to check)Skipped
      check for case conflicts.................................................Passed
      check docstring is first.................................................Passed
      fix end of files.........................................................Passed
      trim trailing whitespace.................................................Passed
      isort....................................................................Passed
      pyupgrade................................................................Passed
      docformatter.............................................................Passed

You can then re-add any files that were modified as a result of the pre-commit checks,
and re-commit the change.

.. tabs::

  .. group-tab:: macOS

    .. code-block:: console

      (venv) $ git add some/interesting_file.py
      (venv) $ git commit -m "Minor change"
      black....................................................................Passed
      flake8...................................................................Passed
      check toml...........................................(no files to check)Skipped
      check yaml...........................................(no files to check)Skipped
      check for case conflicts.................................................Passed
      check docstring is first.................................................Passed
      fix end of files.........................................................Passed
      trim trailing whitespace.................................................Passed
      isort....................................................................Passed
      pyupgrade................................................................Passed
      docformatter.............................................................Passed
      [bugfix e3e0f73] Minor change
      1 file changed, 4 insertions(+), 2 deletions(-)

  .. group-tab:: Linux

    .. code-block:: console

      (venv) $ git add some/interesting_file.py
      (venv) $ git commit -m "Minor change"
      black....................................................................Passed
      flake8...................................................................Passed
      check toml...........................................(no files to check)Skipped
      check yaml...........................................(no files to check)Skipped
      check for case conflicts.................................................Passed
      check docstring is first.................................................Passed
      fix end of files.........................................................Passed
      trim trailing whitespace.................................................Passed
      isort....................................................................Passed
      pyupgrade................................................................Passed
      docformatter.............................................................Passed
      [bugfix e3e0f73] Minor change
      1 file changed, 4 insertions(+), 2 deletions(-)

  .. group-tab:: Windows

    .. code-block:: doscon

      (venv) C:\...>git add some\interesting_file.py
      (venv) C:\...>git commit -m "Minor change"
      black....................................................................Passed
      flake8...................................................................Passed
      check toml...........................................(no files to check)Skipped
      check yaml...........................................(no files to check)Skipped
      check for case conflicts.................................................Passed
      check docstring is first.................................................Passed
      fix end of files.........................................................Passed
      trim trailing whitespace.................................................Passed
      isort....................................................................Passed
      pyupgrade................................................................Passed
      docformatter.............................................................Passed

Now you are ready to start hacking on BeeWare docs!

Building BeeWare's documentation
================================

Build documentation locally
---------------------------

Once your development environment is set up, run:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: console

      (venv) $ tox -e docs

  .. group-tab:: Linux

    .. code-block:: console

      (venv) $ tox -e docs

  .. group-tab:: Windows

    .. code-block:: doscon

      (venv) C:\...>tox -e docs

The output of the file should be in the ``docs/_build/html`` folder. If there
are any markup problems, they'll raise an error.

Live documentation preview
--------------------------

To support rapid editing of documentation, BeeWare also has a "live preview" mode:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: console

      (venv) $ tox -e docs-live

  .. group-tab:: Linux

    .. code-block:: console

      (venv) $ tox -e docs-live

  .. group-tab:: Windows

    .. code-block:: doscon

      (venv) C:\...>tox -e docs-live

This will build the documentation, start a web server to serve the build documentation,
and watch the file system for any changes to the documentation source. If a change is
detected, the documentation will be rebuilt, and any browser viewing the modified page
will be automatically refreshed.

Live preview mode will only monitor the ``docs`` directory for changes. If you're
updating the inline documentation associated with BeeWare source code, you'll need to use
the ``docs-live-src`` target to build docs:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: console

      (venv) $ tox -e docs-live-src

  .. group-tab:: Linux

    .. code-block:: console

      (venv) $ tox -e docs-live-src

  .. group-tab:: Windows

    .. code-block:: doscon

      (venv) C:\...>tox -e docs-live-src

This behaves the same as ``docs-live``, but will also monitor any changes to the
``core/src`` folder, reflecting any changes to inline documentation. However, the
rebuild process takes much longer, so you may not want to use this target unless
you're actively editing inline documentation.

Documentation linting
---------------------

The build process will identify reStructuredText problems, but BeeWare performs some
additional "lint" checks. To run the lint checks:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: console

      (venv) $ tox -e docs-lint

  .. group-tab:: Linux

    .. code-block:: console

      (venv) $ tox -e docs-lint

  .. group-tab:: Windows

    .. code-block:: doscon

      (venv) C:\...>tox -e docs-lint

This will validate the documentation does not contain:

* dead hyperlinks
* misspelled words

If a valid spelling of a word is identified as misspelled, then add the word to
the list in ``docs/spelling_wordlist``. This will add the word to the
spellchecker's dictionary. When adding to this list, remember:

* We prefer US spelling, with some liberties for programming-specific
  colloquialism (e.g., "apps") and verbing of nouns (e.g., "scrollable")
* Any reference to a product name should use the product's preferred
  capitalization. (e.g., "macOS", "GTK", "pytest", "Pygame", "PyScript").
* If a term is being used "as code", then it should be quoted as a literal
  rather than being added to the dictionary.

Rebuilding all documentation
----------------------------

To force a rebuild for all of the documentation:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: console

      (venv) $ tox -e docs-all

  .. group-tab:: Linux

    .. code-block:: console

      (venv) $ tox -e docs-all

  .. group-tab:: Windows

    .. code-block:: doscon

      (venv) C:\...>tox -e docs-all

The documentation should be fully rebuilt in the ``docs/_build/html`` folder.
If there are any markup problems, they'll raise an error.

What to work on?
================

If you're looking for specific areas to improve, there are `tickets tagged
"documentation"
<https://github.com/beeware/BeeWare/issues?q=is%3Aopen+is%3Aissue+label%3Adocumentation>`__
in BeeWare's issue tracker.

However, you don't need to be constrained by these tickets. If you can identify
an error in the tutorial, or an improvement that can be made, start writing!
Anything that improves the experience of the end user is a welcome change.

Submitting a pull request
=========================

Before you submit a pull request, there's a few bits of housekeeping to do.

Submit from a feature branch, not your ``main`` branch
------------------------------------------------------

Before you start working on your change, make sure you've created a branch.
By default, when you clone your repository fork, you'll be checked out on
your ``main`` branch. This is a direct copy of BeeWare's ``main`` branch.
To contribute to BeeWare itself, not the docs, please review the repo README.

While you *can* submit a pull request from your ``main`` branch, it's preferable
if you *don't* do this. If you submit a pull request that is *almost* right, the
core team member who reviews your pull request may be able to make the necessary
changes, rather than giving feedback asking for a minor change. However, if you
submit your pull request from your ``main`` branch, reviewers are prevented from
making modifications.

Instead, you should make your changes on a *feature branch*. A feature branch
has a simple name to identify the change that you've made.

To create a feature branch, run:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: console

      (venv) $ git checkout -b fix-layout-bug

  .. group-tab:: Linux

    .. code-block:: console

      (venv) $ git checkout -b fix-layout-bug

  .. group-tab:: Windows

    .. code-block:: doscon

      (venv) C:\...>git checkout -b fix-layout-bug

Commit your changes to this branch, then push to GitHub and create a pull request.
