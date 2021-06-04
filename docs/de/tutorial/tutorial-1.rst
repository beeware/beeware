===========================
Tutorial 1 - Your first app
===========================

We're ready to create our first application.

Install the BeeWare tools
=========================

First, we need to install **Briefcase**. Briefcase is a BeeWare tool that can
be used to package your application for distribution to end users - but it can
also be used to bootstrap a new project. Make sure you're in the
``beeware-tutorial`` directory you created in :doc:`Tutorial 0 <tutorial-0>`,
with the ``beeware-venv`` virtual environment activated, and run:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      (beeware-venv) $ python -m pip install briefcase

  .. group-tab:: Linux

    .. code-block:: bash

      (beeware-venv) $ python -m pip install briefcase

    .. admonition:: Possible errors during installation

        If you see errors during installation, it's almost certainly because
        some of the system requirements haven't been installed. Make sure you
        have :ref:`installed all the platform pre-requisistes
        <install-dependencies>`.

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv)C:\...>python -m pip install briefcase

    .. admonition:: Possible errors during installation

        If you're using a more recent version of Python (3.8+), installing the
        ``beeware`` package may raise an error. This will usually manifest as:

        .. code-block:: doscon

                Traceback (most recent call last):
                  File "<string>", line 1, in <module>
                  File "C:\...\Local\Temp\pip-install-ytuu_37_\pythonnet\setup.py", line 18, in <module>
                    from wheel import bdist_wheel
                ModuleNotFoundError: No module named 'wheel'
                ----------------------------------------
            ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.

        Depending on the specifics of your environment, it might also manifest
        as a report that includes the following:

        .. code-block:: doscon

              Building wheel for pythonnet (setup.py) ... error
              ERROR: Command errored out with exit status 1:
              ...
                File "c:\...\Local\Programs\Python\Python38\lib\subprocess.py", line 364, in check_call
                  raise CalledProcessError(retcode, cmd)
              subprocess.CalledProcessError: Command '['...\\python.exe', 'tools\\geninterop\\geninterop.py', 'src\\runtime\\interop38.cs']' returned non-zero exit status 1.
              ----------------------------------------
              ERROR: Failed building wheel for pythonnet
              Running setup.py clean for pythonnet
            Failed to build pythonnet

        This is caused because the ``beeware`` package has dependencies, and on
        Windows, one of those dependencies is `Python for .NET
        <http://pythonnet.github.io/>`__. Python for .NET isn't a pure Python
        package - it contains C# modules that need to be compiled. The Python
        for .NET team publishes pre-compiled versions of these modules, but
        they sometimes lag behind in support of more recent versions of Python.

        If you get this error, you have three options:

         1. Use an older version of Python. Check the `pythonnet entry on
            PyPI <https://pypi.org/project/pythonnet/>`__ to see the versions
            of Python currently supported by Python for .NET.

         2. Configure your environment to support compiling Python for .NET.
            This is a moderately complex process, and will require you to have
            Visual Studio. See `the Python for .NET wiki
            <https://github.com/pythonnet/pythonnet/wiki/Installation>`__ for
            details.

         3. Install an unofficial compiled wheel. The Python for .NET team
            suggests `this collection of wheels
            <https://www.lfd.uci.edu/~gohlke/pythonlibs/#pythonnet>`__ as a
            possible source. The `.whl` file can be installed with
            ``python -m pip install somefile.whl``; you should then be able to
            re-run ``python -m pip install --pre beeware``.

One of the BeeWare tools is **Briefcase**. Briefcase can be used to package
your application for distribution to end users - but it can also be used to
bootstrap a new project.

Bootstrap a new project
=======================

Let's start our first BeeWare project!  We're going to use the Briefcase
``new`` command to create an application called **Hello World**. Run the
following from your command prompt:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      (beeware-venv) $ briefcase new

  .. group-tab:: Linux

    .. code-block:: bash

      (beeware-venv) $ briefcase new

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>briefcase new

Briefcase will ask us for some details of our new application. For the
purposes of this tutorial, use the following:

* **Formal Name** - Accept the default value: ``Hello World``.

* **App Name** - Accept the default value: ``helloworld``.

* **Bundle** - If you own your own domain, enter that domain in reversed order.
  (For example, if you own the domain "cupcakes.com", enter ``com.cupcakes``
  as the bundle). If you don't own your own domain, accept the default bundle
  (``com.example``).

* **Project Name** - Accept the default value: ``Hello World``.

* **Description** - Accept the default value (or, if you want to be really
  creative, come up with your own description!)

* **Author** - Enter your own name here.

* **Author's email** - Enter your own email address. This will be used in the
  configuration file, in help text, and anywhere that an email is required
  when submitting the app to an app store.

* **URL** - The URL of the landing page for your application. Again, if you own
  your own domain, enter a URL at that domain (including the ``https://``).
  Otherwise, just accept the default URL (``https://example.com/helloworld``).
  This URL doesn't need to actually exist (for now); it will only be used if
  you publish your application to an app store.

* **License** - Accept the default license (BSD). This won't affect
  anything about the operation of the tutorial, though - so if you have
  particularly strong feelings about license choice, feel free to choose
  another license.

* **GUI framework** - Accept the default option, Toga (BeeWare's own GUI
  toolkit).

Briefcase will then generate a project skeleton for you to use. If you've
followed this tutorial so far, and accepted the defaults as described, your
file system should look something like::

    beeware-tutorial/
        beeware-venv/
            ...
        helloworld/
            LICENSE
            README.rst
            pyproject.toml
            src/
                helloworld/
                    resources/
                        helloworld.icns
                        helloworld.ico
                        helloworld.png
                    __init__.py
                    __main__.py
                    app.py

This skeleton is actually a fully functioning application without adding
anything else. The ``src`` folder contains all the code for the application,
and the ``pyproject.toml`` file describes how to package the application for
distribution. If you open ``pyproject.toml`` in an editor, you'll see the
configuration details you just provided to Briefcase.

Now that we have a stub application, we can use Briefcase to run the
application.

Run the app in developer mode
=============================

Move into the ``helloworld`` project directory and tell briefcase to start
the project in Developer (or ``dev``) mode:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      (beeware-venv) $ cd helloworld
      (beeware-venv) $ briefcase dev

      [hello-world] Installing dependencies...
      ...
      [helloworld] Starting in dev mode...

  .. group-tab:: Linux

    .. code-block:: bash

      (beeware-venv) $ cd helloworld
      (beeware-venv) $ briefcase dev

      [hello-world] Installing dependencies...
      ...
      [helloworld] Starting in dev mode...

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>cd helloworld
      (beeware-venv) C:\...>briefcase dev

      [hello-world] Installing dependencies...
      ...
      [helloworld] Starting in dev mode...

This should open a GUI window:

.. tabs::

  .. group-tab:: macOS

    .. image:: images/macOS/tutorial-1.png
       :alt: Hello World Tutorial 1 window, on macOS

  .. group-tab:: Linux

    .. image:: images/linux/tutorial-1.png
       :alt: Hello World Tutorial 1 window, on Linux

  .. group-tab:: Windows

    .. image:: images/windows/tutorial-1.png
       :alt: Hello World Tutorial 1 window, on Windows

Press the close button (or select Quit from the application's menu), and you're
done! Congratulations - you've just written a standalone, native application
in Python!

Next steps
==========

We now have a working application, running in developer mode. Now we can add
some logic of our own to make our application do something a little more
interesting. In :doc:`Tutorial 2 <tutorial-2>`, we'll put a more useful user
interface onto our application.
