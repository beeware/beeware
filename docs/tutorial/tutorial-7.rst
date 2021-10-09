===============================
Tutorial 7 - Making it Smooooth
===============================

Unless you've got a *really* fast internet connection, you may notice that when
you press the button, the GUI for your app locks up for a little bit. This is
because the web request we have made is *synchronous*. When our application makes
the web request, it waits for the API to return a response before continuing.
While it's waiting, it *isn't* allowing the application to redraw - and as a
result, the application locks up.

Asynchronous programming
========================

**Coming soon**

Next steps
==========

We've now got an application that is slick and responsive, even when it's
waiting on a slow API. But it still looks like a tutorial app. Is there anything
we can do about that? Turn to :doc:`Tutorial 8 <tutorial-8>` to find out...
