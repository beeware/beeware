
If you experience problems with BeeWare, `log them on GitHub`_. If you want to
contribute code, please `fork the code`_ and `submit a pull request`_.

.. _log them on GitHub: https://github.com/beeware/beeware/issues
.. _fork the code: https://github.com/beeware/beeware
.. _submit a pull request: https://github.com/beeware/beeware/pulls

.. _setup-dev-environment:

Set up your development environment
===================================

First, ensure that you have Python 3 and pip installed. To do this, run:

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
      (venv) $ pip install -e ".[dev]"

  .. group-tab:: Linux

    .. code-block:: console

      (venv) $ cd beeware
      (venv) $ pip install -e .[dev]

  .. group-tab:: Windows

    .. code-block:: doscon

      (venv) C:\...>cd beeware
      (venv) C:\...>pip install -e .[dev]

Pre-commit automatically runs during the commit
-----------------------------------------------

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


.. _pr-housekeeping:

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

Add change information for release notes
----------------------------------------

Before you submit this change as a pull request, you need to add a *change
note*. BeeWare uses `towncrier <https://pypi.org/project/towncrier/>`__ to automate
building the release notes for each release. Every pull request must include at
least one file in the ``changes/`` directory that provides a short description
of the change implemented by the pull request.

This description should be a high level summary of the change from the
perspective of the user, not a deep technical description or implementation
detail. It is distinct from a commit message - a commit message describes what
has been done so that future developers can follow the reasoning for a change;
the change note is a "user facing" description. For example, if you fix a bug
caused by date handling, the commit message might read:

    Modified date validation to accept US-style MM-DD-YYYY format.

The corresponding change note would read something like:

    Date widgets can now accept US-style MM-DD-YYYY format.

The change note should be in ReST format, in a file that has name of the format
``<id>.<fragment type>.rst``. If the change you are proposing will fix a bug or
implement a feature for which there is an existing issue number, the ID will be
the number of that ticket. If the change has no corresponding issue, the PR
number can be used as the ID. You won't know this PR number until you push the
pull request, so the first CI pass will fail the Towncrier check; add the change
note and push a PR update and CI should then pass.

There are five allowed fragment types:

- ``feature``: The PR adds a new behavior or capability that wasn't previously
  possible (e.g., adding a new widget, or adding a significant capability to an
  existing widget);
- ``bugfix``: The PR fixes a bug in the existing implementation;
- ``doc``: The PR is an significant improvement to documentation;
- ``removal``; The PR represents a backwards incompatible change in the BeeWare
  API; or
- ``misc``; A minor or administrative change (e.g., fixing a typo, a minor
  language clarification, or updating a dependency version) that doesn't need to
  be announced in the release notes.

Some PRs will introduce multiple features and fix multiple bugs, or introduce
multiple backwards incompatible changes. In that case, the PR may have multiple
change note files. If you need to associate two fragment types with the same ID,
you can append a numerical suffix. For example, if PR 789 added a feature
described by ticket 123, closed a bug described by ticket 234, and also made two
backwards incompatible changes, you might have 4 change note files:

* ``123.feature.rst``
* ``234.bugfix.rst``
* ``789.removal.1.rst``
* ``789.removal.2.rst``

For more information about Towncrier and fragment types see `News Fragments
<https://towncrier.readthedocs.io/en/stable/tutorial.html#creating-news-fragments>`__.
