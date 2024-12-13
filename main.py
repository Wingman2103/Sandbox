import random
import string
from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class Textr(BaseModel):
    paragraph_count: int
class Stringr(BaseModel):
    count:int
    length:int
class Numberr(BaseModel):
    size:int
    lower_bound:int
    upper_bound:int
class Floatr(BaseModel):
 size:int
 lower_bound:float
 upper_bound:float
class Booleanr(BaseModel):
    size:int
def generate_random_word(length):
    word=''
    for i in range(length):
        word += random.choice(string.ascii_lowercase)
    return word
def generate_random_sentence(word_count):
    sentence=''
    for i in range(word_count):
      word_length = random.randint(3, 10)
      sentence+= generate_random_word(word_length) +' '
    return sentence.strip() +'.'
def generate_random_paragraph(sentence_count):
    paragraph=''
    for i in range(sentence_count):
        sentence_length = random.randint(5, 15)
        paragraph+= generate_random_sentence(sentence_length) +' '
    return paragraph.strip()
def generate_text(paragraph_count):
    text=''
    for i in range(paragraph_count):
        sentence_count = random.randint(3, 7)
        text+= generate_random_paragraph(sentence_count) + '\n\n'
    a=text.strip()
    return a
@app.post("/generate_text/")
def api_generate_text(request: Textr):
    a=generate_text(request.paragraph_count)
    return {"text":a }
def generate_random_character_string(length):
    chars=''
    for i in range(length):
        chars += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return chars
@app.post("/generate_strings/")
def api_generate_strings(request: Stringr):
    strings = [generate_random_character_string(request.length) for _ in range(request.count)]
    a={"strings": strings}
    return a
def generate_random_number_list(size, lower_bound, upper_bound):
    numbers =[]
    for i in range(size):
        numbers.append(random.randint(lower_bound, upper_bound))
    return numbers
@app.post("/generate_numbers/")
def api_generate_numbers(request: Numberr):
    numbers = generate_random_number_list(request.size, request.lower_bound, request.upper_bound)
    return {"numbers":numbers}
def generate_random_float_list(size, lower_bound, upper_bound):
    floats= []
    for i in range(size):
        floats.append(random.uniform(lower_bound, upper_bound))
        a=floats
    return floats
@app.post("/generate_floats/")
def api_generate_floats(request: Floatr):
    floats = generate_random_float_list(request.size, request.lower_bound, request.upper_bound)
    a = {"floats": floats}
    return {"floats": floats}
def generate_random_boolean_list(size):
    booleans = []
    for i in range(size):
        booleans.append(random.choice([True, False]))
    return booleans
@app.post("/generate_booleans/")
def api_generate_booleans(request: Booleanr):
    booleans = generate_random_boolean_list(request.size)
    return {"booleans":booleans}
import random
import string
def generate_random_word(length):
    word = ''
    for i in range(length):
        word += random.choice(string.ascii_lowercase)
    return word
def generate_random_sentence(word_count):
    sentence = ''
    for i in range(word_count):
        word_length = random.randint(3, 10)
        sentence += generate_random_word(word_length)+ ' '
    return sentence.strip()+'.'
def generate_random_paragraph(sentence_count):
    paragraph = ''
    for i in range(sentence_count):
        sentence_length = random.randint(5, 15)
        paragraph+=generate_random_sentence(sentence_length) +' '
    return paragraph.strip()
def generate_text(paragraph_count):
    text=''
    for i in range(paragraph_count):
        sentence_count = random.randint(3, 7)
        text += generate_random_paragraph(sentence_count) + '\n\n'
    return text.strip()
def save_text_to_file(text, filename):
    with open(filename,'w') as file:
        file.write(text)
def load_text_from_file(filename):
    with open(filename,'r') as file:
        return file.read()
def main():
    print("Welcome to the Random Text Generator!")
    num_paragraphs=int(input("How many paragraphs do you want to generate? "))
    random_text=generate_text(num_paragraphs)
    print("\nGenerated Random Text:\n")
    print(random_text)
    save_option = input("Do you want to save this text to a file? (yes/no) ")
    if save_option.lower()=='yes':
        filename = input("Enter the filename (with .txt extension): ")
        save_text_to_file(random_text, filename)
        print(f"Text saved to {filename}")
def generate_random_character_string(length):
    chars=''
    for i in range(length):
        chars+=random.choice(string.ascii_letters+string.digits+string.punctuation)
    return chars
def generate_multiple_random_strings(count, length):
    strings=[]
    for i in range(count):
        strings.append(generate_random_character_string(length))
    return strings
def print_random_strings(strings):
    for s in strings:
        print(s)
