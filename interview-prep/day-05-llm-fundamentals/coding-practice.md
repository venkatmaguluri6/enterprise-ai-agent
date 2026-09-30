# Day 5 — Daily Reading + Coding Practice

This file is self-contained for daily study: theory, examples, interview essentials, quick revision and coding.

## 1. Today's target

Explain how a prompt becomes an LLM response, then implement a small mock pipeline to see the stages. The mock is educational and is not a real neural network.

## 2. Read this pipeline

```text
Prompt
 ↓
Tokenization
 ↓
Token IDs
 ↓
Token embeddings + positional information
 ↓
Transformer (attention + feed-forward layers)
 ↓
Next-token scores/probabilities
 ↓
Decoding selects a token
 ↓
Append token and repeat
 ↓
Response
```

## 3. Core concepts in plain English

### LLM
A neural network trained to learn patterns from data and generate language. Many chat LLMs predict a next token based on context.

### Token and token ID
A token is a tokenizer-defined text unit: word, subword, punctuation, etc. A token ID is its integer vocabulary index. The exact tokens and IDs depend on the tokenizer.

### Embeddings
A vector is a list of numbers. Token embeddings are model input representations; document embeddings are commonly used for semantic retrieval in RAG.

### Transformer and attention
Attention lets each token representation incorporate information from other relevant tokens. Q is compared against K to calculate weights, and those weights combine V. Positional information helps represent order.

### Autoregressive generation
Predict a next token → append it → predict again → stop when a stopping condition is reached.

### Context window
The supported token budget for a request. System prompts, history, retrieved chunks, tool outputs and generated tokens may consume that budget.

### Temperature and top-p
Temperature changes the sharpness of the sampling distribution. Top-p restricts sampling to a high-probability candidate pool. Neither guarantees factual accuracy.

### RAG and hallucinations
RAG retrieves external chunks and provides them to the LLM as context. It can improve grounding but cannot guarantee zero hallucinations.

## 4. Tiny examples

Text → tokens:
```python
import re

text = "What is RAG?"
tokens = re.findall(r"\w+|[^\w\s]", text.lower())
print(tokens)  # ['what', 'is', 'rag', '?']
```

Remember: this regex is only a toy tokenizer. Production tokenizers can split text differently.

Conceptual token ID lookup:
```python
vocabulary = {"what": 1, "is": 2, "rag": 3, "?": 4}
ids = [vocabulary.get(token, 0) for token in tokens]
```

Here, 0 is our made-up unknown-token ID. Real tokenizer vocabularies and reserved IDs are model-specific.

## 5. Project implementation

File: `app/services/llm_demo.py`

The demo contains:
- `tokenize(text)`
- `token_to_id(tokens)`
- `generate_next_token(tokens)`
- `generate_response(prompt, max_tokens)`

The generation function uses rules, not learned weights. It demonstrates the *shape* of a generation loop only.

Run the demo:

```bash
python -c "from app.services.llm_demo import tokenize, token_to_id, generate_response; print(tokenize('What is RAG?')); print(token_to_id(tokenize('What is RAG?'))); print(generate_response('What is RAG?', 5))"
```

Run tests:

```bash
pytest
```

## 6. Coding tasks

### Task A — inspect tokenization
Try:
- `"Hello, world!"`
- `"RAG combines retrieval with generation."`
- `"AI Engineer 2026"`

Explain why this regex tokenizer is not the same as a real model tokenizer.

### Task B — inspect token IDs
Try a known token and an unknown token. Explain why different tokenizers can assign different IDs to the same text.

### Task C — change the generation loop
1. Call `generate_response("What is RAG?", max_tokens=1)`.
2. Try `max_tokens=3`.
3. Try `max_tokens=0`.
4. Try a negative value and explain the error.

### Task D — explain a real LLM versus the mock
The mock uses if-statements and a tiny vocabulary. A real LLM uses learned parameters and model inference to produce next-token scores. Be clear about this difference in interviews.

## 7. Most important interview questions

1. What is an LLM?
2. Token vs token ID?
3. Token embedding vs document embedding?
4. What is self-attention?
5. Explain Q, K and V.
6. Why does a Transformer need positional information?
7. What is autoregressive generation?
8. What is the context window?
9. Temperature vs top-p?
10. Does RAG eliminate hallucinations?

Use the answers in `interview-questions.md` to practise out loud.

## 8. Interview memory hacks

```text
Text → tokens → IDs → vectors → Transformer → next token → repeat
Q asks | K matches | V supplies
Training = learn | Inference = use
Temperature = distribution sharpness
Top-p = cumulative-probability candidate pool
RAG = retrieve evidence + generate
```

## 9. 30-second interview answer

> The input is tokenized and mapped to token IDs, then converted into vector representations with positional information. Transformer layers use self-attention and feed-forward networks to build contextual representations. The model produces next-token scores, and decoding selects a token that is appended to the context. This repeats until generation stops. In RAG, retrieved chunks provide external context, but RAG cannot guarantee zero hallucinations.

## 10. Today's 20-minute coding routine

- 5 min: run the demo and inspect tokens/IDs.
- 5 min: vary `max_tokens` and inspect generation.
- 5 min: explain why the demo is not a real LLM.
- 5 min: answer tokenization, embeddings, attention and context-window questions without notes.
