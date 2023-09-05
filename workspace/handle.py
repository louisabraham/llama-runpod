import json
import os

import runpod
from llama_cpp import Llama

args = json.loads(os.environ.get("LLAMA_ARGS", "{}"))
llm = Llama(**args)


def handler(event):
    inp = event["input"]
    return llm(**inp)


runpod.serverless.start({"handler": handler})
