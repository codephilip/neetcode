class TextEditor(object):
    def __init__(self):
        self.stack = []
        self.content = ""

    def write(self, content):
        if not content.endswith(" "):
            content += " "
        self.stack.append(content)
        self.content += content
        return self.stack

    def read(self):
        return self.content

    def delete(self):
        if self.stack:
            last_entry = self.stack.pop()
            self.content = self.content[: -len(last_entry)]


x = TextEditor()
x.write("hello world")
x.write("hi!")

x.write("hello world 2")
x.write("howdy!")

print(x.read())
x.delete()
print(x.read())
