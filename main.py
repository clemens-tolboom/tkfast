import tkinter as tk
import multiprocessing as mp

from server import run_fastapi


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.server_process = None

    def start_server(self):
        web_dir = 'web'
        self.server_process = mp.Process(target=run_fastapi, args=(web_dir,))
        self.server_process.start()

    def stop_server(self):
        if self.server_process is not None:
            self.server_process.kill()
            self.server_process = None


def run_gui():
    root = tk.Tk()
    app = MainApplication(root)
    app.pack(side="top", fill="both", expand=True)

    app.start_server()
    root.mainloop()
    app.stop_server()


if __name__ == "__main__":
    mp.freeze_support()

    run_gui()
