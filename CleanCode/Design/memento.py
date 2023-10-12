class Memento:
    """The Memento class: Stores the internal state of the Originator."""

    def __init__(self, content):
        """Initialize the memento with the given content."""
        self._content = content

    def get_saved_content(self):
        """Return the content stored in the memento."""
        return self._content


class Editor:
    """The Originator class: The object whose state we want to save and restore."""

    def __init__(self):
        """Initialize the editor with empty content."""
        self._content = ""

    def type(self, words):
        """Add words to the editor's content."""
        self._content += words

    def get_content(self):
        """Return the current content of the editor."""
        return self._content

    def save(self):
        """Save the current state of the editor and return it as a memento."""
        return Memento(self._content)

    def restore(self, memento):
        """Restore the editor's state from a given memento."""
        self._content = memento.get_saved_content()


class History:
    """The Caretaker class: Keeps track of multiple memento states."""

    def __init__(self):
        """Initialize an empty history."""
        self._mementos = []

    def save(self, editor):
        """Save the current state of the editor to history."""
        self._mementos.append(editor.save())

    def undo(self, editor):
        """Undo the last change by restoring the previous state of the editor."""
        if not self._mementos:
            return
        memento = self._mementos.pop()
        editor.restore(memento)


# Usage of the Memento pattern:
editor = Editor()
history = History()

editor.type("First sentence.")
editor.type(" Second sentence.")
print(editor.get_content())  # Output: First sentence. Second sentence.

history.save(editor)
editor.type(" Third sentence.")
print(editor.get_content())  # Output: First sentence. Second sentence. Third sentence.

history.undo(editor)
print(editor.get_content())  # Output: First sentence. Second sentence.
