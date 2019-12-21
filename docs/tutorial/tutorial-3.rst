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

You can now use briefcase to build your application. Since this is the first
time we're packaging our application, we need to create some confguration files
and other scaffolding to support the packaging process. From the ``helloworld``
directory, run:

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
      [helloworld] Application created.

  .. group-tab:: Linux

    .. note::

      Packaging binaries for Linux is complicated, because of the inconsistent
      library versions present on each distribution. Briefcase uses the
      `AppImage <https://appimage.org/>`__ format by default, which resolves
      many of these problems. An AppImage can be executed on *any* Linux
      distribution with a version of libc greater than or equal the version of
      the distribution where the AppImage was created.

      To simplify the packaging process, Briefcase provides a pre-compiled
      Python support library. This support library was compiled on Ubuntu 16.04,
      which means the AppImages build by Briefcase can be used on *any* Linux
      distribution of about the same age or newer - but those AppImages *must*
      be compiled on Ubuntu 16.04.

      This means you have four options:

      1. Install Ubuntu 16.04 on your own machine.

      2. Find a cloud or CI provider that can provide you an Ubuntu 16.04
         machine for build purposes. Github Actions, for example, provides
         Ubuntu 16.04 as a build option.

      3. Run Briefcase inside a Docker container. Once you have `installed
         Docker <https://docs.docker.com/install/>`__, the command::

            $ docker run -it -v /path/to/project:/project ubuntu:16.04 /bin/bash

         will start a Docker container running Ubuntu 16.04, mounting your
         local project directory (``/path/to/project``) as the ``/project``
         directory in the container. You can then install the requirements
         necessary to run Briefcase inside the container::

             $ apt-get update
             $ apt-get install python3-dev python3-venv libgirepository1.0-dev libcairo2-dev libpango1.0-dev libwebkitgtk-3.0-0 gir1.2-webkit-3.0
             $ pip install beeware

         There is no need to use a virtual environment inside the Docker
         container, as Docker provides the isolation layer that virtual
         environments provide in a local environment.

         As an aside, this approach will also allow you to create Linux
         packages while on Windows or macOS.

      4. Build your own version of the BeeWare `Python support libraries
         <https://github.com/beeware/Python-Linux-support>`__. If you take this
         approach, be aware that your AppImage will only be as portable as the
         version of libc that is available on the distribution you use. If you
         build using Ubuntu 19.10, for example, you can expect that only people
         on the most recent versions of Fedora or Arch will be able to run your
         AppImage.

    .. code-block:: bash

      (beeware-venv) $ briefcase create

      [helloworld] Generating application template...
      Using app template: https://github.com/beeware/briefcase-linux-appImage-template.git
      ...
      [helloworld] Installing support package...
      ...
      [helloworld] Installing dependencies...
      ...
      [helloworld] Installing application code...
      ...
      [helloworld] Installing application resources...
      ...
      [helloworld] Application created.

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
      [helloworld] Application created.

Once this completes, if you look in the project directory, you should now see a
directory corresponding to your platform (``macOS``, ``linux``, or ``windows``)
that contains additional files. This is the platform-specific packaging
configuration for your application.

You can then compile an installer, using the `build` command:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      (beeware-venv) $ briefcase build

      [helloworld] Building DMG...
      ...
      [helloworld] Created Hello World-0.0.1.dmg.

    Once this step completes, the ``macOS`` folder will contain an ``Hello
    World.app``. This file is a self contained macOS executable. If you open
    the Finder, you can double click on the icon to start the application. If
    you send ``Hello World.app`` to a friend, they will be able to do the same
    - double click on the app, and see your app running.

    The ``macOS`` folder will contain a file named ``Hello World-0.0.1.dmg``.
    If you locate this file in the Finder, and double click on it's icon,
    you'll mount the DMG, giving you a copy of the Hello World app, and a
    link to your Applications folder for easy installation. Drag the app file
    into Application, and you've installed your application. Send the DMG file
    to a friend, and they should be able to do the same.

  .. group-tab:: Linux

    .. code-block:: bash

      (beeware-venv) $ briefcase build

      [helloworld] Building AppImage...
      ...
      [helloworld] Created Hello World-x86_64-0.0.1.AppImage.

    Once this step completes, the ``linux`` folder will contain a file named
    ``Hello World-x86_64-0.0.1.AppImage``. This AppImage is an executable;
    you can run it from the shell, or double click on it in your file explorer.
    You can also give it to any other Linux user, and as long as they've got
    a recent version of Linux, they should be able to run it in the same way.

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>briefcase build

      [helloworld] Building MSI...
      ...
      [helloworld] Created Hello_World-0.0.1.msi.

    Once this step completes, the ``windows`` folder will contain a file named
    ``Hello_World-0.0.1.msi``. If you double click on this installer, you
    should go through a familiar Windows installation process. Once this
    installation completes, there will be a "Hello World" entry in your start
    menu.

Next steps
==========

We now have our application packaged for distribution on desktop platforms. But
what about mobile? In :doc:`Tutorial 4 <tutorial-4/index>`, we'll convert
out application into a mobile application, and deploy it onto a device
simulator, and onto a phone.
