# Day 8 — Amazon Bedrock Fundamentals

## Goal
Understand the managed AWS foundation-model workflow, explain it in interviews, and build a small Python integration that can be tested without making a real AWS call.

## 80/20 concepts

### What is Amazon Bedrock?
Amazon Bedrock is a managed AWS service for using supported foundation models through APIs. Your application sends input to a model and receives generated output without operating the model-serving infrastructure itself.

### Key vocabulary
- **Foundation model (FM):** a broadly trained model that can perform tasks such as generation, summarization, and question answering.
- **Inference:** running a model on an input to produce an output.
- **Bedrock Runtime:** the API surface used for model inference.
- **Model ID:** identifies the model or inference target.
- **boto3:** AWS SDK for Python.
- **IAM:** defines which AWS actions an identity can perform.
- **Converse API:** a common message-based interface supported by many Bedrock models.
- **Inference configuration:** controls such as maximum output tokens and temperature, where supported.

### Typical request flow
1. User sends a request to your FastAPI application.
2. Application validates input and constructs a prompt/messages.
3. boto3 calls the Bedrock Runtime API using configured AWS credentials.
4. IAM evaluates permissions and the service checks model/region availability and access.
5. The selected model generates a response.
6. Application extracts the response, handles errors, logs safe metadata, and returns output.

### Converse API example
```python
import boto3

client = boto3.client("bedrock-runtime", region_name="YOUR_AWS_REGION")
response = client.converse(
    modelId="YOUR_SUPPORTED_MODEL_ID",
    messages=[
        {"role": "user", "content": [{"text": "Explain RAG simply."}]}
    ],
    inferenceConfig={"maxTokens": 200, "temperature": 0.2},
)
answer = response["output"]["message"]["content"][0]["text"]
print(answer)
```

This is a template. Replace the region and model ID with values available to your AWS account. The chosen model must support Converse, and your account needs the required access and IAM permissions.

### Credentials and safety
- Never hardcode access keys in source code or commit them to Git.
- Locally, use an AWS profile configured with the AWS CLI or another supported credential provider.
- In AWS, prefer an appropriate IAM role for the workload.
- Grant least-privilege permissions, including only the required Bedrock actions and resources where supported.
- Do not log secrets, sensitive prompts, or personal data unnecessarily.
- Set sensible timeouts/retries, validate inputs, handle throttling and service errors, and monitor latency/cost.
- Keep model ID and region configurable rather than embedding them throughout the application.

### Important interview distinctions
- **Bedrock vs SageMaker:** Bedrock is a managed way to consume supported foundation models; SageMaker provides broader tools to build, train, customize, and deploy ML models. The right choice depends on the use case.
- **Prompt vs model:** the prompt is the input/instructions; the model is what performs inference.
- **Temperature:** influences output variability; low temperature does not guarantee factual correctness.
- **RAG vs direct inference:** direct inference sends the prompt to a model; RAG retrieves relevant external context and includes it in the model request.
- **IAM vs model access:** correct IAM permissions alone may not satisfy every model's availability/access requirements. Verify the current model, region, and account setup.

## Local setup checklist
1. Create/activate a Python virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Configure credentials through a supported AWS credential provider; never put credentials in code.
4. Verify identity with `aws sts get-caller-identity` if the AWS CLI is installed.
5. Confirm the selected model is available to your account in the selected region and supports Converse.
6. Run unit tests first. They use a fake client and should not incur AWS charges.
7. Make a real invocation only after checking model availability, permissions, and pricing.

## Memory trick
**App → boto3 → Bedrock Runtime → model → response.**
- boto3 authenticates using the configured AWS credential chain.
- IAM authorizes the requested action.
- The model generates the output.
- Your app still owns validation, error handling, security, and response shaping.

## Day 8 acceptance criteria
- Explain Bedrock, inference, boto3, IAM, and Converse.
- Explain the request flow without mixing up authentication and authorization.
- Implement a small service with an injectable client.
- Unit-test request construction and response parsing without AWS credentials.
