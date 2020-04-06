.. raw:: html

    <style>
        .row {clear: both}

        .column img {border: 1px solid black;}

        @media only screen and (min-width: 1000px),
               only screen and (min-width: 500px) and (max-width: 768px){

            .column {
                padding-left: 5px;
                padding-right: 5px;
                float: left;
            }

            .column3  {
                width: 33.3%;
            }

            .column2  {
                width: 50%;
            }
        }
    </style>

=============================
Tutorial 5 - Taking it Mobile
=============================

So far, we've been running and testing our application on the desktop. However,
BeeWare also supports mobile platforms - and the application we've written
can be deployed to your mobile device, too!

.. rst-class:: clearfix row

.. rst-class:: column column2

:doc:`iOS <iOS>`
----------------

iOS applications can only be compiled on macOS. You'll need `Xcode
<https://apps.apple.com/au/app/xcode/id497799835?mt=12>`__, which you should
have installed in :doc:`Tutorial 0 <../tutorial-0>`.

.. rst-class:: column column2

:doc:`Android <android>`
------------------------

Android applications be compiled on macOS, Windows or Linux.

.. toctree::
    :maxdepth: 1
    :hidden:

    iOS
    android
