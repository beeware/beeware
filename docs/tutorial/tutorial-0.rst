==============================
Tutorial 0 - Let's get set up!
==============================

Before we build our first BeeWare app, we have to make sure we've got
all the prerequisites for running BeeWare.

.. _install-python:

Install Python
==============

The first thing we'll need is a working Python interpreter.

.. tabs::

  .. group-tab:: macOS

    If you're on macOS, a recent version of Python is included with Xcode or
    the command line developer tools. To check if you already have it, run the
    following command:

    .. code-block:: console

      $ python3 --version

    If Python is installed, you'll see its version number. Otherwise, you'll be
    prompted to install the command line developer tools.

    You should ensure that you are using Python 3.9 or newer. If it isn't,
    you'll need to upgrade your Python install. You can get the official
    installer from `the Python website <https://www.python.org/downloads>`_. You
    can use any stable version of Python from 3.9 onward. We'd advise avoiding
    alphas, betas, and release candidates unless you *really* know what you're
    doing.

  .. group-tab:: Linux

    If you're on Linux, you'll install Python using the system package manager
    (``apt`` on Debian/Ubuntu/Mint, ``dnf`` on Fedora, or ``pacman`` on Arch).

    You should ensure that the system Python is Python 3.9 or newer; if it isn't
    (e.g., Ubuntu 20.04 ships with Python 3.8), you'll need to upgrade your
    Linux distribution to something more recent.

    Support for Raspberry Pi is limited at this time.

  .. group-tab:: Windows

    If you're on Windows, you can get the official installer from `the Python
    website <https://www.python.org/downloads>`_. You can use any stable version
    of Python from 3.9 to 3.12 - `Python 3.13 is not currently supported
    <https://github.com/beeware/toga/issues/2889>`__. We'd also advise avoiding
    alphas, betas, and release candidates unless you *really* know what you're
    doing.

.. admonition:: Alternative Python distributions

    There are lots of different ways of installing Python. You can install
    Python through `homebrew
    <https://docs.brew.sh/Homebrew-and-Python>`__. You can use `pyenv
    <https://github.com/pyenv/pyenv#simple-python-version-management-pyenv>`__
    to manage multiple Python installs on the same machine. Windows users
    can install Python from the Windows App Store. Users from a data science
    background might want to use `Anaconda
    <https://docs.anaconda.com/anaconda/install/>`__ or `Miniconda
    <https://docs.conda.io/en/latest/miniconda.html>`__.

    If you're on macOS or Windows, it doesn't matter *how* you've installed
    Python - it only matters that you can run ``python3`` from your operating
    system's command prompt/terminal application, and get a working Python
    interpreter.

    If you're on Linux, you *must* use the system Python provided by your
    operating system. You will be able to complete *most* of this tutorial using
    a non-system Python, but you won't be able to package your application for
    distribution to others.

.. _install-dependencies:

Install dependencies
====================

Next, install the additional dependencies needed for your operating system:

