# image-processor-client
Asynchronous image-processor python client for [image-processor] server.


### Installation
To install image processor client library, you can use following command:
```sh
python3 -m pip install -U git+https://github.com/thec0sm0s/image-processor-client
```

### Basic Example
```python
import asyncio
import image_processor

client = image_processor.Client()

loop = asyncio.get_event_loop()
meme_bytes = loop.run_until_complete(client.memes.rip("Python", "https://i.imgur.com/U5QR5SY.png"))

with open("rip_meme.png", "wb") as meme_file:
    meme_file.write(meme_bytes)
 
 
```


### Requiremets
* Python 3+
* `aiohttp`
* [image-processor]

[image-processor]: https://github.com/thec0sm0s/image-processor