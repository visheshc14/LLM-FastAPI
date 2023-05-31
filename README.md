# LLM-FastAPI
NimbleBox Apprenticeship ML Engineer Task - 1
This project demonstrates the implementation of a Language Model Server using FastAPI and gRPC. It leverages a large language model to generate coherent text based on user input. 

Getting Started
To set up and run the project, follow the steps below:

Install the required Python packages by running 
    ```bash
    pip install -r requirements.txt.
    ```

Train the language model using `trainer.py`. Provide the dataset file (`--fp argument`) and other training arguments as needed. The trained model weights will be saved in a specified location.

Start the language model server by running `uvicorn server:app --host 0.0.0.0 --port 8000`. The server will listen on `http://localhost:8000` and accept text generation requests.

Use the provided APIs or client.py to generate text by sending requests to the server. Example curl command: 
```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "Hello"}' http://localhost:8000/generate
```

Optionally, use test.py to stress test the server's performance and evaluate its response time under load.

## Crux: ML Engineer

Bonus points:
- if the filepath can be a GitHub gist (eg. this gist)
- if everything can be run via single shell file
- if LLM can give coherent reply
- a file `test.py` that can:
  - stress test the server using `multithreading`
  - provide a CLI for using the model *fast*

Ultra bonus points:
- you use gRPC over HTTP/REST
- you use something other than python (but not C++, Javascript FFS)

### Train a language model and serve it over a FastAPI.

- create a github repository
- create a file called `trainer.py` which can be accessed via CLI to train an LLM (protip: take a look at `python-fire`). It should take in following arguments:
  - `fp` the file to finetune the model on
  - some training arguments as well (protip: don't use `huggingface` try `karpathy/minGPT`)
  - the result of this should be the model weights saved in some location
- create a file called `server.py` that serves the LLM over a HTTP/REST over some APIs (protip: use `pydantic` for models)
- A `curl` command to call the model and get response
- an ipython notebook that contains steps to run this