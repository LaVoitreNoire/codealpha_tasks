import random

def select_random_word():
    words = [
    'python', 'hangman', 'programming', 'developer', 'function',
    'variable', 'keyboard', 'monitor', 'internet', 'database',
    'algorithm', 'engineer', 'software', 'hardware', 'network',
    'laptop', 'desktop', 'compile', 'syntax', 'runtime',
    'debugger', 'loop', 'condition', 'statement', 'integer',
    'float', 'string', 'boolean', 'array', 'list',
    'dictionary', 'tuple', 'exception', 'operator', 'class',
    'object', 'inheritance', 'module', 'package', 'library',
    'binary', 'decimal', 'hexadecimal', 'frontend', 'backend',
    'server', 'client', 'socket', 'protocol', 'request',
    'response', 'framework', 'virtual', 'environment', 'terminal',
    'editor', 'command', 'repository', 'version', 'control',
    'github', 'commit', 'branch', 'merge', 'pull',
    'push', 'clone', 'debug', 'execute', 'script',
    'logic', 'design', 'interface', 'storage', 'memory',
    'cache', 'thread', 'process', 'stack', 'queue',
    'pointer', 'bit', 'byte', 'kernel', 'driver',
    'linux', 'windows', 'macos', 'cloud', 'docker',
    'api', 'json', 'xml', 'encryption', 'security'
] # can include many by creating a txt file and merging it with this

    return random.choice(words)

def hangman_game():
    word = select_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while incorrect_guesses < max_incorrect_guesses:
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
        else:
            incorrect_guesses += 1
            print(f"Incorrect! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        current_state = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print("Word:", ' '.join(current_state))

        if '_' not in current_state:
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nGame over! The word was:", word)

hangman_game()