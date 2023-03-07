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

    .. code-block:: console

      (beeware-venv) $ briefcase create

      [helloworld] Generating application template...
      Using app template: https://github.com/beeware/briefcase-macOS-app-template.git, branch v0.3.12
      ...
      [helloworld] Installing support package...
      ...
      [helloworld] Installing application code...
      ...
      [helloworld] Installing requirements...
      ...
      [helloworld] Installing application resources...
      ...
      [helloworld] Removing unneeded app content...
      ...
      [helloworld] Created build/helloworld/macos/app

  .. group-tab:: Linux

    .. code-block:: console

      (beeware-venv) $ briefcase create

      [helloworld] Finalizing application configuration...
      Targeting ubuntu:jammy (Vendor base debian)
      Determining glibc version... done

      Targeting glibc 2.35
      Targeting Python3.10

      [helloworld] Generating application template...
      Using app template: https://github.com/beeware/briefcase-linux-AppImage-template.git, branch v0.3.12
      ...
      [helloworld] Installing support package...
      ...
      [helloworld] Building Docker container image...
      ...
      [helloworld] Installing application code...
      ...
      [helloworld] Installing requirements...
      ...
      [helloworld] Entering Docker context...
      ...
      [helloworld] Leaving Docker context...
      Building wheels for app requirements... done

      [helloworld] Entering Docker context...
      ...
      [helloworld] Leaving Docker context...
      Installing app requirements... done

      [helloworld] Installing application resources...
      ...
      [helloworld] Removing unneeded app content...
      ...
      [helloworld] Created build/helloworld/linux/ubuntu

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>briefcase create

      [helloworld] Generating application template...
      Using app template: https://github.com/beeware/briefcase-windows-app-template.git, branch 0.3.12
      ...
      [helloworld] Installing support package...
      ...
      [helloworld] Installing application code...
      ...
      [helloworld] Installing requirements...
      ...
      [helloworld] Installing application resources...
      ...
      [helloworld] Created build\helloworld\windows\app

You've probably just seen pages of content go past in your terminal... so what
just happened? Briefcase has done the following:

1. It **generated an application template**. There's a lot of files and
   configurations required to build a native installer, above and beyond the
   code of your actual application. This extra scaffolding is almost the same
   for every application on the same platform, except for the name of the
   actual application being constructed - so Briefcase provides an application
   template for each platform it supports. This step rolls out the template,
   substituting the name of your application, bundle ID, and other properties of
   your configuration file as required to support the platform you're building
   on.

   If you're not happy with the template provided by Briefcase, you can
   provide your own. However, you probably don't want to do this until you've
   got a bit more experience using Briefcase's default template.

2. It **downloaded and installed a support package**. The packaging approach
   taken by briefcase is best described as "the simplest thing that could
   possibly work" - it ships a complete, isolated Python interpreter as part of
   every application it builds. This is slightly space inefficient - if you
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

3. It **installed application requirements**. Your application can specify any
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

    .. code-block:: console

      (beeware-venv) $ briefcase build

      [helloworld] Adhoc signing app...
      ...
      Signing build/helloworld/macos/app/Hello World.app
      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.0% • 00:07

      [helloworld] Built build/helloworld/macos/app/Hello World.app

    On macOS, the ``build`` command doesn't need to *compile* anything, but it
    does need to sign the contents of binary so that it can be executed. This
    signature is an "ad-hoc" signature - it will only work on *your* machine; if
    you want to distribute the application to others, you'll need to provide a
    full signature.

  .. group-tab:: Linux

    .. code-block:: console

      (beeware-venv) $ briefcase build

      [helloworld] Finalizing application configuration...
      Targeting ubuntu:jammy (Vendor base debian)
      Determining glibc version... done

      Targeting glibc 2.35
      Targeting Python3.10

      [helloworld] Building application...
      Build bootstrap binary...
      make: Entering directory '/home/brutus/beeware-tutorial/helloworld/build/linux/ubuntu/jammy/bootstrap'
      ...
      make: Leaving directory '/home/brutus/beeware-tutorial/helloworld/build/linux/ubuntu/jammy/bootstrap'
      Building bootstrap binary... done

      Installing license... done

      Installing changelog... done

      Installing man page... done

      Update file permissions...
      ...
      Updating file permissions... done

      Stripping binary... done

      [helloworld] Built build/helloworld/linux/ubuntu/jammy/helloworld-0.0.1/usr/bin/helloworld

    Once this step completes, the ``build`` folder will contain a
    ``helloworld-0.0.1`` folder that contains a mirror of a Linux ``/usr``
    filesystem. This filesystem mirror will contain a ``bin`` folder with a
    ``helloworld`` binary, plus ``lib`` and ``share`` folders needed to support
    the binary.

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>briefcase build
      Setting stup app details... done

      [helloworld] Built build\helloworld\windows\app\src\Toga Test.exe

    On Windows, the ``build`` command doesn't need to *compile* anything, but
    it does need to write some metadata so that the application knows it's name,
    version, and so on.

