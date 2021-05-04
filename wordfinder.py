"""Word Finder: get random words from a dictionary."""


class WordFinder:
    """get random words from dictionary.
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["ocean", "sea", "lake"]
    True

    >>> wf.random() in ["ocean", "sea", "lake"]
    True

    >>> wf.random() in ["ocean", "sea", "lake"]
    True
    """

    def start(self, path):
        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Special WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["moose", "wolf", "rabbit"]
    True

    >>> swf.random() in ["moose", "wolf", "rabbit"]
    True

    >>> swf.random() in ["moose", "wolf", "rabbit"]
    True
    """

    def parse(self, dict_file):
        """Parse list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]

