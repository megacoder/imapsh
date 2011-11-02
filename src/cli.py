#!/usr/bin/python

import  sys
import  os
import  readline
import  rlcompleter

class   Completer:

    def __init__( self, words = None ):
        self.words = words
        self.words.sort()
        self.prefix = None
        return

    def complete( self, prefix, index ):
        if prefix != self.prefix:
            self.matching_words = [
                w for w in self.words if w.startswith( prefix )
            ]
            self.prefix = prefix
        try:
            return self.matching_words[ index ]
        except IndexError:
            return None

if __name__ == '__main__':
    completer = Completer( os.listdir( '.' ) )
    index = 0
    while True:
        words = completer.complete( 's', index )
        index += 1
        if words is None:
            break
        print words
