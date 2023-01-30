==================================
Tutorial 5 - Taking it mobile: iOS
==================================

Now, we're going to take our application, and deploy it as an iOS application.

The process of deploying an application to iOS is very similar to the process
for deploying as a desktop application. First, you run the ``create`` command -
but this time, we specify that we want to create an iOS application:

.. code-block:: bash

  (beeware-venv) $ briefcase create iOS

  [helloworld] Generating application template...
  Using app template: https://github.com/beeware/briefcase-iOS-Xcode-template.git, branch v0.3.12
  ...
  [helloworld] Installing support package...
  ...
  [helloworld] Installing application code...
  ...
  [helloworld] Installing requirements...
  ...
  [helloworld] Installing application resources...
  ...
  [helloworld] Created iOS/Xcode/Hello World

Once this completes, we'll now have an ``iOS`` directory in your project.
This directory will contain a ``Hello World`` folder, which will contain
an Xcode project, as well as the support libraries and the application code
needed for the application.

You can then use Briefcase to compile your app using ``briefcase build iOS``:

.. code-block:: bash

  (beeware-venv) $ briefcase build iOS

  [helloworld] Updating app metadata...
  Setting main module... done

  [helloworld] Building XCode project...
  ...
  Building... done

  [helloworld] Built iOS/Xcode/Hello World/build/Debug-iphonesimulator/Hello World.app

We're now ready to run our application, using ``briefcase run iOS``. You'll be
prompted to select a device to compile for; if you've got simulators for
multiple iOS SDK versions installed, you may also be asked which iOS version you
want to target. The options you are shown may differ from the options show in
this output - at the very least, the list of devices will likely be different.
For our purposes, it doesn't matter which simulator you pick.

.. code-block:: bash

  (beeware-venv) $ briefcase run iOS

  Select simulator device:

     1) iPad (10th generation)
     2) iPad Air (5th generation)
     3) iPad Pro (11-inch) (4th generation)
     4) iPad Pro (12.9-inch) (6th generation)
     5) iPad mini (6th generation)
     6) iPhone 14
     7) iPhone 14 Plus
     8) iPhone 14 Pro
     9) iPhone 14 Pro Max
     10) iPhone SE (3rd generation)

  >  10

  In the future, you could specify this device by running:

      $ briefcase run iOS -d "iPhone SE (3rd generation)::iOS 16.2"

  or:

      $ briefcase run iOS -d 2614A2DD-574F-4C1F-9F1E-478F32DE282E

  [helloworld] Starting app on an iPhone SE (3rd generation) running iOS 16.2 (device UDID 2614A2DD-574F-4C1F-9F1E-478F32DE282E)
  Opening simulator... done

  [helloworld] Installing app...
  Uninstalling any existing app version... done
  Installing new app version... done

  [helloworld] Starting app...
  Launching app... done

  [helloworld] Following simulator log output (type CTRL-C to stop log)...
  ===========================================================================
  ...

This will start the iOS simulator, install your app, and start it. You should
see the simulator start, and eventually open your iOS application:

.. image:: ../images/iOS/tutorial-5.png
   :alt: Hello World Tutorial 5 window, on iOS

If you know ahead of time which iOS simulator you want to target, you can tell
Briefcase to use that simulator by providing a ``-d`` (or ``--device``) option.
Using the name of the device you selected when you built your application, run::

    $ briefcase run iOS -d "iPhone SE (3rd generation)"

If you have multiple iOS versions available, Briefcase will pick the highest
iOS version; if you want to pick a particular iOS version, you tell it to use
that specific version::

    $ briefcase run iOS -d "iPhone SE (3rd generation)::iOS 15.5"

Or, you can name a specific device UDID::

    $ briefcase run iOS -d 2614A2DD-574F-4C1F-9F1E-478F32DE282E

Next steps
==========

We've now got an application on our phone! Is there anywhere else we can deploy
a BeeWare app? Turn to :doc:`Tutorial 6 <../tutorial-6>` to find out...
