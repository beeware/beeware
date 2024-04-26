:orphan:

====================================
Tutorial 10 - Make this app your own
====================================

So far, our app has used a default "gray bee" icon when it is packaged. Let's
personalize our application by configuring it to use our own icon.

Adding an icon
==============

Every platform uses a different format for application icons - and some
platforms need *multiple* icons in different sizes and shapes. To account for
this, Briefcase provides a shorthand way to configure an icon once, and then
have that definition expand in to all the different icons needed for each
individual platform.

Edit your ``pyproject.toml``, adding a new ``icon`` configuration item in the
``[tool.briefcase.app.helloworld]`` configuration section, just above the
``sources`` definition::

    icon = "icons/helloworld"

This icon definition doesn't specify any file extension. The value will be used as
a prefix; each platform will add additional items to this prefix to build the files
needed for each platform.

We can now run ``briefcase update`` again - but this time, we pass in the
``--update-resources`` flag, telling Briefcase that we want to install new
application resources (i.e., the icons):

.. tabs::

  .. group-tab:: macOS

    .. code-block:: console

      (beeware-venv) $ briefcase update --update-resources

      [helloworld] Updating application code...
      Installing src/helloworld... done

      [helloworld] Updating application resources...
      Unable to find icons/helloworld.icns for application icon; using default

      [helloworld] Removing unneeded app content...
      Removing unneeded app bundle content... done

      [helloworld] Application updated.

  .. group-tab:: Linux

    .. code-block:: console

      (beeware-venv) $ briefcase update --update-resources

      [helloworld] Updating application code...
      Installing src/helloworld... done

      [helloworld] Updating application resources...
      Unable to find icons/helloworld-16.png for 16px application icon; using default
      Unable to find icons/helloworld-32.png for 32px application icon; using default
      Unable to find icons/helloworld-64.png for 64px application icon; using default
      Unable to find icons/helloworld-128.png for 128px application icon; using default
      Unable to find icons/helloworld-256.png for 256px application icon; using default
      Unable to find icons/helloworld-512.png for 512px application icon; using default

      [helloworld] Removing unneeded app content...
      Removing unneeded app bundle content... done

      [helloworld] Application updated.

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>briefcase update --update-resources

      [helloworld] Updating application code...
      Installing src/helloworld... done

      [helloworld] Updating application resources...
      Unable to find icons/helloworld.ico for application icon; using default

      [helloworld] Removing unneeded app content...
      Removing unneeded app bundle content... done

      [helloworld] Application updated.

  .. group-tab:: Android

    .. code-block:: console

      (beeware-venv) $ briefcase update android --update-resources

      [helloworld] Updating application code...
      Installing src/helloworld... done

      [helloworld] Updating application resources...
      Unable to find icons/helloworld-round-48.png for 48px round application icon; using default
      Unable to find icons/helloworld-round-72.png for 72px round application icon; using default
      Unable to find icons/helloworld-round-96.png for 96px round application icon; using default
      Unable to find icons/helloworld-round-144.png for 144px round application icon; using default
      Unable to find icons/helloworld-round-192.png for 192px round application icon; using default
      Unable to find icons/helloworld-square-48.png for 48px square application icon; using default
      Unable to find icons/helloworld-square-72.png for 72px square application icon; using default
      Unable to find icons/helloworld-square-96.png for 96px square application icon; using default
      Unable to find icons/helloworld-square-144.png for 144px square application icon; using default
      Unable to find icons/helloworld-square-192.png for 192px square application icon; using default

      [helloworld] Removing unneeded app content...
      Removing unneeded app bundle content... done

      [helloworld] Application updated.

  .. group-tab:: iOS

    .. code-block:: console

      (beeware-venv) $ briefcase iOS --update-resources

        [helloworld] Updating application code...
        Installing src/helloworld... done

        [helloworld] Updating application resources...
        Unable to find icons/helloworld-20.png for 20px application icon; using default
        Unable to find icons/helloworld-29.png for 29px application icon; using default
        Unable to find icons/helloworld-40.png for 40px application icon; using default
        Unable to find icons/helloworld-58.png for 58px application icon; using default
        Unable to find icons/helloworld-60.png for 60px application icon; using default
        Unable to find icons/helloworld-76.png for 76px application icon; using default
        Unable to find icons/helloworld-80.png for 80px application icon; using default
        Unable to find icons/helloworld-87.png for 87px application icon; using default
        Unable to find icons/helloworld-120.png for 120px application icon; using default
        Unable to find icons/helloworld-152.png for 152px application icon; using default
        Unable to find icons/helloworld-167.png for 167px application icon; using default
        Unable to find icons/helloworld-180.png for 180px application icon; using default
        Unable to find icons/helloworld-1024.png for 1024px application icon; using default

        [helloworld] Removing unneeded app content...
        Removing unneeded app bundle content... done

        [helloworld] Application updated.

