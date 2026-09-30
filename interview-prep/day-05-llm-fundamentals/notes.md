# Day 5 — LLM Fundamentals and Transformer Architecture

## Goal

Explain how text goes from a user's prompt to an LLM response, and connect the core terms to RAG and our Enterprise AI Agent project.

## The whole story in one picture

```text
Prompt
  ↓
Tokenizer
  ↓
Tokens → Token IDs
  ↓
Token embeddings + positional information
  ↓
Transformer blocks (attention + feed-forward layers)
  ↓
Scores / probabilities for the next token
  ↓
Decoding strategy selects a token
  ↓
Append token and repeat
  ↓
Generated response
```

This is a simplified view of a decoder-only autoregressive LLM. Architectures and implementations vary.

## 1. What is an LLM?

A large language model is a neural network trained on large amounts of data to learn patterns and generate language. Many chat LLMs generate text by predicting one next token at a time from the context.

**Interview line:** An LLM uses learned parameters and the supplied context to generate a likely continuation, commonly through next-token prediction.

Do not say every LLM searches the internet. A model may answer from learned patterns and provided context; browsing is a separate tool/capability.

## 2. Tokens and tokenization

A token is a unit selected by a tokenizer. It may be a word, part of a word, punctuation, or another text unit. The exact split depends on the tokenizer.

```text
"What is RAG?"
      ↓ tokenizer
["What", " is", " R", "AG", "?"]  # illustrative only
      ↓ vocabulary lookup
[ID, ID, ID, ID, ID]
```

Token IDs are vocabulary-specific integers. Do not memorize example IDs; the same text can have different tokenization/IDs across models.

**Why it matters in production:** prompts, retrieved chunks, conversation history and generated output all consume tokens. Token counts affect context limits, latency and cost.

## 3. Embeddings: two meanings to distinguish

An embedding is a vector representation.

- **Token embeddings:** turn token IDs into vectors inside the model.
- **Text/document embeddings:** represent a sentence or document as a vector for tasks such as semantic search in a RAG system.

```text
Token IDs → token embedding layer → Transformer

Document → embedding model → document vector → vector index
```

**Interview line:** Token embeddings are part of the language model's input representation; document embeddings are commonly generated separately for semantic retrieval.

## 4. Transformer and self-attention

A Transformer uses attention to let token representations incorporate information from other tokens. This helps model context and relationships.

Example: in "The animal was tired, so it slept", context helps relate "it" to "the animal".

A simplified Transformer block includes:
1. Self-attention
2. Residual connection and normalization
3. Feed-forward network
4. Another residual connection and normalization

Real implementations have architecture-specific details.

## 5. Query, Key and Value (Q, K, V)

Think of attention like matching a question against available information:

- **Q — Query:** what this token is looking for.
- **K — Key:** what each token can be matched against.
- **V — Value:** the information to combine using the attention weights.

Scaled dot-product attention is commonly written as:

`Attention(Q, K, V) = softmax(QKᵀ / √dₖ)V`

At interview level, explain the flow: compare Q with K → calculate scores → softmax to get weights → weighted combination of V.

The scale factor helps keep dot-product scores at a manageable magnitude and supports stable softmax gradients.

## 6. Multi-head attention

Instead of one attention calculation, multi-head attention uses multiple heads whose outputs are combined. Heads can learn different patterns, but do not claim each head always has one fixed, human-readable role.

## 7. Positional information

Attention alone does not inherently tell the model the order of tokens. Transformers therefore use positional information. Methods differ; examples include sinusoidal positional encodings and RoPE (Rotary Positional Embeddings).

Order matters:
- "Dog bites man"
- "Man bites dog"

## 8. Decoder-only models and autoregressive generation

GPT-style models are generally decoder-only Transformers. A causal mask prevents a token from attending to future tokens during next-token training/generation.

Autoregressive generation:
1. Process the prompt.
2. Produce scores/probabilities for the next token.
3. Choose a token using a decoding strategy.
4. Append it to the context.
5. Repeat until a stop condition or output limit.

