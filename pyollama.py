import ollama # pip install ollama

def convert_nanoseconds_to_seconds(nanoseconds):
    return nanoseconds / 1_000_000_000

def run_multimodel_models(model, prompt, images):
   response = ollama.generate(
      model=model,
      prompt=prompt,
      images=images
   )
   return response

def run_model(model, prompt, stream=False):
  res = ollama.generate(
    model=model, 
    prompt=prompt,
    stream=stream
  )
  return res

def list_models_names():
  models = [model for model in ollama.list()['models']]
  return [model['name'] for model in models]