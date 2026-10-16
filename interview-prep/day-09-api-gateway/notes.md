# Day 9 — Amazon API Gateway

## Goal
Understand how to expose a backend or GenAI service safely to clients, explain the main API Gateway features in interviews, and design a production-minded API front door.

## 80/20: What is API Gateway?
Amazon API Gateway is a managed service for creating, publishing, securing, monitoring, and managing APIs. It can route incoming API requests to supported backends such as Lambda functions or HTTP endpoints.

## Request flow
Client → API Gateway → authentication/authorization and request controls → integration/backend → response back to client.

For a GenAI application:
Client → API Gateway → FastAPI service (or Lambda) → Bedrock Runtime → model → response.

API Gateway is not the LLM and does not replace FastAPI business logic. It is an API entry point and management layer.

## API types — high-level comparison

| Option | Typical use |
|---|---|
| HTTP API | Lower-cost, lower-latency API proxying and common authorization needs |
| REST API | More feature-rich API management needs, depending on requirements |
| WebSocket API | Persistent two-way communication over WebSockets |

Choose based on required features, integrations, security, observability, quotas, and cost—not by memorizing that one is always better.

## Common integrations
- **Lambda:** API Gateway invokes a Lambda function.
- **HTTP backend:** API Gateway forwards requests to a supported HTTP endpoint, such as a service behind a load balancer, when configured appropriately.
- **Other AWS services:** supported service integrations can avoid an intermediate application in selected architectures.

For a containerized FastAPI app, API Gateway is not automatically a direct replacement for a load balancer. Validate the chosen integration and networking design. A common architecture is API Gateway → VPC Link/private integration → load balancer → FastAPI service, where supported and configured.

## Core features to know
- **Routes/resources and methods:** map incoming paths and HTTP methods to integrations.
- **Stages and deployments:** publish a configured API version to a named stage such as dev or prod; exact deployment behavior depends on API type.
- **Authorization:** options can include IAM authorization, JWT authorizers for supported HTTP API configurations, Cognito or Lambda authorizers depending on API type and setup.
- **Throttling and quotas:** limit request rates/bursts and help protect backends. Limits are not a substitute for application-level abuse prevention.
- **CORS:** browser cross-origin policy configuration; configure allowed origins, methods, and headers deliberately.
- **Logging and metrics:** monitor requests, errors, latency, and integration failures; avoid logging secrets or sensitive request bodies unnecessarily.
- **Validation and payload limits:** validate requests at the edge where supported, and also validate in the application.
- **Caching:** available in some API configurations; use only when responses can safely be reused.
- **Custom domains and TLS:** expose stable API domains and secure client connections.

## Authentication vs authorization
- **Authentication:** who is making the request?
- **Authorization:** what is that identity allowed to do?
- API Gateway can enforce selected authorization policies, but the backend must still enforce business-level permissions where needed.
- Do not trust user identity claims unless they are validated by the configured authorizer and safely passed to the backend.

## Example architecture for an AI chat API
1. Client calls `POST /chat` with a prompt.
2. API Gateway applies TLS, route matching, configured authorization, throttling, and request controls.
3. Integration forwards the request to a FastAPI backend or Lambda.
4. Backend validates the request, applies business rules, and calls Bedrock Runtime.
5. Backend returns a controlled JSON response.
6. Gateway returns the response; logs/metrics help diagnose latency and errors.

## Security and reliability checklist
- Use HTTPS and a suitable authorizer or IAM authorization for the use case.
- Apply least privilege to backend identities and integration permissions.
- Set sensible request/response limits, timeouts, throttling, and bounded retries.
- Do not assume gateway throttling prevents all abuse; add per-user/application controls when required.
- Validate input in the backend even if edge validation is enabled.
- Keep secrets in a secrets manager or supported secure configuration—not source control.
- Avoid logging prompts, tokens, authorization headers, or personal data by default.
- Configure CORS narrowly for browser clients.
- Monitor 4xx/5xx rates, integration latency, throttling, and backend errors.
- Test unauthorized requests, malformed payloads, oversized inputs, timeouts, and throttled traffic.

## API Gateway vs FastAPI
API Gateway manages the API edge: routes, supported authorization, throttling, stages, and gateway-level monitoring.
FastAPI handles application logic: Pydantic validation, domain rules, orchestration, calls to Bedrock, and application-specific response models.
They can complement each other rather than compete.

## Memory trick
**Gateway protects and routes; backend validates and thinks.**
Gateway: edge controls → route → integration.
Backend: validate → business logic → Bedrock → response.

## Day 9 completion checklist
- Explain API Gateway and where it fits in a GenAI architecture.
- Compare HTTP API, REST API, and WebSocket API at a high level.
- Explain authentication vs authorization, throttling, stages, integrations, CORS, and monitoring.
- Design an API for a FastAPI/Bedrock chat service.
- Explain how you would test and troubleshoot 401/403, 429, 5xx, and high latency.