Running your app
================

You can now use Briefcase to run your application:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: console

      (beeware-venv) $ briefcase run

      [helloworld] Starting app...
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
      Running app module: helloworld
      ---------------------------------------------------------------------------

  .. group-tab:: Linux

    .. code-block:: console

      (beeware-venv) $ briefcase run

      [helloworld] Finalizing application configuration...
      Targeting ubuntu:jammy (Vendor base debian)
      Determining glibc version... done

      Targeting glibc 2.35
      Targeting Python3.10

      [helloworld] Starting app...
      ===========================================================================
      Install path: /home/brutus/beeware-tutorial/helloworld/build/helloworld/linux/ubuntu/jammy/helloworld-0.0.1/usr
      Pre-initializing Python runtime...
      PYTHONPATH:
      - /usr/lib/python3.10
      - /usr/lib/python3.10/lib-dynload
      - /home/brutus/beeware-tutorial/helloworld/build/helloworld/linux/ubuntu/jammy/helloworld-0.0.1/usr/lib/helloworld/app
      - /home/brutus/beeware-tutorial/helloworld/build/helloworld/linux/ubuntu/jammy/helloworld-0.0.1/usr/lib/helloworld/app_packages
      Configure argc/argv...
      Initializing Python runtime...
      Running app module: helloworld
      ---------------------------------------------------------------------------

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>briefcase run

      [helloworld] Starting app...

      ===========================================================================
      Log started: 2022-12-02 10:57:34Z
      PreInitializing Python runtime...
      PythonHome: C:\Users\brutus\beeware-tutorial\helloworld\windows\app\Hello World\src
      PYTHONPATH:
      - C:\Users\brutus\beeware-tutorial\helloworld\windows\app\Hello World\src\python39.zip
      - C:\Users\brutus\beeware-tutorial\helloworld\windows\app\Hello World\src
      - C:\Users\brutus\beeware-tutorial\helloworld\windows\app\Hello World\src\app_packages
      - C:\Users\brutus\beeware-tutorial\helloworld\windows\app\Hello World\src\app
      Configure argc/argv...
      Initializing Python runtime...
      Running app module: helloworld
      ---------------------------------------------------------------------------

This will start to run your native application, using the output of the
``build`` command.

You might notice some small differences in the way your application looks
when it's running. For example, icons and the name displayed by the operating
system may be slightly different to those you saw when running under developer
mode. This is also because you're using the packaged application, not just
running Python code. From the operating system's perspective, you're now
running "an app", not "a Python program", and this is reflected in how the
application appears.

Building your installer
=======================

You can now package your application for distribution, using the ``package``
command. The package command does any compilation that is required to convert
the scaffolded project into a final, distributable product. Depending on the
platform, this may involve compiling an installer, performing code signing,
or doing other pre-distribution tasks.

