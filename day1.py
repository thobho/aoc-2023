from utils import read_data 

tokens = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def process_token_start(text: str):
    for token_key, token_value in tokens.items():
        if text.startswith(token_key):
            return (text[len(token_key):], token_value)        
    return (text[1:], None)

def process_token_end(text: str):
    for token_key, token_value in tokens.items():
        if text.endswith(token_key):
            return (text[0:-len(token_key)], token_value)
    return (text[0:-1], None)

def process_line_forward(text: str):
    currently_processing = text
    while len(currently_processing) > 0:
        (substring, number) = process_token_start(currently_processing)
        currently_processing = substring
        if number is not None:
            return number
    return None
        
def process_line_backward(text: str):
    currently_processing = text
    while len(currently_processing) > 0:
        (substring, number) = process_token_end(currently_processing)
        currently_processing = substring
        if number is not None:
            return number
    return None
    
test_data = read_data('day1.txt')

def solution():
    result = 0
    for line in test_data.split("\n"):
        start_n = process_line_forward(line)
        end_n = process_line_backward(line)
        partial = start_n * 10 + end_n
        print(partial, '     ', line)
        result = result + partial
    return result


print(solution())