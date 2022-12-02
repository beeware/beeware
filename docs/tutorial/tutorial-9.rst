==========================
Tutorial 9 - Testing times
==========================

Most software development doesn't involve writing new code - it's modifying
existing code. Ensuring that existing code continues to work in the way we
expect is a key part of the software development process. One way to do ensure
the behavior of our app is with a *test suite*.

Running the test suite
======================

It turns out our project already has a test suite! When we originally generated
our project, two top-level directories were generated: ``src`` and ``tests``.
The ``src`` folder contains the code for our app; the ``tests`` folder contains
our test suite. Inside the ``tests`` folder is a file named ``test_app.py`` with
the following content::

    def test_first():
        "An initial test for the app"
        assert 1 + 1 == 2

This is a `Pytest <https://pytest.org>`__ *test case* - a block of code that can
be executed to verify some behavior of your app. In this case, the test is a
placeholder, and doesn't test anything about our app - but it is a test that we
can perform.

We can run this test suite using the ``--test`` option to ``briefcase dev``. As
this is the first time we are running tests, we also need to pass in the ``-r``
option to ensure that the test requirements are also installed:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      (beeware-venv) $ briefcase dev --test -r

      [helloworld] Installing requirements...
      ...
      Installing dev requirements... done

      [helloworld] Running test suite in dev environment...
      ===========================================================================
      ============================= test session starts ==============================
      platform darwin -- Python 3.11.0, pytest-7.2.0, pluggy-1.0.0 -- /Users/brutus/beeware-tutorial/beeware-venv/bin/python3.11
      cachedir: /var/folders/b_/khqk71xd45d049kxc_59ltp80000gn/T/.pytest_cache
      rootdir: /Users/brutus
      plugins: anyio-3.6.2
      collecting ... collected 1 item

      tests/test_app.py::test_first PASSED                                     [100%]

      ============================== 1 passed in 0.01s ===============================

  .. group-tab:: Linux

    .. code-block:: bash

      (beeware-venv) $ briefcase dev --test -r

      [helloworld] Installing requirements...
      ...
      Installing dev requirements... done

      [helloworld] Running test suite in dev environment...
      ===========================================================================
      ============================= test session starts ==============================
      platform linux -- Python 3.11.0
      pytest==7.2.0
      py==1.11.0
      pluggy==1.0.0
      cachedir: /tmp/.pytest_cache
      rootdir: /home/brutus
      plugins: anyio-3.6.2
      collecting ... collected 1 item

      tests/test_app.py::test_first PASSED                                     [100%]

      ============================== 1 passed in 0.01s ===============================

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv)C:\...>briefcase dev --test -r

      [helloworld] Installing requirements...
      ...
      Installing dev requirements... done

      [helloworld] Running test suite in dev environment...
      ===========================================================================
      ============================= test session starts ==============================
      platform win32 -- Python 3.11.0
      pytest==7.2.0
      py==1.11.0
      pluggy==1.0.0
      cachedir: C:\Users\brutus\AppData\Local\Temp\.pytest_cache
      rootdir: C:\Users\brutus
      plugins: anyio-3.6.2
      collecting ... collected 1 item

      tests/test_app.py::test_first PASSED                                     [100%]

      ============================== 1 passed in 0.01s ===============================

Success! We've just executed a single test that verifies Python math works in
the way we'd expect (What a relief!).

Let's replace this placeholder test with a test to verify that our
``generate()`` method behaves the way we'd expect. Replace the contents of
``test_app.py`` with the following::

    from helloworld.app import greeting


    def test_name():
        """If a name is provided, the greeting includes the name"""

        assert greeting("Alice") == "Hello, Alice"


    def test_empty():
        """If a name is not provided, a generic greeting is provided"""

        assert greeting("") == "Hello, stranger"

This defines two new tests, verifying the two behaviors we expect to see: the
output when a name is provided, and the output when the name is empty.

