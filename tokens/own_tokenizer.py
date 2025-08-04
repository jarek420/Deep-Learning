import string

test= "abbbababababbabababababbababbaaaabbbbaaaaaaaaaaaaabbabababbababbbabababa"

# 1. def function that will cut string into array of chars "bakars" -> 'b', 'a', 'k', 'a', 'r', 's'
def cut_string_to_chars(s: str):
    char_array = []
    for char in s:
        char_array.append(char)
    return char_array

# 2. def function that will count all pairs of chars in array
def count_pairs(char_array):
    pairs_count = {}
    for i in range(len(char_array) - 1):
        pair = (char_array[i], char_array[i + 1])
        if pair in pairs_count:
            pairs_count[pair] += 1
        else:
            pairs_count[pair] = 1
    return pairs_count

print(count_pairs(cut_string_to_chars(test)))

# 3. def function that will create token from most common pair of chars
def create_token_from_most_common_pair(pairs_count):
    most_common_pair = max(pairs_count, key=pairs_count.get)
    token = ''.join(most_common_pair)
    return token

def merge_tokens(token, char_array):
    tmp_array = []
    for i in range(len(char_array) - 1):
        if char_array[i] == token[0] and char_array[i + 1] == token[1]:
            tmp_array.append(token)
        else:
            tmp_array.append(char_array[i])
    return tmp_array

a = create_token_from_most_common_pair(count_pairs(cut_string_to_chars(test)))
char_new = merge_tokens(a, cut_string_to_chars(test))
print(merge_tokens(a, cut_string_to_chars(test)))
#NOTE:
# legth of the token will be changing, after chaging string into array of chars length of each elements is 1
# so we need to make all functions more dynamic
a = create_token_from_most_common_pair(count_pairs(cut_string_to_chars(char_new)))
char_new = merge_tokens(a, cut_string_to_chars(char_new))
print(merge_tokens(a, cut_string_to_chars(char_new)))