The next token is not always selected by simply taking the highest-probability option; decoding settings can allow sampling.

## 9. Context window

A model's context window is its supported token budget for the input context and, depending on the model/API, generated output. Always check the specific model's limits.

Context can include system instructions, user messages, conversation history, retrieved document chunks and tool results. Large context can increase cost and latency; more context is not automatically more useful.

**RAG connection:** retrieve and rank relevant chunks rather than blindly stuffing every document into the prompt.

## 10. Temperature and top-p

- **Temperature:** adjusts the sharpness of the token probability distribution during sampling. Lower values tend to make choices more predictable; higher values tend to make them more varied.
- **Top-p (nucleus sampling):** samples from a set of high-probability tokens whose cumulative probability reaches the configured threshold.

Memory trick: **temperature = randomness tendency; top-p = candidate probability pool.**

Neither setting makes a model more intelligent or guarantees factual accuracy. Their exact effects depend on implementation and other decoding settings.

## 11. Training vs inference vs parameters

- **Training:** adjusts model parameters using data and an optimization procedure.
- **Inference:** runs a trained model to produce outputs for new inputs.
- **Parameters/weights:** learned numerical values used by the network.

A larger parameter count does not automatically make a model best for every task. Data quality, architecture, training, alignment, tools, latency and cost all matter.

## 12. Hallucinations and RAG

A hallucination is an output that is false, fabricated or unsupported but presented as if it were correct.

RAG retrieves external information and supplies relevant context to the LLM. It can improve grounding, but it does **not** guarantee zero hallucinations. Retrieval can fail, documents can be wrong, and the model can misinterpret evidence.

```text
Question → retrieve relevant chunks → build grounded prompt → LLM → answer
```

## 13. Token budget, latency and cost

Practical levers include:
- Keep system prompts clear and concise.
- Retrieve only relevant chunks.
- Limit unnecessary conversation history.
- Set a suitable output-token limit.
- Choose a model that fits the task and latency/cost requirements.
- Measure actual usage and response quality.

Do not assume latency is only model generation time: network, queueing, retrieval and prompt size can also matter.

## 14. Day 5 mock implementation

The project adds `app/services/llm_demo.py`. It uses a tiny vocabulary and simple rules to demonstrate the pipeline. It is **not a real LLM**, has no learned weights and does not perform Transformer inference.

Run:

```bash
python -c "from app.services.llm_demo import tokenize, token_to_id, generate_response; print(tokenize('What is RAG?')); print(token_to_id(tokenize('What is RAG?'))); print(generate_response('What is RAG?', 5))"
pytest
```

## Quick revision cheat sheet

```text
Text → tokens → token IDs → token embeddings
     → Transformer / attention
     → next-token scores → decoding → repeat

Token embedding  → representation inside LLM
Document embedding → vector for semantic retrieval
Q → Query         K → Key             V → Value
Training → learn  Inference → use
Context window → supported token budget
Temperature → sampling distribution sharpness
Top-p → cumulative-probability candidate set
RAG → retrieve evidence and pass it to the LLM
Hallucination → plausible-sounding but unsupported/incorrect output
```

## 30-second interview answer

> The input is tokenized and mapped to token IDs, which are converted into vector representations with positional information. Transformer layers use self-attention and feed-forward networks to build contextual representations. An autoregressive model then produces scores for the next token; a decoding strategy selects one, appends it to the context, and repeats. Context limits and decoding settings affect how generation behaves. In a RAG application, retrieved documents can ground the prompt, although RAG does not eliminate hallucinations.

## Before Day 6

Be ready to explain:
1. Token vs token ID vs embedding.
2. Token embedding vs document embedding.
3. Self-attention and Q/K/V.
4. Why positional information is needed.
5. Autoregressive generation.
6. Context window and token budget.
7. Temperature vs top-p.
8. Training vs inference.
9. Why RAG cannot guarantee zero hallucinations.
