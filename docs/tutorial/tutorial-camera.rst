:orphan:

===========================
Tutorial 12 - Camera access
===========================

In this tutorial, we will use the camera on a mobile device. Important
clarification, this will only work when installing the application on an actual
mobile device; it will *not* work using an emulator on your development machine
and will *not* work using the desktop or web versions of the application.

Prerequisites
=============

Make sure you at least have gotten to the point where you have the skeleton
application running in developer mode. See the :doc:`first <tutorial-0>`
:doc:`two <tutorial-1>` tutorials for details. Short story shorter, run the
following commands in an empty directory.


.. tabs::
    .. group-tab:: macOS
        .. code-block:: console

            $ python3 -m venv beeware-venv
            $ source beeware-venv/bin/activate
            (beeware-venv)$ python -m pip install briefcase
            (beeware-venv)$ briefcase new
            (beeware-venv)$ cd helloworld
            (beeware-venv)$ briefcase dev

    .. group-tab:: Linux
        .. code-block:: console

            $ python3 -m venv beeware-venv
            $ source beeware-venv/bin/activate
            (beeware-venv)$ python -m pip install briefcase
            (beeware-venv)$ briefcase new
            (beeware-venv)$ cd helloworld
            (beeware-venv)$ briefcase dev

    .. group-tab:: Windows
        .. code-block:: doscon

            C:\...>py -m venv beeware-venv
            C:\...>beeware-venv\Scripts\activate
            (beeware-venv) C:\...>python -m pip install briefcase
            (beeware-venv) C:\...>briefcase new
            (beeware-venv) C:\...>cd helloworld
            (beeware-venv) C:\...>briefcase dev


The skeleton application should appear on your development machine. Exit the
window and continue.

Take a photo
============

In order to add camera support, the highlighted code needs to be added to the
code in your project's ``app.py`` file. If you've accepted all the default
settings while bootstrapping the application, the full path of the file will be
``helloworld/src/helloworld/app.py``.


.. code-block:: python
    :emphasize-lines: 20-28, 34-51

    """
    My first application
    """

    import toga
    from toga.style import Pack
    from toga.style.pack import COLUMN, ROW


    class HelloWorld(toga.App):
        def startup(self):
            """Construct and show the Toga application.

            Usually, you would add your application to a main content box.
            We then create a main window (with a name matching the app), and
            show the main window.
            """
            main_box = toga.Box()

            self.photo = toga.ImageView(style=Pack(height=300, padding=5))
            camera_button = toga.Button(
                "Take photo",
                on_press=self.take_photo,
                style=Pack(padding=5)
            )

            main_box.add(self.photo)
            main_box.add(camera_button)

            self.main_window = toga.MainWindow(title=self.formal_name)
            self.main_window.content = main_box
            self.main_window.show()

        async def take_photo(self, widget, **kwargs):
            try:
                if not self.camera.has_permission:
                    await self.camera.request_permission()

                image = await self.camera.take_photo()
                if image:
                    self.photo.image = image
            except NotImplementedError:
                await self.main_window.info_dialog(
                    "Oh no!",
                    "The Camera API is not implemented on this platform",
                )
            except PermissionError:
                await self.main_window.info_dialog(
                    "Oh no!",
                    "You have not granted permission to take photos",
                )


    def main():
        return HelloWorld()


The first highlighted code block creates two widgets, an ``ImageView`` to
display the photo and a ``Button`` to take the photo, and adds them to the GUI
layout. The second highlighted code block defines the event handler that
either takes the photo or throws an appropriate error.

Device Permissions
==================

We will try to run the application on our mobile device, but find we are not
quite there yet. From the directory with the ``pyproject.toml`` file, run the
commands to deploy the application to your mobile device.

