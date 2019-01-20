.. _intro:



Introduction
============

Image Processor Client is an asynchronous python wrapper for `Image Processor`__ API
which has various available pre-made image processing models and methods
and can be used as image processing library in asynchronous applications
easily.


Requirements
------------

Client uses ``aiohttp`` to send and receive requests to server asynchronously
in non-blocking manner.
**Python 3.6** is recommended. Python 3.4 or lower is not supported due to
aiohttp requirements.

In most of the cases, you will want to self host the `Image Processor`_ API server
locally for better performance and response time rather using public API which
is open for everyone.


Installing
----------

You can install the library directly from PyPI using PIP by following command in shell or command prompt: ::

    python3 -m pip install -U image-processor-client

You can also install latest development version (**maybe unstable/broken**) by following commnd: ::

    python3 -m pip install -U git+https://github.com/thec0sm0s/image-processor-client.git


Basic Usage
-----------

Although library is meant to used within other asynchronous applications,
but its basic usage can be making request to server to process an example meme
and save it to our disk locally.

We will use asyncio to run asynchronous functions.

.. code-block:: python3

        import asyncio
        from image_processor_client import Client

        client = Client()
        loop = asyncio.get_event_loop()

        async_function = client.memes.rip("Python", "https://i.imgur.com/U5QR5SY.png")
        meme_bytes = loop.run_until_complete(async_function)

        with open("python_rip.png", "wb") as meme_file:
            meme_file.write(meme_bytes)




.. _Image Processor: https://github.com/thec0sm0s/image-processor/
__ Image Processor_
