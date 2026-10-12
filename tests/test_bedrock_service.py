import pytest

from app.services.bedrock_service import generate_text


class FakeBedrockClient:
    def __init__(self):
        self.kwargs = None

    def converse(self, **kwargs):
        self.kwargs = kwargs
        return {
            "output": {
                "message": {
                    "content": [{"text": "Amazon Bedrock is a managed service."}]
                }
            }
        }


def test_generate_text_calls_converse_and_extracts_answer():
    client = FakeBedrockClient()

    answer = generate_text(
        prompt=" Explain Bedrock. ",
        model_id="example-model",
        region_name="us-east-1",
        max_tokens=120,
        temperature=0.1,
        client=client,
    )

    assert answer == "Amazon Bedrock is a managed service."
    assert client.kwargs["modelId"] == "example-model"
    assert client.kwargs["messages"][0]["content"][0]["text"] == "Explain Bedrock."
    assert client.kwargs["inferenceConfig"] == {
        "maxTokens": 120,
        "temperature": 0.1,
    }


@pytest.mark.parametrize("prompt", ["", "   "])
def test_empty_prompt_is_rejected(prompt):
    with pytest.raises(ValueError, match="prompt"):
        generate_text(prompt, "example-model", "us-east-1", client=FakeBedrockClient())


def test_invalid_max_tokens_is_rejected():
    with pytest.raises(ValueError, match="max_tokens"):
        generate_text("hello", "example-model", "us-east-1", max_tokens=0, client=FakeBedrockClient())


def test_unexpected_response_shape_is_reported():
    class BrokenClient:
        def converse(self, **kwargs):
            return {}

    with pytest.raises(RuntimeError, match="unexpected response shape"):
        generate_text("hello", "example-model", "us-east-1", client=BrokenClient())
