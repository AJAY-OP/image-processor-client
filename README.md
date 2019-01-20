# image-processor-client
Asynchronous image-processor python client for [image-processor] API server.


### Installation
To install image processor client library, you can use following command:
```sh
python3 -m pip install image-processor-client
```

### Basic Example
```python
import asyncio
from image_processor_client import Client

client = Client()

loop = asyncio.get_event_loop()
meme_bytes = loop.run_until_complete(client.memes.rip("Python", "https://i.imgur.com/U5QR5SY.png"))

with open("rip_meme.png", "wb") as meme_file:
    meme_file.write(meme_bytes)
 
 
```


### Requiremets
* Python 3.6+
* `aiohttp`
* [image-processor] API Server (if self-hosted)


### Documentation
For all of the available methods and ful API reference, check our [documentaion]. 

[image-processor]: https://github.com/thec0sm0s/image-processor
[documentaion]: https://image-processor-client.readthedocs.io/en/latest/
