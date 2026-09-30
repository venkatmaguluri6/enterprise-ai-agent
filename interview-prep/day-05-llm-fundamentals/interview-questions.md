# Day 5 — Important LLM Interview Questions and Answers

Focus on understanding these high-value questions first rather than memorizing every possible detail.

## 1. What is an LLM?

**Answer:** A large language model is a neural network trained on large amounts of data to learn language patterns and generate outputs. Many chat LLMs generate text autoregressively by predicting the next token from the current context.

**Memory:** learned patterns + context → generated continuation.

## 2. What is a token? Is it always a word?

**Answer:** No. A token may be a word, subword, punctuation mark or another unit defined by the tokenizer. Tokenization varies by model/tokenizer.

**Trap:** Do not assume one token equals one word.

## 3. What is the difference between tokenization and token IDs?

**Answer:** Tokenization splits text into tokens. Each token is then mapped to an integer ID from that tokenizer's vocabulary.

```text
Text → tokens → integer IDs
```

## 4. What is an embedding?

**Answer:** An embedding is a vector representation of information. Token embeddings are used within the LLM, while sentence/document embeddings are commonly used for semantic search and RAG retrieval.

**Trap:** These are related concepts but not interchangeable uses.

## 5. Explain the Transformer architecture.

**Answer:** A Transformer processes token representations through layers that commonly include attention and feed-forward networks. Attention lets token representations incorporate context from other tokens. Positional information helps the model represent token order.

## 6. What is self-attention?

**Answer:** Self-attention computes how token representations should combine information from other tokens in the same sequence. It helps the model represent contextual relationships.

**Memory:** each token can look at relevant tokens in its context.

## 7. Explain Query, Key and Value.

**Answer:** Query is compared with Keys to calculate attention scores. Those scores are normalized into weights, which are used to combine Values.

**Memory:** Q asks, K matches, V supplies.

## 8. Why scale QKᵀ by √dₖ?

**Answer:** Scaling keeps dot-product scores at a manageable magnitude as the key dimension grows, helping avoid overly extreme softmax values and supporting stable gradients.

## 9. Why is multi-head attention used?

**Answer:** It performs attention through multiple learned heads and combines their outputs, allowing the model to capture different relationships or representation patterns.

**Trap:** Don't claim each head always has one fixed interpretable purpose.

## 10. Why does a Transformer need positional information?

**Answer:** Attention by itself does not inherently encode token order. Positional information helps distinguish sequences where the same tokens appear in different orders.

## 11. What is autoregressive generation?

**Answer:** The model predicts a next token based on the context, appends the selected token, and repeats until a stopping condition is reached.

## 12. What is the context window?

**Answer:** It is the amount of tokenized context the model supports for a request. The exact limit and how output tokens count toward it depend on the model/API.

**Production follow-up:** system instructions, chat history, retrieved chunks and tool results can all consume tokens.

## 13. Temperature vs top-p?

**Answer:** Temperature adjusts the sharpness of the probability distribution used during sampling. Top-p restricts sampling to a high-probability candidate set whose cumulative probability reaches a threshold.

**Trap:** Neither guarantees correctness or makes the model more intelligent.

## 14. What is the difference between training and inference?

**Answer:** Training uses data and optimization to learn model parameters. Inference runs the trained model to generate a prediction or response for an input.

## 15. Does a larger model always perform better?

**Answer:** No. Model size is one factor. Performance also depends on data, architecture, training methods, alignment, the task, tools and deployment constraints.

## 16. What is a hallucination?

**Answer:** A hallucination is incorrect, fabricated or unsupported output presented as if it were reliable. LLM generation does not inherently guarantee factual truth.

## 17. Does RAG eliminate hallucinations?

**Answer:** No. RAG can provide relevant external evidence and improve grounding, but retrieval can fail, sources can be inaccurate, and the model can misinterpret or ignore the evidence.

## 18. How does an LLM relate to a RAG system?

**Answer:** The retriever finds relevant chunks, the application adds them to the prompt, and the LLM generates an answer conditioned on the question and supplied context.

## 19. Why do tokens matter for cost and latency?

**Answer:** Model APIs often meter input and output tokens. Larger prompts and outputs can increase cost and processing time, so retrieval, prompt design and output limits should be measured and tuned.

## 20. What happens between receiving a prompt and returning a response?

**Answer:** The application prepares the messages, the tokenizer maps text to token IDs, the model processes the representation through Transformer layers, and decoding selects output tokens autoregressively. The serving system returns the generated text and may also report usage metadata.

## 21. What is the difference between token embeddings and document embeddings?

**Answer:** Token embeddings are learned input representations used by the language model. Document embeddings represent larger text units as vectors for semantic comparison and retrieval, often using an embedding model.

## 22. How would you reduce context usage in a RAG application?

**Answer:** Retrieve fewer but more relevant chunks, deduplicate results, use suitable chunk sizes, remove irrelevant conversation history, keep instructions concise and set appropriate output limits. Evaluate answer quality so reducing tokens does not remove needed evidence.

## 23. Is async related to LLM intelligence?

**Answer:** No. Async affects how the application handles waiting and concurrent I/O. It does not change the model's learned intelligence or the correctness of its output.

## 24. How would you explain LLMs to a non-ML backend interviewer?

**Answer:** The application sends structured messages to a trained model. The model processes token representations and generates a response piece by piece. Our backend controls the prompt, retrieved context, tools, safety checks, limits, logging and response format.

## 25. Give a 30-second explanation of LLM generation.

**Answer:** The input is tokenized and converted into vector representations with positional information. Transformer layers use self-attention and feed-forward networks to build contextual representations. The model predicts scores for the next token; decoding selects a token, appends it to the context, and repeats until generation ends. In RAG, retrieved documents can provide grounding, but they do not guarantee zero hallucinations.

## Interview traps to remember

- A token is not necessarily a word.
- Token IDs are tokenizer-specific.
- Token embeddings and document embeddings serve different roles.
- Attention helps contextualize representations; it is not a database lookup.
- Transformers need positional information.
- Temperature/top-p influence sampling, not factual truth.
- RAG reduces some grounding problems but does not guarantee correctness.
- More parameters do not automatically mean better results.
- Async improves application I/O concurrency, not LLM intelligence.

## 5 questions to memorize first

1. Explain LLM generation end to end.
2. Token vs token ID vs embedding.
3. Explain self-attention and Q/K/V.
4. Context window and why it matters in RAG.
5. Temperature vs top-p; why neither guarantees truth.