We can now re-run the test suite. This time, we don't need to provided the
``-r`` option, as the test requirements have already been installed; we only
need to use the ``--test`` option:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      (beeware-venv) $ briefcase dev --test

      [helloworld] Running test suite in dev environment...
      ===========================================================================
      ============================= test session starts ==============================
      ...
      collecting ... collected 2 items

      tests/test_app.py::test_name PASSED                                      [ 50%]
      tests/test_app.py::test_empty PASSED                                     [100%]

      ============================== 2 passed in 0.11s ===============================

  .. group-tab:: Linux

    .. code-block:: bash

      (beeware-venv) $ briefcase dev --test

      [helloworld] Running test suite in dev environment...
      ===========================================================================
      ============================= test session starts ==============================
      ...
      collecting ... collected 2 items

      tests/test_app.py::test_name PASSED                                      [ 50%]
      tests/test_app.py::test_empty PASSED                                     [100%]

      ============================== 2 passed in 0.11s ===============================

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv)C:\...>briefcase dev --test

      [helloworld] Running test suite in dev environment...
      ===========================================================================
      ============================= test session starts ==============================
      ...
      collecting ... collected 2 items

      tests/test_app.py::test_name PASSED                                      [ 50%]
      tests/test_app.py::test_empty PASSED                                     [100%]

      ============================== 2 passed in 0.11s ===============================

Excellent! Our ``generate()`` utility method is working as expected.

Test driven development
=======================

Now that we have a test suite, we can use it to drive the development of new
features. Let's modify our app to have a special greeting for one particular
user. We can start by adding a test case for the new behavior that we'd like to
see to the bottom of ``test_app.py``::

    def test_brutus():
        """If the name is Brutus, a special greeting is provided"""

        assert greeting("Brutus") == "BeeWare the IDEs of Python!"

Then, run the test suite with this new test:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      (beeware-venv) $ briefcase dev --test

      [helloworld] Running test suite in dev environment...
      ===========================================================================
      ============================= test session starts ==============================
      ...
      collecting ... collected 3 items

      tests/test_app.py::test_name PASSED                                      [ 33%]
      tests/test_app.py::test_empty PASSED                                     [ 66%]
      tests/test_app.py::test_brutus FAILED                                    [100%]

      =================================== FAILURES ===================================
      _________________________________ test_brutus __________________________________

          def test_brutus():
              """If the name is Brutus, a special greeting is provided"""

      >       assert greeting("Brutus") == "BeeWare the IDEs of Python!"
      E       AssertionError: assert 'Hello, Brutus' == 'BeeWare the IDEs of Python!'
      E         - BeeWare the IDEs of Python!
      E         + Hello, Brutus

      tests/test_app.py:19: AssertionError
      =========================== short test summary info ============================
      FAILED tests/test_app.py::test_brutus - AssertionError: assert 'Hello, Brutus...
      ========================= 1 failed, 2 passed in 0.14s ==========================

  .. group-tab:: Linux

    .. code-block:: bash

      (beeware-venv) $ briefcase dev --test

      [helloworld] Running test suite in dev environment...
      ===========================================================================
      ============================= test session starts ==============================
      ...
      collecting ... collected 3 items

      tests/test_app.py::test_name PASSED                                      [ 33%]
      tests/test_app.py::test_empty PASSED                                     [ 66%]
      tests/test_app.py::test_brutus FAILED                                    [100%]

      =================================== FAILURES ===================================
      _________________________________ test_brutus __________________________________

          def test_brutus():
              """If the name is Brutus, provide a special greeting"""

      >       assert greeting("Brutus") == "BeeWare the IDEs of Python!"
      E       AssertionError: assert 'Hello, Brutus' == 'BeeWare the IDEs of Python!'
      E         - BeeWare the IDEs of Python!
      E         + Hello, Brutus

      tests/test_app.py:19: AssertionError
      =========================== short test summary info ============================
      FAILED tests/test_app.py::test_brutus - AssertionError: assert 'Hello, Brutus...
      ========================= 1 failed, 2 passed in 0.14s ==========================

      ============================== 2 passed in 0.11s ===============================

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv)C:\...>briefcase dev --test

      [helloworld] Running test suite in dev environment...
      ===========================================================================
      ============================= test session starts ==============================
      ...
      collecting ... collected 3 items

      tests/test_app.py::test_name PASSED                                      [ 33%]
      tests/test_app.py::test_empty PASSED                                     [ 66%]
      tests/test_app.py::test_brutus FAILED                                    [100%]

      =================================== FAILURES ===================================
      _________________________________ test_brutus __________________________________

          def test_brutus():
              """If the name is Brutus, provide a special greeting"""

      >       assert greeting("Brutus") == "BeeWare the IDEs of Python!"
      E       AssertionError: assert 'Hello, Brutus' == 'BeeWare the IDEs of Python!'
      E         - BeeWare the IDEs of Python!
      E         + Hello, Brutus

      tests/test_app.py:19: AssertionError
      =========================== short test summary info ============================
      FAILED tests/test_app.py::test_brutus - AssertionError: assert 'Hello, Brutus...
      ========================= 1 failed, 2 passed in 0.14s ==========================

