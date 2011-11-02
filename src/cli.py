#!/usr/bin/python

import  sys
import  os
import  readline
import  rlcompleter

class   Cli( object ):

    def __init__( self, histfile = '~/.readline.rc' ):
        readline.parse_and_bind( 'tab: complete' )
        readline.parse_and_bind( 'set editing-mode vi' )
        self.histfile = os.path.expanduser( histfile )
        try:
            readline.read_init_file( self.histfile )
        except IOError:
            pass
        self.completer = rlcompleter.Completer()
        self.cwd = '.'
        self.show_prompt = True
        self.prompt = '> '
        self.stdout = sys.stdout
        return

    def prompt_set( self, prompt = '> ' ):
        self.prompt = prompt
        self.show_prompt = True
        return

    def prompt_enable( self ):
        self.show_prompt = True
        return

    def prompt_disable( self ):
        self.show_prompt = False
        return

    def get_input( self, show_prompt = None, prompt = None ):
        if show_prompt is None:
            show_prompt = self.show_prompt
        if show_prompt:
            if prompt is None:
                prompt = self.prompt
            line = raw_input( prompt ).strip()
        else:
            line = self.stdin.readline().strip()
        return line

if __name__ == '__main__':
    cli = Cli()
    line = cli.get_input()
    print line
