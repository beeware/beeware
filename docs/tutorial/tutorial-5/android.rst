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

.. tabs::

  .. group-tab:: macOS

    On macOS, the default format is a *.pkg* installer. Download and execute the
    installer, accepting the defaults. In your terminal, run::

      (beeware-venv) $ export JAVA_HOME="$(/usr/libexec/java_home -v 1.8)"

    You will need to run this every time you start a terminal session, or you
    can add it to your `shell configuration <https://apple.stackexchange.com/a/356455>`_
    or `launchd configuration <http://www.dowdandassociates.com/blog/content/howto-set-an-environment-variable-in-mac-os-x-launchd-plist/>`_.

  .. group-tab:: Linux

    On Linux, the default format is a *.tar.gz* file. Download it and unpack it to a
    directory of your choosing. Set the ``JAVA_HOME`` environment variable to the
    directory containing ``bin/javac``. For example, if you unpacked the *.tar.gz* file
    into ``~/java/1.8/``, at the time of writing, you would need to run::

      (beeware-venv) $ export JAVA_HOME="$HOME/java/1.8/jdk8u242-b08"

    You will need to run this every time you start a terminal session, or you
    can add it to your `PAM environment file <https://help.ubuntu.com/community/EnvironmentVariables#Persistent_environment_variables>`_,
    `shell configuration <https://apple.stackexchange.com/a/356455>`_,
    or `systemd configuration <https://in.waw.pl/~zbyszek/blog/environmentd.html>`_.

  .. group-tab:: Windows

    On Windows, the default is the *.msi* installer. Download and execute the
    installer.

    During the install process, look for an option labeled **Set JAVA_HOME variable**.
    Ensure it is enabled; if a red letter *X* precedes it, click the red letter *X*
    and choose **Will be installed on local hard drive**.

Testing your Java 8 environment
-------------------------------

To make sure that the Java compiler is available via the *JAVA_HOME*
environment variable, and that it is version 8, run the following command.

We test *javac* here, not *java*, because if *javac* works, so will *java*.

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      (beeware-venv) $ "$JAVA_HOME/bin/javac" -version
      javac 1.8.0_242

    If you get a "Command not found" error, look for the ``export`` command in
    the previous section, and run it.

  .. group-tab:: Linux

    .. code-block:: bash

      (beeware-venv) $ "$JAVA_HOME/bin/javac" -version
      javac 1.8.0_242

    If you get a "Command not found" error, look for the ``export`` command in
    the previous section, and run it.

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>"%JAVA_HOME%\bin\javac" -version
      javac 1.8.0_242

    If you get a "Command not found" error, re-run the installer from AdoptOpenJDK
    and be sure to configure the installer to "Set JAVA_HOME variable".

Create an Android app and compile it
====================================

The process of deploying an application to Android is very similar to the
process for deploying as a desktop application. First, you run the ``create``
command. This downloads an Android app template and adds your Python code to it.

.. tabs::

  .. group-tab:: macOS

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

  .. group-tab:: Linux

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

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>briefcase create android

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
Android project with a Gradle build configuration. This project will contain
your application code, and a support package containing the Python interpreter
and the `rubicon-java` library.

In the process, Briefcase downloads the Android SDK. You may be prompted to
accept Google's Android SDK license.

You can then use Briefcase's ``build`` command to compile this into an Android
APK app file. It will take quite a few minutes the first time, depending on
your Internet connection speed, and then should take less than 30 seconds every
successive time.

.. admonition:: Gradle can look stuck

  You may see Gradle stuck on the "CONFIGURING" step for many, many minutes.
  Gradle is likely busy performing downloads, and you should not interrupt it.
  This typically only affects the first time an app is built.

.. code-block:: bash

  (beeware-venv) $ briefcase build android
  [helloworld] Building Android APK...
  Starting a Gradle Daemon
  ...
  BUILD SUCCESSFUL in 1m 1s
  28 actionable tasks: 17 executed, 11 up-to-date
  [helloworld] Built android/Hello World/app/build/outputs/apk/debug/app-debug.apk

