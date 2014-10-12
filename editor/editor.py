from command_parser import EditorPrompt
from canvas import Canvas

if __name__ == '__main__':
    canvas = Canvas()
    prompt = EditorPrompt(canvas)
    prompt.prompt = '>'
    prompt.cmdloop('Welcome to Editor')
