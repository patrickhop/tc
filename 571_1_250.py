# SRM 571
# DIV 1
# 250
# 157.27 awarded
# didn't really understand the question, or the code I was writing. in the future, spend more time
# digging into the kernel of the problem, and write code that solves it. no trial and error coding.

class FoxAndMp3():
    def playList(self, n):
        files = []
        if n <= 50:
            for i in xrange(1, n+1):
                files.append(str(i) + '.mp3')
        else:
            lex = 1
            for i in xrange(1, 51):
                files.append(str(lex) + '.mp3')
                if lex <= (n / 10):
                    lex *= 10
                elif str(lex)[-1] != '9':
                    lex += 1
                else:
                    lex += 1
                    lex = lex / 10
        return tuple(sorted(files))