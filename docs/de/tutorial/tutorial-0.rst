==============================
Tutorial 0 - Let's get set up!
==============================

Befor Sie ihre erste BeeWare App erstellen, müssen zuerst die folgenden 
Programme installiert werden.

Python installieren
===================

Zuerst brauchen wir Python 3.5 oder höher.

.. tabs::

  .. group-tab:: macOS

    Wenn Sie macOS verwenden, installieren Sie Python von der
    `Python Website <https://www.python.org/downloads>`__. Es ist egal,
    welche Version Sie verwenden, solange es 3.5 oder höher ist.

  .. group-tab:: Linux

    Wenn Sie Linux verwenden, ist Python meist schon vorinstalliert, jedoch können Sie
    es auch noch mit
    (``apt`` auf Debian/Ubuntu/Mint; ``dnf`` auf Fedora, or ``pacman`` auf Arch) installieren.

    Raspberry Pi wird noch nicht unterstützt.

  .. group-tab:: Windows

    Wenn Sie macOS verwenden, installieren Sie Python von der
    `Python Website <https://www.python.org/downloads>`__. Es ist egal,
    welche Version Sie verwenden, solange es 3.5 oder höher ist.

.. admonition:: Alternative Python distributions

    Es gibt viele Wege, wie `homebrew
    <https://docs.brew.sh/Homebrew-and-Python>`__, `pyenv
    <https://github.com/pyenv/pyenv#simple-python-version-management-pyenv>`__, `Anaconda
    <https://docs.anaconda.com/anaconda/install/>`__, `Miniconda
    <https://docs.conda.io/en/latest/miniconda.html>`__
    oder den Windows Store, um Python zu installieren.

    Es ist egal, *wie* Sie Python installiert haben. Das einzige, das zählt, ist,
    dass Sie `python3` in ihrem terminal/ihrer Kommandozeile ausführen können.

.. _install-dependencies:

Voraussetzungen installieren
============================

Als Nächstes, müssen Sie zusätzliche Programme installieren:

.. tabs::

  .. group-tab:: macOS

    Um BeeWare Apps auf macOS zu erstellen, benötigen Sie:

    * **Git**, ein Versions-manager. Sie können Git von
      `git-scm.org <https://git-scm.com/download/>`__ herunterladen.

    * **Xcode**, Apples IDE tools. Sie können Xcode kostenlos vom
      `macOS App Store
      <https://apps.apple.com/au/app/xcode/id497799835?mt=12>`__ herunterladen.

  .. group-tab:: Linux

    Um BeeWare Apps auf Linux zu erstellen, benötigen Sie, abhängig von ihrem
    System:

    **Ubuntu 16.04, Debian 9**

    .. code-block:: bash

      $ sudo apt-get update
      $ sudo apt-get install git python3-dev python3-venv libgirepository1.0-dev libcairo2-dev libpango1.0-dev libwebkitgtk-3.0-0 gir1.2-webkit-3.0

    **Ubuntu 18.04, Debian 10**

    .. code-block:: bash

      $ sudo apt-get update
      $ sudo apt-get install git python3-dev python3-venv libgirepository1.0-dev libcairo2-dev libpango1.0-dev libwebkit2gtk-4.0-37 gir1.2-webkit2-4.0

    **Fedora**

    .. code-block:: bash

      $ sudo dnf install git pkg-config python3-devel gobject-introspection-devel cairo-devel cairo-gobject-devel pango-devel webkitgtk4

    **Arch, Manjaro**

    .. code-block:: bash

      $ sudo pacman -Syu git pkgconf cairo python-cairo pango gobject-introspection gobject-introspection-runtime python-gobject webkit2gtk

    Briefcase nutzt AppImage um Binärdateien für Linux zu erstellen.
    Da das Erstellen von AppImage dateien kompliziert und schwierig ist,
    benutzt Briefcase Docker, um eine immer gleiche Umgebung zu haben.

    Der offiziellen Installer für die `Docker Engine 
    <https://docs.docker.com/engine/install/#server>`__ ist für fast alle
    Unix distributionen erhältlich.
    Wenn die Installation fertiggestellt ist, sollten Sie in der Lage sein,
    mit folgenden Kommandos eine Ubuntu 16.04 virtuelle Maschine zu erstellen:

    .. code-block:: bash

      $ docker run -it ubuntu:16.04

    Nun sollten Sie eine Unix-Kommandozeile (so etwas wie `root@84444e31cff9:/#`) sehen.
    Drücken Sie Ctrl-D um Docker zu beenden und zu ihrer 
    normalen Kommandozeile zurück zu kehren..

  .. group-tab:: Windows

    Um BeeWare Apps auf Windows zu erstellen, benötigen Sie::

    * **Git**, ein Versions-manager. Sie können Git von
      `git-scm.org <https://git-scm.com/download/>`__ herunterladen.

    * **WiX Toolset**, ein Toolset um .msi Installationsdateien zuerst
      kompiliieren. Das Installationsprogramm für WiX können Sie von der
      offiziellen `WiX Toolset Website
      <https://wixtoolset.org/releases/>`__ herunterladen.


Eine virtuelle Umgebung schaffen
================================

Wir nutzen eine virtuelle Umgebung, eine "sandbox", da wir darin unsere Arbeit
in diesem Tutorial von der Haupt Python installation (und allen anderen) separieren.
Daher können wir sie, falls wir unsere gesamte virtuelle Umgebung zerstören,
einfach löschen, ohne direkt Python komplett neu installieren zu müssen.

.. tabs::

  .. group-tab:: macOS

    .. code-block:: bash

      $ mkdir beeware-tutorial
      $ cd beeware-tutorial
      $ python3 -m venv beeware-venv
      $ source beeware-venv/bin/activate

  .. group-tab:: Linux

    .. code-block:: bash

      $ mkdir beeware-tutorial
      $ cd beeware-tutorial
      $ python3 -m venv beeware-venv
      $ source beeware-venv/bin/activate

  .. group-tab:: Windows

    .. code-block:: doscon

      C:\...>md beeware-tutorial
      C:\...>cd beeware-tutorial
      C:\...>py -m venv beeware-venv
      C:\...>beeware-venv\Scripts\activate.bat

Wenn das funktioniert hat, sollte ihre Kommandozeile nun ein
``(beeware-venv)`` Präfix haben. Dieses zeigt an, dass Sie gerade in ihrer
virtuellen Python installation arbeiten. Sie sollten möglichst immer eine
virtuelle Python installation verwenden. Um später wieder auf sie zuzugreifen,
können sie das letzte (``activate``) Kommando wiederholen.

.. admonition:: Alternative virtuelle environments

    Wenn Sie schon öfter Anaconda oder miniconda verwendet haben,
    kennen Sie sich vermutlich schon aus. Im Tutorial verwenden wir
    Pythons standard ``venv`` modul, da es mit der Python installation
    mit installiert wird.
    Letztendlich ist es egal, *wie* Sie ihr virtuelles environment erstellen,
    solange Sie eines haben.

    Genau genommen müssen Sie zwar kein virtuelles environment verwenden, Sie
    *können* Beeware direkt installieren, jedoch ist es *wirklich*, **wirklich**
    zu empfehlen.

Weiter
======

Jetzt haben wir eine virtuelle Umgebung und können :doc:`unsere erste BeeWare app
erstellen. <tutorial-1>`.
