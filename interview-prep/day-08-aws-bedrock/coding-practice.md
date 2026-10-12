# Day 8 — Coding Practice: Bedrock Service

## Task
Implement `generate_text()` in `app/services/bedrock_service.py` so it:
1. Rejects an empty prompt.
2. Rejects `max_tokens < 1`.
3. Uses a provided client for tests, or creates a Bedrock Runtime boto3 client when no client is supplied.
4. Calls the Converse API with one user message.
5. Returns the generated text from the response.

## Implementation
See `app/services/bedrock_service.py`. It accepts a client dependency so tests can use a fake client and avoid AWS credentials/network calls.

## Run tests
```bash
pip install -r requirements.txt
pytest -q
```

## Exercises
1. Add a test that verifies `temperature` and `maxTokens` are passed through.
2. Add a test for an empty prompt.
3. Add a test for invalid max tokens.
4. Extend the service to handle a missing/empty response with a clear exception.
5. Explain why a synchronous boto3 call should not directly block an async FastAPI event loop.
6. Sketch how you would expose this service through a FastAPI endpoint without putting AWS credentials in request data.

## Complexity
Building the request is O(1) relative to prompt length at the Python object level; actual request serialization, network time, model inference, and response processing depend on input/output size and the service/model.
