
# ================================
# <<mixin>> ExportableMixin (AF6.1)
# ================================

from ExternalTasks import send_entry_to_api, export_entry

class ExportableMixin:
    """
    Mixin que adiciona capacidade de exportação externa.
    Assume duck typing: a classe final deve implementar summary().
    """

    def export_to_file(self, filename="export.txt"):
        export_entry(self, filename)

    def send_to_api(self):
        send_entry_to_api(self)
