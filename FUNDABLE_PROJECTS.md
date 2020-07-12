# Fundable projects

The BeeWare project is largely driven by volunteer contributions. We derive
a small income from [financial memberships](https://beeware.org/bee/join),
which is enough to cover promotional and hosting costs; but is not currently
sufficient to pay a developer salary.

However, BeeWare [recently received a US$50k
grant](https://beeware.org/news/buzz/beeware-project-awarded-a-psf-education-grant/)
from the [Python Software Foundation](https://www.python.org/psf-landing/).
This funding enabled us to a [hire a contractor](https://beeware.org/news/buzz/we-have-a-contractor-for-our-android-contract/), who was able to perform a
complete rewrite of BeeWare's Android support in a little over 6 months.

The success of this project shows the impact that adequate funding can have.
There is still much work that could be done to improve the BeeWare ecosystem;
in the interests of expediting that work, we should investigate options for
other grants.

## Project ideas

The following are projects ideas that could be submitted for grants:

### Binary wheels for mobile platforms

The Python packaging ecosystem has defined the *Wheel* format as a way to
distribute packages. This wheels make it easy for developers to share code, uploading wheels to PyPI, and installing wheels into their own projects.

These wheels fall into two major types, depending on the composition of the
project being packaged.

1. **Pure Python wheels**, which are little more than an archive of Python
   code. They will run on any Python install.

2. **Binary wheels**, which include a machine-dependent compiled component,
   which is machine dependent. Wheels for macOS, Windows and Linux are commonly
   available on PyPI. However, there is no mechanism for building wheels for
   mobile platforms (iOS and Android).

This is problematic because many packages in the Python ecosystem - especially
in the numeric Python space - include a compiled component, and must be
distributed as binary wheels. NumPy, SciPy, Pandas, TensorFlow, and more all
have a binary component, and thus must be distributed as binary wheels.

Mobile platforms pose 2 challenges for the Wheel format:

 * They require parallel support of multiple architectures. Whereas a Windows package can be distributed for a single x86-64 architecture, an iOS package must support x86, x86-64, armv7 and aarch64.

 * iOS and Android have very specific requirements for project layout that don't map exactly to the layout favoured by the Wheel format.

We need to develop the tooling to:

 * Create binary wheels for use on iOS and Android.

 * Use binary wheels in an iOS and Android project

At the conclusion of the project, it should be possible to build an app that specifies NumPy as a dependency, build that app for iOS and Android, and submit that app to the App/Play Stores.

## CI infrastructure for Mobile CPython

At present, there is no automated CI infrastructure for the Python support
packages used by BeeWare. These support packages are builds of the CPython source code, compiled for use on iOS and Android.

A number of patches are applied to the source tree to make this compilation
possible. These patches should undergo automated testing before the release of
a new support package. However, at present, testing is only performed on an
ad-hoc basis. This is because commonly avaialble CI providers don't provide
mobile platforms as options in their build farms.

The CPython core team has indicated that a pre-requisite for merging any patches for mobile support into CPython is the ability to perform CI checks, on both simulated and physical hardware.

This project would investigate the options for running CI on simulated and physical devices, and develop the necessary tooling to perform CI on the support packages.

## Develop a WASM story for Python

The emergence of WASM provides an opportunity for Python to be used as a client-side language in the browser.

The aim of this project would be to develop the tooling to allow the execution of Python in the browser.

## Device APIs for Toga

Toga provides a cross platform abtraction API for widgets. It should also support other device capabilities such as:

 * Taking photos with the Camera
 * Selecting a photo from the photo library
 * Playing and recording sound
 * Playing and recording video
 * GPS, Geolocation and Geofencing
 * Accelerometer readings
 * Augmented Reality

Some of these capabilities may be useful on desktop platforms as well.

## Toga source code widget

One major capability gap in Toga at present is the ability to display and edit source code. A source code widget is needed to build an editor, but also many other tools that support the development process, like coverage visualizers, debuggers, diff viewers, and code notepads all depend on a code widget.

For this grant, the BeeWare project would develop a text editor widget for Toga.
The end goal would be a widget that supports:
 * rendering text,
 * editing text,
 * rendering line numbers for that text,
 * rendering colored syntax highlighting,
 * block-level code folding; and
 * context-specific menus.

This widget would have implementations for iOS, Android, macOS, Windows, and Linux.

At the conclusion of the project, it should be possible to build an analog of the IDLE editor using Toga, as well as many other tools.
