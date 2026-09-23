import asyncio
import time


async def fetch_vector_search(query: str) -> list[str]:
    print(f"Vector search started for: {query}")
    await asyncio.sleep(2)
    print("Vector search completed.")
    return ["RAG combines retrieval with generation.", "Embeddings represent text as vectors."]


async def fetch_keyword_search(query: str) -> list[str]:
    print(f"Keyword search started for: {query}")
    await asyncio.sleep(1)
    print("Keyword search completed.")
    return ["BM25 is a lexical search algorithm.", "Hybrid search can combine keyword and vector search."]


async def fetch_metadata(query: str) -> dict[str, str]:
    print(f"Metadata search started for: {query}")
    await asyncio.sleep(1)
    print("Metadata search completed.")
    return {"query": query, "source": "enterprise-knowledge-base"}


async def sequential_search(query: str) -> dict:
    start_time = time.perf_counter()
    vector_results = await fetch_vector_search(query)
    keyword_results = await fetch_keyword_search(query)
    metadata = await fetch_metadata(query)
    return {
        "vector_results": vector_results,
        "keyword_results": keyword_results,
        "metadata": metadata,
        "execution_time": time.perf_counter() - start_time,
    }


async def concurrent_search(query: str) -> dict:
    start_time = time.perf_counter()
    vector_results, keyword_results, metadata = await asyncio.gather(
        fetch_vector_search(query),
        fetch_keyword_search(query),
        fetch_metadata(query),
    )
    return {
        "vector_results": vector_results,
        "keyword_results": keyword_results,
        "metadata": metadata,
        "execution_time": time.perf_counter() - start_time,
    }


async def main() -> None:
    query = "What is RAG?"

    print("\n========== SEQUENTIAL SEARCH ==========")
    sequential_result = await sequential_search(query)
    print(f"Sequential execution time: {sequential_result['execution_time']:.2f} seconds")

    print("\n========== CONCURRENT SEARCH ==========")
    concurrent_result = await concurrent_search(query)
    print(f"Concurrent execution time: {concurrent_result['execution_time']:.2f} seconds")

    print("\nExpected: sequential ≈ 4s, concurrent ≈ 2s")


if __name__ == "__main__":
    asyncio.run(main())
