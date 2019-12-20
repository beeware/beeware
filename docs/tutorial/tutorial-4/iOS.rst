==================================
Tutorial 4 - Taking it mobile: iOS
==================================

Now, we're going to take our application, and deploy it as an iOS application.

The process of deploying an application to iOS is very similar to the process
for deploying as a desktop application. First, you run the ``create`` command -
but this time, we specify that we want to create an iOS application:

.. code-block:: bash

  (beeware-venv) $ briefcase create iOS

  [helloworld] Generating application template...
  Using app template: https://github.com/beeware/briefcase-iOS-app-template.git
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

Once this completes, we'll now have an ``iOS`` directory in your project.
This directory will contain a ``Hello World`` folder, which will contain
an Xcode project, as well as the support libraries and the application code
needed for the application.

You can then use briefcase to compile the application compile an installer,
using the ``build`` command:

.. code-block:: bash

  (beeware-venv) $ briefcase build iOS

  [hello-world] Generating application template...
  Using app template: https://github.com/beeware/briefcase-iOS-Xcode-template.git

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

Next steps
==========

We've now got an application on our phone! Is there anywhere other way to
deploy a BeeWare app? Turn to :doc:`Tutorial 5 <../tutorial-5>` to find
out...