This reports the specific icon file (or files) that Briefcase is expecting.
However, as we haven't provided the actual icon files, the install fails, and
falls back to a default value (the same "gray bee" icon).

Let's provide some actual icons. Download :download:`this icons.zip bundle
<./resources/icons.zip>`, and unpack it into the root of your project
directory. After unpacking, your project directory should look something like::

    beeware-tutorial/
        beeware-venv/
            ...
        helloworld/
            ...
            pyproject.toml
            icons/
                helloworld.icns
                helloworld.ico
                helloworld.png
                helloworld-16.png
                ...
            src/
            ...

There's a *lot* of icons in this folder - but they should all look the same: a
green snake on a light blue background:

.. image:: resources/icon.png
    :align: center
    :alt: Icon of green snake with a blue background

This represents all the different icon sizes and shapes you need to support an
app on every platform that Briefcase supports.

Now that we have icons, we can update the application again. ``briefcase
update`` will only copy the updated resources into the build directory; we also
want to rebuild the app to make sure the icon takes effect. To do this, we call
``briefcase build``, passing in the same ``--update-resources`` argument:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: console

      (beeware-venv) $ briefcase build --update-resources

      [helloworld] Updating application code...
      Installing src/helloworld... done

      [helloworld] Updating application resources...
      Installing icons/helloworld.icns as application icon... done

      [helloworld] Removing unneeded app content...
      Removing unneeded app bundle content... done

      [helloworld] Application updated.

      [helloworld] Ad-hoc signing app...
           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100.0% • 00:01

      [helloworld] Built build/helloworld/macos/app/Hello World.app

  .. group-tab:: Linux

    .. code-block:: console

      (beeware-venv) $ briefcase build --update-resources

      [helloworld] Updating application code...
      Installing src/helloworld... done

      [helloworld] Updating application resources...
      Installing icons/helloworld-16.png as 16px application icon... done
      Installing icons/helloworld-32.png as 32px application icon... done
      Installing icons/helloworld-64.png as 64px application icon... done
      Installing icons/helloworld-128.png as 128px application icon... done
      Installing icons/helloworld-256.png as 256px application icon... done
      Installing icons/helloworld-512.png as 512px application icon... done

      [helloworld] Removing unneeded app content...
      Removing unneeded app bundle content... done

      [helloworld] Application updated.

      [helloworld] Building application...
      Build bootstrap binary...
      ...

      [helloworld] Built build/helloworld/linux/ubuntu/jammy/helloworld-0.0.1/usr/bin/helloworld

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>briefcase build --update-resources

      [helloworld] Updating application code...
      Installing src/helloworld... done

      [helloworld] Updating application resources...
      Installing icons/helloworld.ico as application icon... done

      [helloworld] Removing unneeded app content...
      Removing unneeded app bundle content... done

      [helloworld] Application updated.

      [helloworld] Building App...
      Removing any digital signatures from stub app... done
      Setting stub app details... done

      [helloworld] Built build\helloworld\windows\app\src\Hello World.exe

  .. group-tab:: Android

    .. code-block:: console

      (beeware-venv) $ briefcase build android --update-resources

      [helloworld] Updating application code...
      Installing src/helloworld... done

      [helloworld] Updating application resources...
      Installing icons/helloworld-round-48.png as 48px round application icon... done
      Installing icons/helloworld-round-72.png as 72px round application icon... done
      Installing icons/helloworld-round-96.png as 96px round application icon... done
      Installing icons/helloworld-round-144.png as 144px round application icon... done
      Installing icons/helloworld-round-192.png as 192px round application icon... done
      Installing icons/helloworld-square-48.png as 48px square application icon... done
      Installing icons/helloworld-square-72.png as 72px square application icon... done
      Installing icons/helloworld-square-96.png as 96px square application icon... done
      Installing icons/helloworld-square-144.png as 144px square application icon... done
      Installing icons/helloworld-square-192.png as 192px square application icon... done

      [helloworld] Removing unneeded app content...
      Removing unneeded app bundle content... done

      [helloworld] Application updated.

  .. group-tab:: iOS

    .. code-block:: console

      (beeware-venv) $ briefcase build iOS --update-resources

      [helloworld] Updating application code...
      Installing src/helloworld... done

      [helloworld] Updating application resources...
      Installing icons/helloworld-20.png as 20px application icon... done
      Installing icons/helloworld-29.png as 29px application icon... done
      Installing icons/helloworld-40.png as 40px application icon... done
      Installing icons/helloworld-58.png as 58px application icon... done
      Installing icons/helloworld-60.png as 60px application icon... done
      Installing icons/helloworld-76.png as 76px application icon... done
      Installing icons/helloworld-80.png as 80px application icon... done
      Installing icons/helloworld-87.png as 87px application icon... done
      Installing icons/helloworld-120.png as 120px application icon... done
      Installing icons/helloworld-152.png as 152px application icon... done
      Installing icons/helloworld-167.png as 167px application icon... done
      Installing icons/helloworld-180.png as 180px application icon... done
      Installing icons/helloworld-1024.png as 1024px application icon... done

      [helloworld] Removing unneeded app content...
      Removing unneeded app bundle content... done

      [helloworld] Application updated.

With our icons installed, we can now run our app with the new icon:

.. tabs::

  .. group-tab:: macOS

    .. code-block:: console

      (beeware-venv) $ briefcase run

      [helloworld] Starting app...

  .. group-tab:: Linux

    .. code-block:: console

      (beeware-venv) $ briefcase run

      [helloworld] Starting app...

  .. group-tab:: Windows

    .. code-block:: doscon

      (beeware-venv) C:\...>briefcase run

      [helloworld] Starting app...

  .. group-tab:: Android

    .. code-block:: console

      (beeware-venv) $ briefcase run android

      [helloworld] Starting app...

  .. group-tab:: iOS

    .. code-block:: console

      (beeware-venv) $ briefcase run iOS

      [helloworld] Starting app...

Just as Briefcase provides an option to update *code* before running the app with the
``-u`` option, you can also update resources before running. If you run ``briefcase run
--update-resources``, the app's resources will be updated, and then the app will be
started.

Next steps
==========

This has been a taste for what you can do with the tools provided by the
BeeWare project. What you do from here is up to you!

Some places to go from here:

* Tutorials demonstrating `features of the Toga widget toolkit
  <https://toga.readthedocs.io/en/latest/tutorial/index.html>`__.
* Details on the `options available when configuring your Briefcase project
  <https://briefcase.readthedocs.io/en/latest/reference/index.html>`__.

.. We've now got an application with a custom icon on our desktop and phone! How do
.. we share this application with everyone else? Turn to :doc:`Tutorial 11
.. <tutorial-11>` to find out...
