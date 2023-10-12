class Memento:
    def __init__(self, content):
        self._content = content
    def get_saved_content(self):
        return self._content
class Editor:
    def __init__(self):
        self._content = ""
    def type(self, words):
        self._content += words
    def get_content(self):
        return self._content
    def save(self):
        return Memento(self._content)
    def restore(self, memento):
        self._content = memento.get_saved_content()
class History:
    def __init__(self):
        self._mementos = []
    def save(self, editor):
        self._mementos.append(editor.save())
    def undo(self, editor):
        if not self._mementos:
            return
        memento = self._mementos.pop()
        editor.restore(memento)
editor = Editor()
history = History()
editor.type("First sentence.")
editor.type(" Second sentence.")
print(editor.get_content())
history.save(editor)
editor.type(" Third sentence.")
print(editor.get_content())
history.undo(editor)
print(editor.get_content())
