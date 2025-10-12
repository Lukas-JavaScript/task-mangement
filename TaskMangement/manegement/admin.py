from django.contrib import admin
from .models import added_tasks, in_progress_tasks, completed_tasks, removed_tasks
import socket
from tkinter import messagebox

# Register your models here.
admin.site.register(added_tasks)
admin.site.register(in_progress_tasks)
admin.site.register(completed_tasks)
admin.site.register(removed_tasks)

def get_ip_address():
    try:
        # Verbindung zu einem externen Server herstellen
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception as e:
        return str(e)

messagebox.showinfo("IP Address", f"Die Webseite ist erreichbar unter: http://{get_ip_address()}:8000/management/. Mit dem Bestätigen des Fensters wird der Server gestartet. ")#
