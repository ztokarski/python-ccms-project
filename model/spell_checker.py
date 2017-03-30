import re
import os


class Bad_words:
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, "bad_words.txt")

class Spell_checker:
    def __init__(self, text):
        self.text = text

    def check_email(self):
        pattern = r"([^\s@]{1,64})@(([^\s@]+)\.)+([a-zA-z]{2,5})"
        checker = re.match(pattern, self.text)
        if checker == None:
            return False
        else:
            return True

    def check_if_empty(self):
        pattern = r"[^\s]"
        checker = re.match(pattern, self.text)
        if checker == None:
            return False
        else:
            return True

    def delete_multiple_spaces(self):
        pattern = r' +'
        replacer = re.sub(pattern, r" ", self.text)
        self.text = replacer
        return replacer

    def replace_html_tags(self):
        pattern = r"<[^>]*>"
        replacer = re.sub(pattern, r"", self.text)
        self.text = replacer
        return replacer

    def add_links(self):
        pattern = "@^(http\:\/\/|https\:\/\/)?([a-z0-9][a-z0-9\-]*\.)+[a-z0-9][a-z0-9\-]*$@i"
        replacer = re.sub(pattern, r'<a href="\1">\1</a>', self.text)
        self.text = replacer

        return replacer

    def profanity_filter(self):
        profanities_txt = open(Bad_words.filename)
        curse_list = []
        for row in profanities_txt:
            no_spaces = re.sub("""\n""", "", row)
            curse_list.append(no_spaces)
        profanities_txt.close()
        curse_string = '|'.join(curse_list)
        pattern = r"\b(?i)(?:" + curse_string + r")\b"
        replacer = re.sub(pattern, "", self.text)
        self.text = replacer

        return replacer


    def The_Holy_Trinity_of_Regex(self):
        self.delete_multiple_spaces()
        self.profanity_filter()
        self.replace_html_tags()

        return self.text