.. tabs::

  .. group-tab:: macOS

    Building BeeWare apps on macOS requires:

    * **Git**, a version control system. This is included with Xcode or the
      command line developer tools, which you installed above. You may need
      to open Xcode for the first time in order for Git to work in your
      terminal session. If it still doesn't register that Git is installed,
      you may need to restart your terminal session.

  .. group-tab:: Linux

    To support local development, you'll need to install some system packages.
    The list of packages required varies depending on your distribution:

    **Ubuntu / Debian**

    ..
      The package list should be the same as in ci.yml and unix-prerequisites.rst in the
      Toga repository.

    .. warning::

      Using a Debian-based Linux distribution (including Ubuntu) will require
      some addition modifications later in the tutorial. Keep an eye out for the
      additional steps - if you don't follow them, you'll see errors referencing
      PyGObject or ``girepository-2.0``.

    .. code-block:: console

      $ sudo apt update
      $ sudo apt install git build-essential pkg-config python3-dev python3-venv libgirepository1.0-dev libcairo2-dev gir1.2-gtk-3.0 libcanberra-gtk3-module

    **Fedora**

    .. code-block:: console

      $ sudo dnf install git gcc make pkg-config rpm-build python3-devel gobject-introspection-devel cairo-gobject-devel gtk3 libcanberra-gtk3

    **Arch / Manjaro**

    .. code-block:: console

      $ sudo pacman -Syu git base-devel pkgconf python3 gobject-introspection cairo gtk3 libcanberra

    **OpenSUSE Tumbleweed**

    .. code-block:: console

      $ sudo zypper install git patterns-devel-base-devel_basis pkgconf-pkg-config python3-devel gobject-introspection-devel cairo-devel gtk3 'typelib(Gtk)=3.0' libcanberra-gtk3-module


  .. group-tab:: Windows

    Building BeeWare apps on Windows requires:

    * **Git**, a version control system. You can download Git from from
      `git-scm.com <https://git-scm.com/downloads/>`__.

    After installing these tools, you should ensure you restart any terminal
    sessions. Windows will only expose newly installed tools terminals started
    *after* the install has completed.

Set up a virtual environment
============================

We're now going to create a virtual environment - a "sandbox" that we can use
to isolate our work on this tutorial from our main Python installation. If we
install packages into the virtual environment, our main Python installation
(and any other Python projects on our computer) won't be affected. If we make
a complete mess of our virtual environment, we'll be able to simply delete it
and start again, without affecting any other Python project on our computer,
and without the need to re-install Python.

.. tabs::

  .. group-tab:: macOS

    .. code-block:: console

      $ mkdir beeware-tutorial
      $ cd beeware-tutorial
      $ python3 -m venv beeware-venv
      $ source beeware-venv/bin/activate

  .. group-tab:: Linux

    .. code-block:: console

      $ mkdir beeware-tutorial
      $ cd beeware-tutorial
      $ python3 -m venv beeware-venv
      $ source beeware-venv/bin/activate

  .. group-tab:: Windows

    .. code-block:: doscon

       C:\...>md beeware-tutorial
       C:\...>cd beeware-tutorial
       C:\...>py -3.12 -m venv beeware-venv
       C:\...>beeware-venv\Scripts\activate

    If you're not using Python 3.12, replace the ``-3.12`` in these instructions with
    the version number that you are using.

    .. admonition:: Errors running PowerShell Scripts

      If you're using PowerShell, and you receive the error::

          File C:\...\beeware-tutorial\beeware-venv\Scripts\activate.ps1 cannot be loaded because running scripts is disabled on this system.

      Your Windows account doesn't have permissions to run scripts. To fix this:

      1. Run `Windows PowerShell as Administrator <https://learn.microsoft.com/en-us/powershell/scripting/windows-powershell/starting-windows-powershell?view=powershell-7.4>`_.
      2. Run ``set-executionpolicy RemoteSigned``
      3. Select ``Y`` to change the execution policy.

      Once you've done this you can rerun
      ``beeware-venv\Scripts\activate.ps1`` in your original PowerShell
      session (or a new session in the same directory).

If this worked, your prompt should now be changed - it should have a
``(beeware-venv)`` prefix. This lets you know that you're currently in your
BeeWare virtual environment. Whenever you're working on this tutorial, you
should make sure your virtual environment is activated. If it isn't, re-run the
last command (the ``activate`` command) to re-activate your environment.

.. admonition:: Alternative virtual environments

    If you're using Anaconda or miniconda, you may be more familiar with using
    conda environments. You might also have heard of ``virtualenv``, a
    predecessor to Python's built in ``venv`` module. As with Python installs -
    if you're on macOS or Windows, it doesn't matter *how* you create your
    virtual environment, as long as you have one. If you're on Linux, you should
    stick to ``venv`` and the system Python.

Next steps
==========

We've now set up our environment. We're ready to :doc:`create our first BeeWare
application <tutorial-1>`.
