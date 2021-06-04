=======================================
Tutorial 3 - Packaging for distribution
=======================================

So far, we've been running our application in "Developer mode". This makes it
easy for us to run our application locally - but what we really want is to be
able to give our application to others.

However, we don't want to have to teach our users how to install Python, create
a virtual environment, clone a git repository, and run Briefcase in developer
mode. We'd rather just give them an installer, and have the application Just
Work.

Briefcase can be used to package your application for distribution in this way.

Creating your application scaffold
==================================

Since this is the first time we're packaging our application, we need to create
some confguration files and other scaffolding to support the packaging process.
From the ``helloworld`` directory, run:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      (beeware-venv) $ briefcase create

      [helloworld] Generating application template...
      Using app template: https://github.com/beeware/briefcase-macOS-app-template.git
      ...
      [helloworld] Installing support package...
      ...
      [helloworld] Installing dependencies...
      ...
      [helloworld] Installing application code...
      ...
      [helloworld] Installing application resources...
      ...
      [helloworld] Created macOS/Hello World

  .. group-tab:: Linux

    .. code-block:: bash

      (beeware-venv) $ briefcase create

      [helloworld] Generating application template...
      Using app template: https://github.com/beeware/briefcase-linux-appImage-template.git
      ...
      [helloworld] Installing support package...
      ...
      [helloworld] Installing dependencies...
      [helloworld] Entering Docker context...

      [helloworld] Building Docker container image...
      ...
      [helloworld] Leaving Docker context.

      [helloworld] Installing application code...
      ...
      [helloworld] Installing application resources...
      ...
      [helloworld] Created linux/Hello World

    .. note::

      The first time you run this, it may take a while, as Briefcase needs to
      prepare an Ubuntu 16.04 Docker image that can be used to build AppImage
      binaries. This involves downloading a lot of system packages. On future
      runs, this Docker image will be re-used.

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>briefcase create

      [helloworld] Generating application template...
      Using app template: https://github.com/beeware/briefcase-windows-msi-template.git
      ...
      [helloworld] Installing support package...
      ...
      [helloworld] Installing dependencies...
      ...
      [helloworld] Installing application code...
      ...
      [helloworld] Installing application resources...
      ...
      [helloworld] Created windows\Hello World

You've probably just seen pages of content go past in your terminal... so what
just happened? Briefcase has done the following:

1. It **generated an application template**. There's a lot of files and
   configurations required to build a native installer, above and beyond the
   code of your actual application. This extra scaffolding is almost the same
   for every application on the same platform, except for the name of the
   actual application being constructed - so Briefcase provides an application
   template for each platform it supports. This step rolls out the template,
   subsituting the name of your application, bundle ID, and other properties of
   your configuration file as required to support the platform you're building
   on.

   If you're not happy with the template provided by Briefcase, you can
   provide your own. However, you probably don't want to do this until you've
   got a bit more experience using Briefcase's default template.

2. It **downloaded and installed a support package**. The packaging approach
   taken by briefcase is best described as "the simplest thing that could
   possibly work" - it ships a complete, isolated Python interpreter as part of
   every application it builds. This is slightly space innefficient - if you
   have 5 applications packaged with Briefcase, you'll have 5 copies of the
   Python interpreter. However, this approach guarantees that every application
   is completely independent, using a specific version of Python that is known
   to work with the application.

   Again, Briefcase provides a default support package for each platform; if
   you want, you can provide your own support package, and have that package
   included as part of the build process. You may want to do this if you have
   particular options in the Python interpreter that you need to have enabled,
   or if you want to strip modules out of the standard library that you don't
   need at runtime.

   Briefcase maintains a local cache of support packages, so once you've
   downloaded a specific support package, that cached copy will be used on
   future builds.

3. It **installed application dependencies**. Your application can specify any
   third-party modules that are required at runtime. These will be installed
   using `pip` into your application's installer.

4. It **Installed your application code**. Your application will have its own
   code and resources (e.g., images that are needed at runtime); these files
   are copied into the installer.

5. It **installed your resources needed by your application.** Lastly, it
   adds any additional resources that are needed by the installer itself.
   This includes things like icons that need to be attached to the final
   application and splash screen images.

Once this completes, if you look in the project directory, you should now see a
directory corresponding to your platform (``macOS``, ``linux``, or ``windows``)
that contains additional files. This is the platform-specific packaging
configuration for your application.

Building your application
=========================