.. tabs::

  .. group-tab:: macOS

    .. code-block:: console

      (beeware-venv) $ briefcase package --adhoc-sign

      [helloworld] Signing app with adhoc identity...
      ...
      Signing build/helloworld/macos/app/Hello World.app
           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.0% • 00:07

      [helloworld] Building DMG...
      Signing dist/Hello World-0.0.1.dmg

      [helloworld] Packaged dist/Hello World-0.0.1.dmg

    The ``dist`` folder will contain a file named ``Hello World-0.0.1.dmg``.
    If you locate this file in the Finder, and double click on its icon,
    you'll mount the DMG, giving you a copy of the Hello World app, and a
    link to your Applications folder for easy installation. Drag the app file
    into Applications, and you've installed your application. Send the DMG file
    to a friend, and they should be able to do the same.

    In this example, we've used the ``--adhoc-sign`` option - that is, we're
    signing our application with adhoc credentials. We've done this to keep the
    tutorial simple. Setting up code signing identities is a little fiddly, and
    they're only *absolutely* required if you're intending to distribute your
    application to others. If we were publishing a real application, you will
    need to specify real credentials.

    When you're ready to publish a real application, check out the Briefcase
    How-To guide on `Setting up a macOS code signing identity
    <https://briefcase.readthedocs.io/en/latest/how-to/code-signing/macOS.html>`__

  .. group-tab:: Linux

    The output of the package step will be slightly different depending on
    your Linux distribution. If you're on a Debian-derived distribution,
    you'll see:

    .. code-block:: console

      (beeware-venv) $ briefcase package

      [helloworld] Finalizing application configuration...
      Targeting ubuntu:jammy (Vendor base debian)
      Determining glibc version... done

      Targeting glibc 2.35
      Targeting Python3.10

      [helloworld] Building .deb package...
      Write Debian package control file... done

      dpkg-deb: building package 'helloworld' in 'helloworld-0.0.1.deb'.
      Building Debian package... done

      [helloworld] Packaged dist/helloworld_0.0.1-1~ubuntu-jammy_amd64.deb

    The ``dist`` folder will contain the DEB file that was generated.

    If you're on a Redhat-based distribution, you'll see:

    .. code-block:: console

      (beeware-venv) $ briefcase package

      [helloworld] Finalizing application configuration...
      Targeting fedora:36 (Vendor base rhel)
      Determining glibc version... done

      Targeting glibc 2.35
      Targeting Python3.10

      [helloworld] Building .rpm package...
      Generating rpmbuild layout... done

      Write RPM spec file... done

      Building source archive... done

      Executing(%prep): /bin/sh -e /var/tmp/rpm-tmp.Kav9H7
      + umask 022
      ...
      + exit 0
      Building RPM package... done

      [helloworld] Packaged dist/helloworld-0.0.1-1.fc36.x86_64.rpm

    The ``dist`` folder will contain the RPM file that was generated.

    Other Linux distributions aren't currently supported for packaging.

    If you want to build a package for a Linux distribution other than the one 
    you're using, Briefcase can also help - but you'll need to install Docker.

    Official installers for `Docker Engine
    <https://docs.docker.com/engine/install/#server>`__ are available for a
    range of Unix distributions. Follow the instructions for your platform;
    however, ensure you don't install Docker in "rootless" mode.

    Once you've installed Docker, you should be able to start an Linux
    container - for example:

    .. code-block:: console

      $ docker run -it ubuntu:22.04

    will show you a Unix prompt (something like `root@84444e31cff9:/#`) inside
    an Ubuntu 22.04 Docker container. Type Ctrl-D to exit Docker and return to
    your local shell.

    Once you've got Docker installed, you can use Briefcase to build a package
    for any Linux distribution that Briefcase supports by passing in a Docker
    image as an argument. For example, to build a DEB package for Ubuntu 22.04
    (Jammy), regardless of the operating system you're on, you can run:

    .. code-block:: console

      $ briefcase package --target ubuntu:jammy

    This will download the Docker image for your selected operating system,
    create a container that is able to run Briefcase builds, and build
    the app package inside the image. Once it's completed, the ``dist`` folder
    will contain the package for the target Linux distribution.

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>briefcase package

      [helloworld] Building MSI...
      ...
      [helloworld] Packaged dist\Hello_World-0.0.1.msi

    Once this step completes, the ``dist`` folder will contain a file named
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
