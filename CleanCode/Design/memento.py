# Abstracción: Esta clase representa una abstracción de un
#   Memento, que guarda un estado específico.
class Memento:
    """
    The Memento class: Stores the internal state of
    the Originator.
    """

    # Encapsulamiento: El contenido del memento es privado y
    #   solo es accesible a través de métodos específicos.
    def __init__(self, content):
        """Initialize the memento with the given content."""
        self._content = content

    def get_saved_content(self):
        """Return the content stored in the memento."""
        return self._content


# Abstracción: Esta clase representa el objeto cuyo estado
#   queremos guardar y restaurar.
class Editor:
    """
    The Originator class: The object whose state we want
    to save and restore.
    """

    # Encapsulamiento: El contenido del editor es privado y
    #   solo es accesible a través de métodos específicos.
    def __init__(self):
        """Initialize the editor with empty content."""
        self._content = ""

    def type(self, words):
        """Add words to the editor's content."""
        self._content += words

    def get_content(self):
        """Return the current content of the editor."""
        return self._content

    # Responsabilidad Única: Esta función tiene una única
    #   responsabilidad, que es crear un memento del estado actual.
    def save(self):
        """
        Save the current state of the editor and return it
        as a memento.
        """
        return Memento(self._content)

    # Responsabilidad Única: Esta función tiene una única
    #   responsabilidad, que es restaurar el estado desde un memento.
    def restore(self, memento):
        """Restore the editor's state from a given memento."""
        self._content = memento.get_saved_content()


# Abstracción: Esta clase representa la historia o registro
#   de los mementos.
# Modularidad: La clase History es un módulo separado encargado
#   de gestionar los mementos.
class History:
    """
    The Caretaker class: Keeps track of multiple memento states.
    """

    # Encapsulamiento: La lista de mementos es privada y solo
    # se modifica a través de métodos específicos.
    def __init__(self):
        """Initialize an empty history."""
        self._mementos = []

    def save(self, editor):
        """Save the current state of the editor to history."""

        self._mementos.append(editor.save())

    def undo(self, editor):
        """
        Undo the last change by restoring the previous state
        of the editor.
        """
        if not self._mementos:
            return
        memento = self._mementos.pop()
        editor.restore(memento)


# Uso del patrón Memento.
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
