import sys
import click
import clipboard
import pyphen

from .letters import get_word, letter_length

hyphen = pyphen.Pyphen(lang='en')

SPACES = 6
MAX_LEN = 6

def emojify_word(word, slack_emoji, spaces=SPACES):
    all_lines = []
    word = get_word(word)
    lines = [w.replace(' ', ' '*spaces).replace('#', slack_emoji) for w in word]
    return '\n'.join(lines)

def emojify_words(words, slack_emoji=':garlic:'):
    result = ''
    for word in words:
        if len(word) > MAX_LEN:
            syllables = hyphen.wrap(word, MAX_LEN)
            emojied = emojify_words(syllables, slack_emoji)
        else:
            emojied = emojify_word(word, slack_emoji)
        result += emojied + '\n \n'
    return result

@click.command()
@click.option('--emoji', '-e', default=':garlic:', help='Slack emoji shortcut')
@click.argument('words', nargs=-1)
def emojify(emoji, words):
    result = emojify_words(words, emoji)
    clipboard.copy(result)
    print('copied to clipboard!')

if __name__ == '__main__':
    emojify()
