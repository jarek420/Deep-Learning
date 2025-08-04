import tiktoken

enc = tiktoken.get_encoding("o200k_base")
coded = enc.encode("Hello, world!")
decoded = enc.decode(coded)

print(f"Encoded: {coded}")
print(f"Decoded: {decoded}")