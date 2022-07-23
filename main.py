import tkinter as tk
import multiprocessing as mp

from server import run_fastapi


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


def run_gui():
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)

    web_dir = 'web'
    p = mp.Process(target=run_fastapi, args=(web_dir,))
    p.start()
    root.mainloop()
    p.kill()


if __name__ == "__main__":
    mp.freeze_support()

    run_gui()
