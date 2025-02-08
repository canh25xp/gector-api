# Gector API

## Test the API

```sh
# Using curl
curl -X POST -H "Content-Type: application/json" -d '{"model": "GECToR-Roberta", "text_input_list": ["He do this", "I is a engineer"]}' http://localhost:3000/components/model

# Or send a json file
curl -X POST -H "Content-Type: application/json" -d @request.json http://localhost:3000/components/model

# Using python
python request.py
```