Run the app on a virtual device
===============================

We're now ready to run our application. You can use Briefcase's ``run`` command
to run the app on an Android device, either physical or virtual. This section
covers running the app on a virtual Android device.

On Android, Briefcase's ``run`` command requires that you specify which device to run on.
If you use ``run`` without specifying a device, Briefcase will tell you how to
create an appropriate Android virtual device. Run that command on your system.

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      (beeware-venv) $ briefcase run android

      No Android device was specified. Please specify a specific device on which
      to run the app by passing `-d <device_id>`.

      ...

      If you do not see any devices, you can create and start an emulator by running:

      ...

  .. group-tab:: Linux

    .. code-block:: bash

      (beeware-venv) $ briefcase run android

      No Android device was specified. Please specify a specific device on which
      to run the app by passing `-d <device_id>`.

      ...

      If you do not see any devices, you can create and start an emulator by running:

      ...

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>briefcase run android

      No Android device was specified. Please specify a specific device on which
      to run the app by passing `-d <device_id>`.

      ...

      If you do not see any devices, you can create and start an emulator by running:

      ...


Examine the specific output on your system, and run the commands provided
until you see an Android virtual device on the launcher screen.

You will see two steps of Android booting. First, the Android logo will appear.

.. figure:: ../images/android/tutorial-5-booting.png
   :alt: Android virtual device booting

   Android virtual device booting

In the second phase, the launcher screen will appear.

.. figure:: ../images/android/tutorial-5-running.png
   :alt: Android virtual device fully started, on the launcher screen

   Android virtual device fully started, on the launcher screen

Once an Android virtual device is at the launcher screen, you can launch the app
with Briefcase by running this command:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      (beeware-venv) $ briefcase run android -d emulator-5554

  .. group-tab:: Linux

    .. code-block:: bash

      (beeware-venv) $ briefcase run android -d emulator-5554

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>briefcase run android -d emulator-5554

At this point, you should see the app launch on your virtual device. If you see
an error message, you may need to follow the advice in the error message about
finding the correct device name.

Run the app on a physical device
================================

If you have an Android phone or tablet you want to run your app on, you can
use Briefcase's ``run`` command if you enable debugging on your device and
pass its device ID to ``-d <device_id>``.

To find the device name, use the ``run`` command without ``-d`` parameter.

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      (beeware-venv) $ briefcase run android

      No Android device was specified. Please specify a specific device on which
      to run the app by passing `-d <device_id>`.

      ...

      If you do not see any devices, you can create and start an emulator by running:

      ...

  .. group-tab:: Linux

    .. code-block:: bash

      (beeware-venv) $ briefcase run android

      No Android device was specified. Please specify a specific device on which
      to run the app by passing `-d <device_id>`.

      ...

      If you do not see any devices, you can create and start an emulator by running:

      ...

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>briefcase run android

      No Android device was specified. Please specify a specific device on which
      to run the app by passing `-d <device_id>`.

      ...

      If you do not see any devices, you can create and start an emulator by running:

      ...

In the output, you will see a command you can run with **adb** in the name. Run it
and you will see a list similar to the following::

  List of devices attached
  emulator-5554          device product:sdk_phone_x86 model:Android_SDK_built_for_x86 device:generic_x86 transport_id:1
  CoolPhone_038201       device product:cool_phone_1 model:CoolPhone device:coolphone transport_id:2

If you see your device in this list, you can use the device ID from the first
column. In this case, you would run:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      (beeware-venv) $ briefcase run android -d CoolPhone_038201

  .. group-tab:: Linux

    .. code-block:: bash

      (beeware-venv) $ briefcase run android -d CoolPhone_038201

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>briefcase run android -d CoolPhone_038201

If your device appears in this list, but you see the word **unauthorized**, you
likely need to `enable USB debugging on the device <https://developer.android.com/studio/debug/dev-options>`_.


Next steps
==========

We've now got an application on our phone! Is there anywhere other way to
deploy a BeeWare app? Turn to :doc:`Tutorial 6 <../tutorial-6>` to find
out...
