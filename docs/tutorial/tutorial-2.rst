==================================
Tutorial 2 - Making it interesting
==================================

In :doc:`Tutorial 1 <tutorial-1>`, we generated a stub project that was able
to run, but we didn't write any code ourselves. Let's take a look at what was
generated for us.

What was generated
==================

In the ``src/helloworld`` directory, you should see 3 files: ``__init__.py``,
``__main__.py`` and ``app.py``.

``__init__.py`` marks the ``helloworld`` directory as an importable Python
package. It is an empty file; the very fact it exists tells the Python
interpreter that ``helloworld`` is a package.

``__main__.py`` marks the ``helloworld`` package as a special kind of package -
an executable module. If you try to run the ``helloworld`` module, using
``python -m helloworld``, the ``__main__.py`` file is where Python will start
executing. The contents of ``__main__.py`` is relatively simple::

    from helloworld.app import main

    if __name__ == '__main__':
        main().main_loop()

That is - it imports the ``main`` method from the helloworld app; and if it's
being executed as an entry point, calls the main() method, and starts the
application's main loop. The main loop is the way a GUI application listens for
user input (like mouse clicks and keyboard presses).

The more interesting file is ``app.py`` - this contains the logic that creates
our application window::

    import toga
    from toga.style import Pack
    from toga.style.pack import COLUMN, ROW

    class HelloWorld(toga.App):
        def startup(self):
            main_box = toga.Box()

            self.main_window = toga.MainWindow(title=self.name)
            self.main_window.content = main_box
            self.main_window.show()

    def main():
        return HelloWorld('Hello World', 'com.example.helloworld')

Lets go through this line by line::

    import toga
    from toga.style import Pack
    from toga.style.pack import COLUMN, ROW

First, we import the ``toga`` widget toolkit, as well as some style-related
utility classes and constants. Our code doesn't use these yet - but we'll make
use of them shortly.

Then, we define a class::

    class HelloWorld(toga.App):

Each Toga application has a single ``toga.App`` instance, representing the
running entity that is the application. The app may end up managing multiple
windows; but for simple applications, there will be a single main window.

Next, we define a ``startup()`` method::

        def startup(self):
            main_box = toga.Box()

The first thing the startup method does is to define a main box. Toga's layout
scheme behaves similar to HTML. You build an application by constructing a
collection of boxes, each of which contains other boxes, or actual widgets. You
then apply styles to these boxes to define how they will consume the available
window space.

In this application, we define a single box, but we don't put anything into it.

Next, we define a window into which we can put this empty box::

            self.main_window = toga.MainWindow(title=self.name)

This creates an instance of a ``toga.MainWindow``, which will have a title
matching the application's name. A Main Window is a special kind of window in
Toga - it's a window that is closely bound to the lifecycle of the app. When
the Main Window is closed, the application exits. The Main Window is also the
window that has the application's menu (if you're on a platform like Windows
where menu bars are part of the window)

We then add our empty box as the content of the main window, and instruct the
application to show our window::

            self.main_window.content = main_box
            self.main_window.show()

Last of all, we define a ``main()`` method. This is what creates the instance
of our application::

    def main():
        return HelloWorld('Hello World', 'com.example.helloworld')

This ``main()`` method is the one that is imported and invoked by
``__main__.py``. It creates and returns an instance of our ``HelloWorld``
application.

Adding some content of our own
==============================

**TODO**

Now that we've made these changes we can see what they look like by starting
the application again. As before, we'll use Developer mode:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      (beeware-venv) $ briefcase dev

      [helloworld] Starting in dev mode...

  .. group-tab:: Linux

    .. code-block:: bash

      (beeware-venv) $ briefcase dev

      [helloworld] Starting in dev mode...

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>briefcase dev

      [helloworld] Starting in dev mode...

You'll notice that this time, it *doesn't* install dependencies. Briefcase can
detect that the application has been run before, and to save time, will only
run the application. If you add new dependencies to your app, you can make
sure that they're installed by passing in a ``-d`` option when you run
``briefcase dev``.

This should open a GUI window:

.. tabs::

  .. group-tab:: macOS

    .. image:: images/macOS/tutorial-2.png
        :alt: Hello World Tutorial 2 window, on macOS

  .. group-tab:: Linux

    .. image:: images/linux/tutorial-2.png
        :alt: Hello World Tutorial 2 window, on Linux

  .. group-tab:: Windows

    .. image:: images/windows/tutorial-2.png
        :alt: Hello World Tutorial 2 window, on Windows

Next steps
==========

We've now got an application that does something a little more interesting. But
it only runs on our own computer. Let's package this application for
distribution. In :doc:`Tutorial 3 <tutorial-3>`, we'll wrap our application up
as a standalone installer that we could send to a friend, a customer, or upload
to an App Store.
