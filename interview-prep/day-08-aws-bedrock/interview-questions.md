# Day 8 — Amazon Bedrock Interview Questions

Try to answer each question aloud in 30–60 seconds before reading the answer.

## 1. What is Amazon Bedrock?
Amazon Bedrock is a managed AWS service that lets applications invoke supported foundation models through APIs. It removes the need to manage the underlying model-serving infrastructure, while the application remains responsible for prompts, validation, permissions, error handling, and business logic.

## 2. What is inference?
Inference is the process of passing input to a trained model and obtaining a prediction or generated output.

## 3. What is boto3?
boto3 is the AWS SDK for Python. It lets Python applications interact with AWS services, including Bedrock Runtime.

## 4. What is the Bedrock Runtime API used for?
It provides operations for sending input to supported foundation models and receiving generated results. The Converse API is a common message-oriented option for models that support it.

## 5. What is the Converse API?
It offers a consistent messages-based request shape across many supported models. Model support and available request features still need to be checked for the chosen model.

## 6. What is the role of IAM?
IAM authenticates identities through AWS's credential mechanisms and authorizes actions using policies. In practice, the workload needs permission for the Bedrock actions and resources it uses.

## 7. If IAM permissions are correct, will every model call work?
Not necessarily. The model must also be available in the chosen region, support the requested API, and satisfy any account/model access requirements. Request parameters, quotas, and service availability can also cause failures.

## 8. How should you manage AWS credentials in a Python application?
Use the supported AWS credential chain, such as a local AWS profile for development or an IAM role for an AWS-hosted workload. Avoid hardcoding or committing keys. Use least-privilege policies and rotate/revoke exposed credentials.

## 9. What are max tokens and temperature?
Maximum output tokens limits the generated output length. Temperature influences variability in token selection. Exact behavior depends on model support; neither setting guarantees factual correctness.

## 10. How would you handle a Bedrock throttling error?
Use bounded retries with exponential backoff and jitter where appropriate, respect service guidance, limit concurrency, monitor throttling, and consider quotas or capacity options. Avoid infinite retries and return a clear application-level error if retries are exhausted.

## 11. How would you reduce latency and cost?
Use an appropriate model for the task, limit prompt and output tokens, avoid unnecessary repeated calls, set timeouts, measure end-to-end latency, cache only when safe and appropriate, and monitor usage. Evaluate quality before switching to a smaller/cheaper model.

## 12. What is the difference between direct inference and RAG?
Direct inference sends the user's prompt to a model. RAG first retrieves relevant external content and includes it in the prompt/context so the model can answer using that information. RAG can improve grounding but does not guarantee correctness.

## 13. How would you test a Bedrock integration without spending money?
Inject a fake client into the service and assert the request shape and response parsing. Keep unit tests independent of credentials/network. Use a separately controlled integration test for a real invocation.

## 14. How would you integrate Bedrock into FastAPI?
Put the model call in a service layer, inject/configure the client, validate requests with Pydantic, keep blocking SDK calls off the event loop (for example, use a thread pool or `asyncio.to_thread` in an async endpoint), apply timeouts/retries, and return a controlled response. Avoid creating a new client for every request if client lifecycle and deployment architecture permit safe reuse.

## 15. Bedrock vs SageMaker?
Bedrock is designed for consuming supported foundation models through managed APIs. SageMaker offers tools across the ML lifecycle, including building, training, customizing, and deploying models. The decision depends on control, customization, supported models, operations, and cost.

## Short answer template
“Amazon Bedrock lets my Python application use supported foundation models through managed APIs. I use boto3 and the Bedrock Runtime client, choose a model available in my region, authorize the call with least-privilege IAM permissions, and invoke it using an API such as Converse if the model supports it. In production I add validation, timeouts, bounded retries, safe logging, and cost/latency monitoring. I unit-test the service with a fake client so tests don't depend on AWS.”
