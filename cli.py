import argparse

prog = argparse.ArgumentParser()
prog.add_argument('prompt', type=str, nargs='+', help='your question')

prog.add_argument(
    '-t, --translate', type=str, nargs=1, dest='translate', 
    help='Do the translation into the given language.', metavar='LANG'
)
prog.add_argument(
    '-r, --resume', action='store_true', 
    help='make a resume of anything', dest='resume'
)
parsed_args = prog.parse_args()


def get_prefix():
    translate = parsed_args.translate
    resume = parsed_args.resume
    if isinstance(translate, list):
        return f'traduza para {translate[0]}:'
    elif resume:
        return f'resuma:'
    

PROMPT = ' '.join(parsed_args.prompt)
