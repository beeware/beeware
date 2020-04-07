======================================
Tutorial 4 - Updating your application
======================================

In the last tutorial, we packaged our application as a native application. If
you're dealing with a real-world app, that isn't going to be the end of the
story - you'll likely do some testing, discover problems, and need to make some
changes. Even if your application is perfect, you'll eventually want to publish
version 2 of your application with improvements.

So - how do you update your installed app when you make code changes?

Updating application code
=========================

Our application current prints to the console when you press the button.
However, GUI applications shouldn't really use the console for output. They
need to use dialogs to communicate with users.

Let's add a dialog box to say hello, instead of writing to the console.
Modify the `say_hello` callback so it looks like this::

    def say_hello(self, widget):
        self.main_window.info_dialog(
            'Hi there!',
            "Hello, {}".format(self.name_input.value)
        )

This directs Toga to open a modal dialog box when the button is pressed.

If you run ``briefcase dev`` and press the button, you'll see the new dialog
box. However, if you run ``briefcase run``, the dialog box won't appear.

Why is this? Well, ``briefcase dev`` operates by running your code in place -
it tries to produce as realistic runtime environment for your code as possible,
but it doesn't provide or use any of the platform infrastructure for wrapping
your code as an application. Part of the process of packaging your app involves
copying your code *into* the application bundle - and at the moment, your
application still has the old code in it.

So - we need to tell briefcase to copy over the new version of the code. We
*could* do this by deleting the old platform directory and starting from
scratch. However, Briefcase provides an easier way - you can update the code
for your existing bundled application:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      (beeware-venv) $ briefcase update

      [helloworld] Updating application code...
      Installing src/helloworld...

      [helloworld] Application updated.

  .. group-tab:: Linux

    .. code-block:: bash

      (beeware-venv) $ briefcase update

      [helloworld] Updating application code...
      Installing src/helloworld...

      [helloworld] Application updated.

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>briefcase update

      [helloworld] Updating application code...
      Installing src/helloworld...

      [helloworld] Application updated.

If Briefcase can't find the scaffolded template, it will automatically invoke
`create` to generate a fresh scaffold.

Now that we've updated the installer code, We can then run ``briefcase build``
to re-compiled app, ``briefcase run`` to run the updated app, and ``briefcase
package`` to repackage the application for distribution.

Updating dependencies and icons
===============================

This only updates the application code, though - what if your dependencies have
changed, or you have new application resources, like a new splash screen or
application icon)? In this situation, the ``update`` command has some options
you can use:

* ``briefcase update -d`` (or ``briefcase update --update_dependencies``)
  will re-install your the application dependecies.

* ``briefcase update -r`` (or ``briefcase update --update_resources``)
  will re-install your application resources.

Update and run in one step
==========================

If you're rapidly iterating code changes, you'll likely want to make a code
change, update the application, and immediately re-run your application.
Briefcase has a shortcut to support this usage pattern - the ``-u`` (or
``--update``) option on the ``run`` command.

Let's try making another change. You may have noticed that if you don't type
a name in the text input box, the dialog will say "Hello, ". Let's modify the
``say_hello`` function again to handle this edge case::

        def say_hello(self, widget):
            if self.name_input.value:
                name = self.name_input.value
            else:
                name = 'stranger'

            self.main_window.info_dialog(
                'Hi there!',
                "Hello, {}".format(name)
            )

Run your app in development mode (with ``briefcase dev``) to confirm that the
new logic works; then update, build and run the app with one command:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      (beeware-venv) $ briefcase run -u

      [helloworld] Updating application code...
      Installing src/helloworld...

      [helloworld] Application updated.

      [helloworld] Starting app...

  .. group-tab:: Linux

    .. code-block:: bash

      (beeware-venv) $ briefcase run -u

      [helloworld] Updating application code...
      Installing src/helloworld...

      [helloworld] Application updated.

      [helloworld] Building AppImage...
      ...
      [helloworld] Created linux/Hello World-x86_64-0.0.1.AppImage.

      [helloworld] Starting app...

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>briefcase update

      [helloworld] Updating application code...
      Installing src/helloworld...

      [helloworld] Application updated.

      [helloworld] Starting app...

This should only be required if you're testing something about how your
application runs as a native binary, or hunting a bug that only manifests when
your application is in packaged form. For most day-to-day development,
``briefcase dev`` will be a lot faster.

The package command also accepts the ``-u`` argument, so if you make a change
to your application code and want to repackage immediately, you can run
``briefcase package -u``.

Next steps
==========

We now have our application packaged for distribution on desktop platforms,
and we've been able to update the code in our application.

But what about mobile? In :doc:`Tutorial 5 <tutorial-5/index>`, we'll convert
out application into a mobile application, and deploy it onto a device
simulator, and onto a phone.
