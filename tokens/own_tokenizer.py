def cut_string_to_tokens(s: str):
    return list(s)

def count_pairs(tokens):
    pairs_count = {}
    for i in range(len(tokens) - 1):
        pair = (tokens[i], tokens[i + 1])
        if pair in pairs_count:
            pairs_count[pair] += 1
        else:
            pairs_count[pair] = 1
    return pairs_count

def create_token_from_most_common_pair(pairs_count):
    if not pairs_count:
        return None
    return max(pairs_count, key=pairs_count.get)

def merge_tokens(most_common_pair, tokens):
    merged = []
    i = 0
    while i < len(tokens):
        if i < len(tokens) - 1 and (tokens[i], tokens[i+1]) == most_common_pair:
            merged.append(tokens[i] + tokens[i+1])
            i += 2
        else:
            merged.append(tokens[i])
            i += 1
    return merged

def run_bpe(text, num_merges=10):
    tokens = cut_string_to_tokens(text)
    merges = []
    for _ in range(num_merges):
        pairs = count_pairs(tokens)
        if not pairs:
            break
        most_common = create_token_from_most_common_pair(pairs)
        merges.append(most_common)
        tokens = merge_tokens(most_common, tokens)
        print(f"Merged {most_common} -> tokens: {tokens}")
    return tokens, merges

# test
text = "abbbababababbabababababbababbaaaabbbbaaaaaaaaaaaaabbabababbababbbabababa"
tokens, merges = run_bpe(text, num_merges=15)

print("\nFinal tokens:", tokens)
print("Merge history:", merges)
