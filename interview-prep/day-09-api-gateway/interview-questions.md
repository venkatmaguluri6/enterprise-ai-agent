# Day 9 — API Gateway Interview Questions

Answer aloud first. Aim for a concise 30–60 second response.

## 1. What is Amazon API Gateway?
It is a managed AWS service to create, publish, secure, route, monitor, and manage APIs. It acts as an entry point between clients and backend integrations such as Lambda or HTTP services.

## 2. How does API Gateway fit into a GenAI application?
The client calls an API endpoint, API Gateway applies configured edge controls and routes the request to a backend. The backend validates the prompt, applies business rules, calls Bedrock or another model provider, and returns a response.

## 3. What is the difference between API Gateway and FastAPI?
API Gateway manages the API edge, supported authorization, throttling, stages, and gateway-level monitoring. FastAPI implements application logic, request/response models, validation, orchestration, and model calls. They can be used together.

## 4. HTTP API vs REST API?
HTTP APIs are generally suited to common, low-latency API proxying and standard authorization needs. REST APIs offer additional API management capabilities. Compare the exact feature requirements, integrations, latency, and pricing before choosing.

## 5. What is a WebSocket API?
It supports persistent, two-way communication over a WebSocket connection, useful for applications that need server/client messages over time. It is different from a normal request/response HTTP API.

## 6. What is an API integration?
It defines how a matched route forwards a request to a backend, such as Lambda or an HTTP endpoint. The integration type and configuration determine request/response handling.

## 7. Authentication vs authorization?
Authentication establishes who the caller is. Authorization determines what the caller may do. Gateway authorizers can enforce supported policies, while business-level permissions may still need enforcement in the backend.

## 8. How would you secure a chat endpoint?
Use HTTPS, an appropriate authorizer, least-privilege IAM for backend access, request validation, throttling, safe secret management, and monitoring. Enforce user-specific business permissions in the backend and avoid logging sensitive prompts or credentials.

## 9. What is throttling and why is it important?
Throttling limits request rates and bursts to help protect services and control usage. It can reduce overload but is not a complete abuse-prevention system; sensitive workloads may also need per-user quotas and application-level controls.

## 10. What is CORS?
CORS is a browser-enforced mechanism governing cross-origin requests. Configure allowed origins, methods, and headers deliberately. CORS is not an authentication mechanism and does not protect an API from non-browser clients.

## 11. What are stages?
Stages represent named environments or published deployments, often such as dev, test, and prod. Deployment and stage behavior varies between API types, so describe it for the specific API configuration.

## 12. A client gets HTTP 429. What do you investigate?
Check gateway throttling, usage quotas, backend throttling, and service quotas. Inspect metrics/logs, reduce unnecessary concurrency, and use bounded retries with backoff and jitter when safe. Do not retry indefinitely.

## 13. Requests return 403. What would you check?
Check the configured authorizer or IAM policy, resource/method permissions, identity/token validity, resource policy, and any network or integration permissions relevant to the architecture. Distinguish an authorization rejection from a backend application error.

## 14. The gateway returns 5xx. How do you debug?
Inspect gateway execution/access logs and metrics, then check integration configuration, backend health, permissions, timeouts, and backend logs. Correlate a request ID across layers while avoiding sensitive log content.

## 15. How would you handle long-running LLM responses?
Check gateway integration timeout limits and the selected API/integration's streaming support. For long-running jobs, consider asynchronous processing: return a job ID, process in the background, and let the client poll or receive an event. For token streaming, verify end-to-end support across gateway, integration, backend, and client rather than assuming it works automatically.

## 16. Why validate in FastAPI if API Gateway can validate?
Gateway validation can reject malformed requests early where supported, but backend validation remains important because services may have other callers and business rules require application context. Defense in depth is safer.

## 17. How do you control GenAI cost?
Apply caller authentication, quotas/throttling, prompt and output token limits in the backend, request-size limits, sensible timeouts, usage monitoring, and rate limits appropriate to each user or tenant. Gateway throttling alone cannot control model tokens per request.

## 18. How would you deploy a FastAPI service behind API Gateway?
Select a supported integration pattern based on the hosting target. For a private containerized backend, evaluate API Gateway private integration with VPC Link and a load balancer where supported. Configure routes, authorization, network access, stages/domains, logs/metrics, and test the full path. Do not assume a public FastAPI URL is secure just because API Gateway exists.

## Sample interview answer
“I use Amazon API Gateway as the managed entry point for clients. It routes requests to a backend and can enforce supported authorization, throttling, and API-level monitoring. For a GenAI chat service, the FastAPI backend validates the request, applies business rules, invokes Bedrock, and returns a controlled response. I would configure least-privilege permissions, safe logging, timeouts, and monitoring, and test 401/403, 429, 5xx, and latency scenarios.”
