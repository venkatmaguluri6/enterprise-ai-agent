# Day 9 — Coding and Design Practice

## Exercise 1: Design a chat endpoint
Design `POST /chat` for an application that calls Amazon Bedrock.

Example request:
```json
{
  "message": "Explain retrieval-augmented generation",
  "conversation_id": "optional-session-id"
}
```

Example response:
```json
{
  "answer": "RAG retrieves relevant information and provides it to a model as context.",
  "request_id": "example-request-id"
}
```

Define:
- Which fields are required and their maximum lengths.
- How the caller is authenticated.
- Which API Gateway route/integration is used.
- How FastAPI validates and processes the request.
- What safe error responses are returned.
- Which metrics and logs help diagnose failures.

## Exercise 2: Route and status-code debugging
For each symptom, name the first two things you would inspect:
- 401 Unauthorized
- 403 Forbidden
- 429 Too Many Requests
- 502/503/504 integration or backend errors
- High latency with a successful response

Suggested starting points:
- 401/403: authorizer, IAM/resource policy, token validity, and permissions.
- 429: gateway/backend throttling and service quotas.
- 5xx: integration settings, backend health, permissions, and timeouts.
- High latency: gateway integration latency, backend timing, model latency, and payload size.

## Exercise 3: Add a Pydantic request model
Write a Pydantic model for the chat request that:
- Requires a non-empty `message`.
- Trims whitespace or rejects whitespace-only input.
- Limits message length.
- Makes `conversation_id` optional with a reasonable maximum length.

Then write tests for valid input, empty input, whitespace-only input, and overlong input.

## Exercise 4: Draw the architecture
Draw and explain this path:
Client → API Gateway → FastAPI backend → Bedrock Runtime → response.

For a production design, discuss where TLS terminates, how the caller is authorized, how the backend is reached, how timeouts are handled, and how request IDs/metrics are correlated.

## Exercise 5: Production scenario
A demo works locally, but after API Gateway deployment requests return 504. Make a checklist covering:
1. Integration timeout and supported limits.
2. Backend health and reachability.
3. Network/VPC Link/load-balancer configuration if applicable.
4. Model call duration and backend timeout.
5. Logs/metrics for gateway and backend.
6. Whether a long-running job should be asynchronous instead.

## Optional local practice
Run the existing FastAPI application locally and inspect its OpenAPI document at `/openapi.json`. This helps separate the API contract from the AWS deployment/integration configuration.

## Day 9 memory prompt
**Route → Authorize → Throttle → Integrate → Observe.**
Then the backend validates the request, applies business logic, calls the model, and returns the response.