.. tabs::

  .. group-tab:: macOS
    .. tabs::
      .. group-tab:: Android
            .. code-block:: console

                (beeware-venv)$ briefcase create android
                (beeware-venv)$ briefcase build android
                (beeware-venv)$ briefcase run android

      .. group-tab:: iOS
            .. code-block:: console

                (beeware-venv)$ briefcase create iOS
                (beeware-venv)$ briefcase build iOS
                (beeware-venv)$ briefcase run iOS

  .. group-tab:: Linux
    .. tabs::
      .. group-tab:: Android
            .. code-block:: console

                (beeware-venv)$ briefcase create android
                (beeware-venv)$ briefcase build android
                (beeware-venv)$ briefcase run android

      .. group-tab:: iOS
            .. code-block:: console

                (beeware-venv)$ briefcase create iOS
                (beeware-venv)$ briefcase build iOS
                (beeware-venv)$ briefcase run iOS

  .. group-tab:: Windows
    .. tabs::
      .. group-tab:: Android
            .. code-block:: doscon

                (beeware-venv) C:\...>briefcase create android
                (beeware-venv) C:\...>briefcase build android
                (beeware-venv) C:\...>briefcase run android

      .. group-tab:: iOS
            .. code-block:: doscon

                (beeware-venv) C:\...>briefcase create iOS
                (beeware-venv) C:\...>briefcase build iOS
                (beeware-venv) C:\...>briefcase run iOS


For more details on installing your application to a mobile device, see
:doc:`Tutorial 5 <tutorial-5/index>`.

Once the app has successfully started on your mobile device, you will notice
that you are still not yet able to take a picture. This is because the project
did not specify it will need camera permissions in the ``pyproject.toml`` file.
Add the following line:

.. code-block:: toml

    [tool.briefcase.app.helloworld]
    ...
    permission.camera = "App will take mugshots."


Deploy the application to the mobile device again.

.. tabs::

  .. group-tab:: macOS
    .. tabs::
      .. group-tab:: Android
            .. code-block:: console

                (beeware-venv)$ briefcase build android
                (beeware-venv)$ briefcase run android
      .. group-tab:: iOS
            .. code-block:: console

                (beeware-venv)$ briefcase build iOS
                (beeware-venv)$ briefcase run iOS

  .. group-tab:: Linux
    .. tabs::
      .. group-tab:: Android
            .. code-block:: console

                (beeware-venv)$ briefcase build android
                (beeware-venv)$ briefcase run android

      .. group-tab:: iOS
            .. code-block:: console

                (beeware-venv)$ briefcase build iOS
                (beeware-venv)$ briefcase run iOS

  .. group-tab:: Windows
    .. tabs::
      .. group-tab:: Android
            .. code-block:: doscon

                (beeware-venv) C:\...>briefcase build android
                (beeware-venv) C:\...>briefcase run android

      .. group-tab:: iOS
            .. code-block:: doscon

                (beeware-venv) C:\...>briefcase build iOS
                (beeware-venv) C:\...>briefcase run iOS


This also doesn't work. This is because modifications to the ``pyproject.toml``
file require completely recreating the project. 


.. tabs::

  .. group-tab:: macOS
    .. tabs::
      .. group-tab:: Android
            .. code-block:: console

                (beeware-venv)$ briefcase create android
                (beeware-venv)$ briefcase build android
                (beeware-venv)$ briefcase run android

      .. group-tab:: iOS
            .. code-block:: console

                (beeware-venv)$ briefcase create iOS
                (beeware-venv)$ briefcase build iOS
                (beeware-venv)$ briefcase run iOS

  .. group-tab:: Linux
    .. tabs::
      .. group-tab:: Android
            .. code-block:: console

                (beeware-venv)$ briefcase create android
                (beeware-venv)$ briefcase build android
                (beeware-venv)$ briefcase run android

      .. group-tab:: iOS
            .. code-block:: console

                (beeware-venv)$ briefcase create iOS
                (beeware-venv)$ briefcase build iOS
                (beeware-venv)$ briefcase run iOS

  .. group-tab:: Windows
    .. tabs::
      .. group-tab:: Android
            .. code-block:: doscon

                (beeware-venv) C:\...>briefcase create android
                (beeware-venv) C:\...>briefcase build android
                (beeware-venv) C:\...>briefcase run android

      .. group-tab:: iOS
            .. code-block:: doscon

                (beeware-venv) C:\...>briefcase create iOS
                (beeware-venv) C:\...>briefcase build iOS
                (beeware-venv) C:\...>briefcase run iOS


The application should launch on your mobile device, click the button to take a
picture and it should appear in the GUI.
