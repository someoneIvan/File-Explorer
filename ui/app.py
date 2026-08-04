import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import customtkinter as ctk
from pathlib import Path
from core.actions import change_directory, file_list, open_file
import shutil

# Настройки темы
ctk.set_appearance_mode("System")  # Dark, Light, System
ctk.set_default_color_theme("blue")

class FileExplorerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Настройка окна
        self.title("File Explorer")
        self.geometry("700x500")

        # Текущий путь
        self.current_path = Path.cwd()

        # --- ВЕРХНЯЯ ПАНЕЛЬ (Путь и навигация) ---
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(fill="x", padx=10, pady=10)

        self.btn_up = ctk.CTkButton(self.top_frame, text="⬆ Наверх", width=80, command=self.go_up)
        self.btn_up.pack(side="left", padx=5)

        self.path_entry = ctk.CTkEntry(self.top_frame, placeholder_text="Путь...")
        self.path_entry.pack(side="left", fill="x", expand=True, padx=5)

        # --- СЕРЕДИНА (Список файлов) ---
        self.scrollable_frame = ctk.CTkScrollableFrame(self, label_text="Содержимое папки")
        self.scrollable_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # --- НИЖНЯЯ ПАНЕЛЬ (Кнопки действий) ---
        self.bottom_frame = ctk.CTkFrame(self)
        self.bottom_frame.pack(fill="x", padx=10, pady=10)

        self.btn_open = ctk.CTkButton(self.bottom_frame, text="Открыть", command=self.open_selected)
        self.btn_open.pack(side="left", padx=5)

        self.btn_delete = ctk.CTkButton(self.bottom_frame, text="Удалить", fg_color="red", hover_color="darkred", command=self.delete_selected)
        self.btn_delete.pack(side="left", padx=5)

        self.selected_item = None
        self.load_directory(self.current_path)

    def load_directory(self, path: Path):
        """Загрузка и отображение файлов из папки"""
        self.current_path = path
        self.path_entry.delete(0, "end")
        self.path_entry.insert(0, str(self.current_path))

        # Очищаем старый список элементов
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        self.selected_item = None

        try:
            for item in self.current_path.iterdir():
                icon = "📁 " if item.is_dir() else "📄 "
                
                # Создаем кнопку для каждого файла/папки
                btn = ctk.CTkButton(
                    self.scrollable_frame,
                    text=f"{icon} {item.name}",
                    anchor="w",
                    fg_color="transparent",
                    text_color=("black", "white"),
                    hover_color=("gray70", "gray30"),
                    command=lambda i=item: self.select_item(i)
                )
                btn.pack(fill="x", pady=2)

        except PermissionError:
            label = ctk.CTkLabel(self.scrollable_frame, text="Нет доступа к этой папке", text_color="red")
            label.pack(pady=10)

    def select_item(self, item: Path):
        """Выбор файла или переход в папку по клику"""
        if item.is_dir():
            # Если кликнули на папку — переходим в нее
            self.load_directory(item)
        else:
            # Если файл — запоминаем его для кнопок внизу
            self.selected_item = item
            print(f"Выбран файл: {item.name}")

    def go_up(self):
        """Переход на уровень выше"""
        parent = self.current_path.parent
        if parent != self.current_path:
            self.load_directory(parent)

    def open_selected(self):
        """Открыть выбранный файл в системе"""
        if self.selected_item and self.selected_item.exists():
            open_file(self.selected_item)

    def delete_selected(self):
        """Удаление выбранного файла"""
        if self.selected_item and self.selected_item.exists():
            try:
                if self.selected_item.is_dir():
                    shutil.rmtree(self.selected_item)
                else:
                    self.selected_item.unlink()
                
                # Обновляем список
                self.load_directory(self.current_path)
            except Exception as e:
                print(f"Ошибка при удалении: {e}")

if __name__ == "__main__":
    app = FileExplorerApp()
    app.mainloop()