def main_extended():
    print("Welcome to the Extended Random String Generator!")
    num_strings = int(input("How many random strings do you want to generate? "))
    length_of_strings = int(input("What should be the length of each string? "))
    random_strings = generate_multiple_random_strings(num_strings, length_of_strings)
    print("\nGenerated Random Strings:\n")
    print_random_strings(random_strings)
    save_option = input("Do you want to save these strings to a file? (yes/no) ")
    if save_option.lower() == 'yes':
        filename = input("Enter the filename (with .txt extension): ")
        save_text_to_file('\n'.join(random_strings), filename)
        print(f"Strings saved to {filename}")
def generate_random_number_list(size, lower_bound, upper_bound):
    numbers=[]
    for i in range(size):
        numbers.append(random.randint(lower_bound, upper_bound))
    return numbers
def calculate_average(numbers):
    total=0
    for num in numbers:
        total+=num
    ans=total / len(numbers) if numbers else 0
    return ans
def main_numbers():
    print("Welcome to the Random Number Generator!")
    size=int(input("How many random numbers do you want to generate? "))
    lower_bound=int(input("Enter the lower bound: "))
    upper_bound=int(input("Enter the upper bound: "))
    random_numbers = generate_random_number_list(size, lower_bound, upper_bound)
    print("\nGenerated Random Numbers:\n")
    print(random_numbers)
    average = calculate_average(random_numbers)
    print(f"Average of generated numbers: {average}")
    save_option = input("Do you want to save these numbers to a file? (yes/no) ")
    if save_option.lower()=='yes':
        filename = input("Enter the filename (with .txt extension): ")
        save_text_to_file('\n'.join(map(str, random_numbers)), filename)
        print(f"Numbers saved to {filename}")
def run_all():
    main()
    main_extended()
    main_numbers()
def generate_random_float_list(size, lower_bound, upper_bound):
    floats=[]
    for i in range(size):
        floats.append(random.uniform(lower_bound, upper_bound))
    return floats
def calculate_float_average(floats):
    total=0.0
    for f in floats:
        total+=f
    answer=total / len(floats) if floats else 0.0
    return answer
def main_float_numbers():
    print("Welcome to the Random Float Number Generator!")
    size = int(input("How many random float numbers do you want to generate? "))
    lower_bound = float(input("Enter the lower bound: "))
    upper_bound = float(input("Enter the upper bound: "))
    random_floats = generate_random_float_list(size, lower_bound, upper_bound)
    print("\nGenerated Random Float Numbers:\n")
    print(random_floats)
    average = calculate_float_average(random_floats)
    print(f"Average of generated float numbers: {average}")
    save_option = input("Do you want to save these floats to a file? (yes/no) ")
    if save_option.lower()=='yes':
        filename = input("Enter the filename (with .txt extension): ")
        save_text_to_file('\n'.join(map(str, random_floats)), filename)
        print(f"Floats saved to {filename}")
def generate_random_boolean_list(size):
    booleans=[]
    for i in range(size):
        booleans.append(random.choice([True, False]))
    return booleans
def print_boolean_list(booleans):
    for b in booleans:
        print(b)
def main_boolean():
    print("Welcome to the Random Boolean Generator!")
    size = int(input("How many random boolean values do you want to generate? "))
    random_booleans = generate_random_boolean_list(size)
    print("\nGenerated Random Boolean Values:\n")
    print_boolean_list(random_booleans)
    save_option = input("Do you want to save these booleans to a file? (yes/no) ")
    if save_option.lower() == 'yes':
        filename = input("Enter the filename (with .txt extension): ")
        save_text_to_file('\n'.join(map(str, random_booleans)), filename)
        print(f"Booleans saved to {filename}")
def generate_random_string_with_numbers(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))
def generate_multiple_random_strings_with_numbers(count, length):
    strings = []
    for i in range(count):
        strings.append(generate_random_string_with_numbers(length))
    return strings
def print_random_strings_with_numbers(strings):
    for s in strings:
        print(s)
def main_strings_with_numbers():
    print("Welcome to the Random String with Numbers Generator!")
    num_strings = int(input("How many random strings with numbers do you want to generate? "))
    length_of_strings = int(input("What should be the length of each string? "))
    random_strings = generate_multiple_random_strings_with_numbers(num_strings, length_of_strings)
    print("\nGenerated Random Strings with Numbers:\n")
    print_random_strings_with_numbers(random_strings)
    save_option = input("Do you want to save these strings to a file? (yes/no) ")
    if save_option.lower()=='yes':
        filename = input("Enter the filename (with .txt extension): ")
        save_text_to_file('\n'.join(random_strings),filename)
        print(f"Strings saved to {filename}")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    run_all()
    main()
    main_extended()
    main_numbers()
    main_float_numbers()
    main_boolean()
    main_strings_with_numbers()