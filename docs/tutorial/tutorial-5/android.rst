======================================
Tutorial 5 - Taking it mobile: Android
======================================

The process of deploying an application to Android is very similar to the
process for deploying as a desktop application. There is one additional
pre-requisite: Java 8.

Setting up Java 8
=================

To use BeeWare's Android tooling, you must install a Java 8 compiler and provide
the path to it in the ``JAVA_HOME`` environment variable. This is because
BeeWare's Android tooling depends on the Android SDK, and the Android SDK
depends on the Java runtime and compiler being available. Some tools within
the Android SDK specifically require version 8 of Java, so we stick to that
in this documentation.

Download & install Java 8
-------------------------

Visit the `AdoptOpenJDK website <https://adoptopenjdk.net/>`_ and
download OpenJDK 8.

On macOS, the default format is a *.pkg* installer. Download and execute the
installer, accepting the defaults. In your terminal, run:
``export JAVA_HOME="$(/usr/libexec/java_home -v 1.8)"``

On Windows, the default is the *.msi* installer. Download and execute the
installer. During the install process, look for an option labeled
**Set JAVA_HOME variable**. Ensure it is enabled; if a red letter *X* precedes it,
click the red letter *X* and choose **Will be installed on local hard drive**.

On Linux, the default is a _.tar.gz_ file. Download it and unpack it to a
directory of your choosing. Set the *JAVA_HOME* environment variable to the
directory containing *bin*; for example, if you unpacked the *.tar.gz* file
into ``~/java/1.8/``, at the time of writing, you would need to run
``export JAVA_HOME=$HOME/java/1.8/jdk8u242-b08``.

Testing your Java 8 environment
-------------------------------

To make sure that the Java compiler is available via the *JAVA_HOME*
environment variable, and that it is version 8, run the following command.

We test *javac* here, not *java*, because if *javac* works, so will *java*.

If you get a "Command not found" error on macOS or Linux, look for the
``export`` command in the previous section, and run it.

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      $ "$JAVA_HOME/bin/javac" -version
      javac 1.8.0_242

  .. group-tab:: Linux

    .. code-block:: bash

      $ "$JAVA_HOME/javac" -version
      javac 1.8.0_242

  .. group-tab:: Windows

    .. code-block:: doscon

      C:\...>"%JAVA_HOME%\bin\javac" -version
      javac 1.8.0_242

Create an Android app and compile it
====================================

The process of deploying an application to Android is very similar to the
process for deploying as a desktop application. First, you run the ``create``
command. This downloads an Android app template and adds your Python code to it.

.. code-block:: bash

  (beeware-venv) $ briefcase create android

  [helloworld] Generating application template...
  Using app template: https://github.com/beeware/briefcase-android-gradle-template.git
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

Once this completes, we'll now have an ``android`` directory in your project.
This directory will contain a ``Hello World`` folder, which will contain an
Android project configured to use gradle, your application code, and a support
package containing the Python interpreter and the `rubicon-java` library.

In the process, Briefcase downloads the Android SDK. You may be prompted to
accept Google's Android SDK license.

You can then use Briefcase's ``build`` command to compile this into an Android
APK app file. It will take more than two minutes the first time, depending on
your Internet connection speed, and then should take less than 30 seconds every
successive time.

.. code-block:: bash

  (beeware-venv) $ briefcase build android
  [helloworld] Building Android APK...
  Starting a Gradle Daemon
  ...
  BUILD SUCCESSFUL in 1m 1s
  28 actionable tasks: 17 executed, 11 up-to-date
  [helloworld] Built android/Hello World/app/build/outputs/apk/debug/app-debug.apk

Run the app
===========

We're now ready to run our application. You can use Briefcase's ``run`` command
to run the app on an Android device, either physical or virtual. On Android,
the ``run`` command requires that you specify which device to run on.

The easiest way to configure an Android device is to use Briefcase's built-in
recommendations for how to set up an Android device. Run this command:

.. code-block:: bash

  (beeware-venv) $ briefcase run android

  No Android device was specified. Please specify a specific device on which
  to run the app by passing `-d <device_id>`.

  ...

  If you do not see any devices, you can create and start an emulator by running:

  ...


Examine the specific output on your system, and run the commands provided
until you see an Android virtual device on your screen. Once an Android virtual
device is running, you can launch the app with Briefcase by running this command:

.. code-block:: bash

  (beeware-venv) $ briefcase run android -d emulator-5554

At this point, you should see the app launch on your virtual device.

If you have a physical Android device you would prefer to run the app on,
you can find its name and pass it to ``-d <device_id>``.


Next steps
==========

We've now got an application on our phone! Is there anywhere other way to
deploy a BeeWare app? Turn to :doc:`Tutorial 6 <../tutorial-6>` to find
out...
