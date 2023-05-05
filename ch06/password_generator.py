import random

def create_password_generator(chars):
    def password_generator(n_chars):
        return "".join(random.choices(chars, k=n_chars))
    return password_generator

f = create_password_generator("abcdef")
print(f(5))
print(f(5))
print(f(5))
