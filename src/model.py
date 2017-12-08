from definitions import model_path


def train():
  print('Training...')
  # Training will produce the model file
  with open(model_path, 'w+') as f:
    f.write('the good stuff')

def test():
  print('Testing!')
  


def predict(data):
  return {'prediction': 'now-using-nginx'}
