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


=======
BeeWare
=======

BeeWare is a Python native, OS native, cross platform GUI toolkit. Toga consists of a library of base components with a shared
interface to simplify platform-agnostic GUI development.

BeeWare is a suite of tools and libraries, each of which works together to help you write cross platform native GUI applications:

* `Toga <toga.readthedocs.org>`__, a cross platform widget toolkit
* `Briefcase <briefcase.readthedocs.org>`__, an application packaging tool
* `Rubicon <rubicon-objc.readthedocs.org>`__, a library for accessing Objective C libraries on iOS and macOS
* `VOC <voc.readthedocs.org>`__, a compiler for converting Python into Java bytecode
* `Batavia <batavia.readthedocs.org>`__, an interpreter for running Python in a web browser.
* and more.

You can use each of the tools in isolation, or you can use all of them as a suite. There is a `beeware` helper tool to assit using all the tools as a suite.

The BeeWare suite is available on Mac OS, Windows, Linux (GTK); mobile platforms such as Android and iOS; and for the Web.


.. rst-class::  row

Table of contents
=================

.. rst-class:: clearfix row

.. rst-class:: column column2


:ref:`Tutorial <tutorial>`
------------------------------

Get started with a hands-on introduction to BeeWare for beginners

.. rst-class:: column column2


:ref:`How-to guides <how-to>`
-----------------------------

Guides and recipes for common problems and tasks


.. rst-class:: column column2

:ref:`Background <background>`
------------------------------

Explanation and discussion of key topics and concepts


.. rst-class:: column column2

:ref:`Reference <reference>`
------------------------------

Technical reference - commands, modules, classes, methods


.. rst-class:: clearfix row


Community
=========

You can talk to the community through:

 * `@pybeeware on Twitter`_

 * `pybee/general on Gitter`_

.. _BeeWare suite: http://pybee.org
.. _Read The Docs: https://toga.readthedocs.io
.. _@pybeeware on Twitter: https://twitter.com/pybeeware
.. _pybee/general on Gitter: https://gitter.im/pybee/general


.. toctree::
   :maxdepth: 2
   :hidden:
   :titlesonly:


   tutorial/index
   how-to/index
   reference/index
   background/index
