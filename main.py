import tkinter as tk


class IDARADZ:
    def __init__(self, root):
        self.root = root

        self.root.title("IDARA DZ")
        self.root.geometry("1100x700")
        self.root.configure(bg="#f5f5f5")

        # الشريط الجانبي
        self.sidebar = tk.Frame(
            root,
            bg="#111111",
            width=220
        )
        self.sidebar.pack(side="right", fill="y")

        # شعار البرنامج
        self.logo = tk.Label(
            self.sidebar,
            text="IDARA DZ",
            bg="#111111",
            fg="white",
            font=("Arial", 24, "bold")
        )
        self.logo.pack(pady=40)

        # زر الوثائق
        self.docs_btn = tk.Button(
            self.sidebar,
            text="الوثائق",
            bg="white",
            fg="#111111",
            font=("Arial", 14, "bold"),
            relief="flat",
            cursor="hand2"
        )
        self.docs_btn.pack(fill="x", padx=20, pady=10, ipady=10)

        # المنطقة الرئيسية
        self.main_area = tk.Frame(
            root,
            bg="#f5f5f5"
        )
        self.main_area.pack(side="left", expand=True, fill="both")

        # العنوان
        self.title = tk.Label(
            self.main_area,
            text="قسم الوثائق",
            bg="#f5f5f5",
            fg="#111111",
            font=("Arial", 28, "bold"),
            anchor="e"
        )
        self.title.pack(fill="x", padx=40, pady=(40, 10))

        # الوصف
        self.subtitle = tk.Label(
            self.main_area,
            text="إدارة الطلبات الخطية والنماذج",
            bg="#f5f5f5",
            fg="#555555",
            font=("Arial", 13),
            anchor="e"
        )
        self.subtitle.pack(fill="x", padx=40)

        # بطاقة تجريبية
        self.card = tk.Frame(
            self.main_area,
            bg="white",
            bd=1,
            relief="solid"
        )
        self.card.pack(
            anchor="ne",
            padx=40,
            pady=40,
            ipadx=40,
            ipady=30
        )

        self.card_title = tk.Label(
            self.card,
            text="طلب خطي",
            bg="white",
            fg="#111111",
            font=("Arial", 18, "bold")
        )
        self.card_title.pack(pady=(0, 10))

        self.card_text = tk.Label(
            self.card,
            text="بطاقة تجريبية للنظام",
            bg="white",
            fg="#666666",
            font=("Arial", 11)
        )
        self.card_text.pack()

        self.preview_btn = tk.Button(
            self.card,
            text="معاينة",
            bg="#111111",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2"
        )
        self.preview_btn.pack(fill="x", pady=(20, 0), ipady=8)


root = tk.Tk()
app = IDARADZ(root)
root.mainloop()