You can now compile your application. This step performs any binary
compilation that is necessary for your application to be executable on your
target platform.

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      (beeware-venv) $ briefcase build

      [helloworld] Built macOS/Hello World/Hello World.app

    On ``macOS``, the ``build`` command doesn't need to do anything. A ``.app``
    folder is a layout convention of ``macOS`` itself; as long as the folder
    has a ``.app`` extension, and adheres to some internal layout rules, and
    provides some metadata in a known location, the folder will appear to the
    operating system as an application.

  .. group-tab:: Linux

    .. code-block:: bash

      (beeware-venv) $ briefcase build

      [helloworld] Building AppImage...
      ...
      [helloworld] Built linux/Hello World-x86_64-0.0.1.AppImage

    Once this step completes, the ``linux`` folder will contain a file named
    ``Hello World-x86_64-0.0.1.AppImage``. This AppImage is an executable;
    you can run it from the shell, or double click on it in your file explorer.
    You can also give it to any other Linux user, and as long as they've got
    a version of Linux published after 2016, they should be able to run it in
    the same way.

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>briefcase build

      [helloworld] Built windows\Hello World

    On Windows, this step does nothing. The distributed "binary" on windows is
    a folder with a known entry point; the installer (when it is eventually
    created) will encode details on how to start the application, and install
    a Start Menu item to invoke the application.

Running your app
================

You can now use Briefcase to run your application:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      (beeware-venv) $ briefcase run

      [helloworld] Starting app...

      (beeware-venv) $

  .. group-tab:: Linux

    .. code-block:: bash

      (beeware-venv) $ briefcase run

      [helloworld] Starting app...

      (beeware-venv) $

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>briefcase run

      [helloworld] Starting app...

      (beeware-venv) C:\...>

This will start to run your native application, using the output of the
`build` command.

You'll notice that the console output we saw earlier won't be visible anymore. 
This is because we are now running a standalone, packaged app that has no 
(visible) console to which it can output. 

You might also notice some small differences in the way your application looks 
when it's running. For example, icons and the name displayed by the operating
system may be slightly different to those you saw when running under developer
mode. This is also because you're using the packaged application, not just
running Python code. From the operating system's perspective, you're now
running "an app", not "a Python program", and this is reflected in how the
application appears. 

Building your installer
=======================

You can now package your application for distribution, using the `package`
command. The package command does any compilation that is required to convert
the scaffolded project into a final, distributable product. Depending on the
platform, this may involve compiling an installer, performing code signing,
or doing other pre-distribution tasks.

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      (beeware-venv) $ briefcase package --no-sign

      [helloworld] Building DMG...
      ...
      [helloworld] Created macOS/Hello World-0.0.1.dmg

    The ``macOS`` folder will contain a file named ``Hello World-0.0.1.dmg``.
    If you locate this file in the Finder, and double click on its icon,
    you'll mount the DMG, giving you a copy of the Hello World app, and a
    link to your Applications folder for easy installation. Drag the app file
    into Application, and you've installed your application. Send the DMG file
    to a friend, and they should be able to do the same.

    In this example, we've used the ``--no-sign`` option - that is, we've
    decided to *not* sign our application. We've done this to keep the tutorial
    simple. Setting up code signing identities is a little fiddly, and they're
    only *absolutely* required if you're intending to distribute your
    application to others. If we were publishing a real application, you would
    leave off the ``--no-sign`` flag.

    When you're ready to publish a real application, check out the Briefcase
    How-To guide on `Setting up a macOS code signing identity
    <https://briefcase.readthedocs.io/en/latest/how-to/code-signing/macOS.html>`__

  .. group-tab:: Linux

    .. code-block:: bash

      (beeware-venv) $ briefcase package

      [helloworld] Building AppImage...
      ...
      [helloworld] Created linux/Hello World-x86_64-0.0.1.AppImage.

    On Linux, this step does nothing. The AppImage created by the build command
    is a complete executable, requiring no additional processing.

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>briefcase package

      [helloworld] Building MSI...
      ...
      [helloworld] Created windows\Hello_World-0.0.1.msi

    Once this step completes, the ``windows`` folder will contain a file named
    ``Hello_World-0.0.1.msi``. If you double click on this installer to run it,
    you should go through a familiar Windows installation process. Once this
    installation completes, there will be a "Hello World" entry in your start
    menu.

Next steps
==========

We now have our application packaged for distribution on desktop platforms.
But what happens when we need to update the code in our application? How do
we get those updates into our packaged application? Turn to
:doc:`Tutorial 4 <./tutorial-4>` to find out...