This time, we see a test failure - and the output explains the source of the
failure: the test is expecting the output "BeeWare the IDEs of Python!", but our
implementaion of ``greeting()`` is returning "Hello, Brutus". Let's modify the
implementation of ``greeting()`` in ``src/helloworld/app.py`` to have the new
behavior::

    def greeting(name):
        if name:
            if name == "Brutus":
                return "BeeWare the IDEs of Python!"
            else:
                return f"Hello, {name}"
        else:
            return "Hello, stranger"

If we run the tests again, we'll now see our tests pass:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      (beeware-venv) $ briefcase dev --test

      [helloworld] Running test suite in dev environment...
      ===========================================================================
      ============================= test session starts ==============================
      ...
      collecting ... collected 3 items

      tests/test_app.py::test_name PASSED                                      [ 33%]
      tests/test_app.py::test_empty PASSED                                     [ 66%]
      tests/test_app.py::test_brutus PASSED                                    [100%]

      ============================== 3 passed in 0.15s ===============================

  .. group-tab:: Linux

    .. code-block:: bash

      (beeware-venv) $ briefcase dev --test

      [helloworld] Running test suite in dev environment...
      ===========================================================================
      ============================= test session starts ==============================
      ...
      collecting ... collected 3 items

      tests/test_app.py::test_name PASSED                                      [ 33%]
      tests/test_app.py::test_empty PASSED                                     [ 66%]
      tests/test_app.py::test_brutus PASSED                                    [100%]

      ============================== 3 passed in 0.15s ===============================

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv)C:\...>briefcase dev --test

      [helloworld] Running test suite in dev environment...
      ===========================================================================
      ============================= test session starts ==============================
      ...
      collecting ... collected 3 items

      tests/test_app.py::test_name PASSED                                      [ 33%]
      tests/test_app.py::test_empty PASSED                                     [ 66%]
      tests/test_app.py::test_brutus PASSED                                    [100%]

      ============================== 3 passed in 0.15s ===============================

Runtime tests
=============

So far, we'e been running the tests in development mode. This is especially
useful when you're developing new features, as you can rapidly iterate on adding
tests, and adding code to make those tests pass. However, at some point, you'll
want to verify that your code also runs correctly when inside the bundle app
environment.

