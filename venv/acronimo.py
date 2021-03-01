def user_input():
    return input("cual es el enfoque de tu empresa: ")

def acronym(words):

    return "".join(word[0] for word in words).upper()

def main():
    words = user_input().split()
    print(f"el acronimo de tu frase es: {acronym(words)}.")

if __name__ == "__main__":
    main()