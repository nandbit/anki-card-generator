def chunk_list(data: list[str], size: int):
    for i in range(0, len(data), size):
        yield data[i:i + size]