The ``--test`` and ``-r`` options can also be passed to the ``run`` command. If
you use ``briefcase run --test -r``, the same test suite will run, but it will
run inside the packaged application bundle rather than you development
environment:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      (beeware-venv) $ briefcase run --test -r

      [helloworld] Updating application code...
      Installing src/helloworld... done
      Installing tests... done

      [helloworld] Updating requirements...
      ...
      [helloworld] Built macOS/app/Hello World/Hello World.app
      [helloworld] Built linux/Hello World-x86_64-0.0.1.AppImage (test mode)

      [helloworld] Starting test suite...
      ===========================================================================
      Configuring isolated Python...
      Pre-initializing Python runtime...
      PythonHome: /Users/brutus/beeware-tutorial/helloworld/macOS/app/Hello World/Hello World.app/Contents/Resources/support/python-stdlib
      PYTHONPATH:
      - /Users/brutus/beeware-tutorial/helloworld/macOS/app/Hello World/Hello World.app/Contents/Resources/support/python311.zip
      - /Users/brutus/beeware-tutorial/helloworld/macOS/app/Hello World/Hello World.app/Contents/Resources/support/python-stdlib
      - /Users/brutus/beeware-tutorial/helloworld/macOS/app/Hello World/Hello World.app/Contents/Resources/support/python-stdlib/lib-dynload
      - /Users/brutus/beeware-tutorial/helloworld/macOS/app/Hello World/Hello World.app/Contents/Resources/app_packages
      - /Users/brutus/beeware-tutorial/helloworld/macOS/app/Hello World/Hello World.app/Contents/Resources/app
      Configure argc/argv...
      Initializing Python runtime...
      Installing Python NSLog handler...
      Running app module: tests.helloworld
      ---------------------------------------------------------------------------
      ============================= test session starts ==============================
      ...
      collecting ... collected 3 items

      tests/test_app.py::test_name PASSED [ 33%]
      tests/test_app.py::test_empty PASSED [ 66%]
      tests/test_app.py::test_brutus PASSED [100%]

      ============================== 3 passed in 0.21s ===============================

      [helloworld] Test suite passed!

  .. group-tab:: Linux

    .. code-block:: bash

      (beeware-venv) $ briefcase run --test -r

      [helloworld] Updating application code...
      Installing src/helloworld... done
      Installing tests... done

      [helloworld] Updating requirements...
      ...
      [helloworld] Built linux/Hello World-x86_64-0.0.1.AppImage (test mode)

      [helloworld] Starting test suite...
      ===========================================================================
      ============================= test session starts ==============================
      ...
      collecting ... collected 3 items

      tests/test_app.py::test_name PASSED [ 33%]
      tests/test_app.py::test_empty PASSED [ 66%]
      tests/test_app.py::test_brutus PASSED [100%]

      ============================== 3 passed in 0.21s ===============================

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv)C:\...>briefcase run --test -r

      [helloworld] Updating application code...
      Installing src/helloworld... done
      Installing tests... done

      [helloworld] Updating requirements...
      ...
      [helloworld] Built windows\app\Hello World\src\Hello World.exe (test mode)

      ===========================================================================
      Log started: 2022-12-02 10:57:34Z
      PreInitializing Python runtime...
      PythonHome: C:\Users\brutus\beeware-tutorial\helloworld\windows\app\Hello World\src
      PYTHONPATH:
      - C:\Users\brutus\beeware-tutorial\helloworld\windows\app\Hello World\src\python311.zip
      - C:\Users\brutus\beeware-tutorial\helloworld\windows\app\Hello World\src
      - C:\Users\brutus\beeware-tutorial\helloworld\windows\app\Hello World\src\app_packages
      - C:\Users\brutus\beeware-tutorial\helloworld\windows\app\Hello World\src\app
      Configure argc/argv...
      Initializing Python runtime...
      Running app module: togatest
      ---------------------------------------------------------------------------
      ============================= test session starts ==============================
      ...
      collecting ... collected 3 items

      tests/test_app.py::test_name PASSED [ 33%]
      tests/test_app.py::test_empty PASSED [ 66%]
      tests/test_app.py::test_brutus PASSED [100%]

      ============================== 3 passed in 0.21s ===============================

As with ``briefcase dev --test``, the ``-r`` option is only needed the first
time you run the test suite to ensure that the test dependencies are present. On
subsequent runs, you can omit this option.

You can also use the ``--test`` option on mobile backends: - so ``briefcase run
iOS --test`` and ``briefcase run android --test`` will both work, running the
test suite on the mobile device you select.

Next steps
==========

This has been a taste for what you can do with the tools provided by the
BeeWare project. What you do from here is up to you!

Some places to go from here:

 * Tutorials demonstrating `features of the Toga widget toolkit
   <https://toga.readthedocs.io/en/latest/tutorial/index.html>`__.
 * Details on the `options available when configuring your Briefcase project
   <https://briefcase.readthedocs.io/en/latest/reference/index.html>`__.


..We've now got a a test suite for our application. But it still looks like a
..tutorial app. Is there anything we can do about that? Turn to :doc:`Tutorial 10
..<tutorial-10>` to find out...
