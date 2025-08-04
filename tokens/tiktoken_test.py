import tiktoken

test_strings = [
    "nation",
    "national",
    "nationality",
    "nationalism",
    "nationalist",
    "nationalistic",
    "nationalistically",
    "nationals",
    "nation-state",
    "nation-states",
    "nacjonalista",
    "nacjonalistyczny",
    "nacjonalistycznie",
    "nacjonalistyczni",
    "nacjonalistycznych",
    "nacjonalistyczne",
]

enc = tiktoken.get_encoding("o200k_base")
coded_arr = []
for string in test_strings:
    
    coded = enc.encode(string)
    decoded = enc.decode(coded)
    coded_arr.append((string, coded, decoded))
    print(f"Original: {string}, Encoded: {coded}, Decoded: {decoded}")

    