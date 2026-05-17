import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import sys
import os
import threading
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))

from lessons_cpp import lessons_cpp, PHASES_CPP
from lessons_cpp_advanced import lessons_cpp_advanced, PHASES_CPP_ADVANCED
from lessons_cpp_v3 import lessons_cpp_v3, PHASES_CPP_V3
from lessons_python import lessons_python, PHASES_PYTHON
from lessons_python_advanced import lessons_python_advanced, PHASES_PYTHON_ADVANCED
from lessons_python_v3 import lessons_python_v3, PHASES_PYTHON_V3
from progress import load_progress, save_progress, mark_lesson_completed, get_completed_count, is_completed, save_current_pos, load_current_pos
from checker import check_python, check_cpp_output
from ai_tutor import load_config, save_config, ask_ai, clear_history, PROVIDER_PRESETS, generate_tutor_prompt
from calendar_data import record_study, get_month_data, get_month_stats, get_all_stats
from i18n import _, LANGUAGES, load_lang_pref, save_lang_pref


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(_("main_title"))
        self.root.geometry("1200x780")
        self.root.minsize(1000, 680)

        icon_path = os.path.join(os.path.dirname(__file__), "icon.jpg")
        if os.path.exists(icon_path):
            try:
                from PIL import Image, ImageTk
                img = Image.open(icon_path)
                icon_photo = ImageTk.PhotoImage(img)
                self.root.iconphoto(True, icon_photo)
                self.root.icon = icon_photo
            except Exception:
                pass

        try:
            style = ttk.Style()
            style.theme_use("vista")
            style.configure("TButton", font=("Microsoft YaHei", 9))
            style.configure("TLabelframe.Label", font=("Microsoft YaHei", 9, "bold"))
            style.configure("TLabel", font=("Microsoft YaHei", 9))
            style.configure("Header.TLabel", font=("Microsoft YaHei", 12, "bold"), foreground="#1a1a2e")
            style.configure("Title.TLabel", font=("Microsoft YaHei", 14, "bold"), foreground="#0d47a1")
            style.configure("Green.TLabel", foreground="#27ae60", font=("Microsoft YaHei", 9, "bold"))
            style.configure("Phase.TLabel", font=("Microsoft YaHei", 10), foreground="#7f8c8d")
            style.configure("green.Horizontal.TProgressbar", troughcolor="#e8f5e9", background="#43a047", thickness=18)
            style.configure("blue.Horizontal.TProgressbar", troughcolor="#e3f2fd", background="#1976d2", thickness=18)
        except:
            pass
        self.lang = tk.StringVar(value="python")
        self.ui_lang = tk.StringVar(value=load_lang_pref())
        self.current_lesson = None
        self.current_step_idx = 0
        self.ai_plans = []

        self._build_ui()
        self._switch_language("python")
        self._show_welcome()
        self.root.mainloop()

    def _build_ui(self):
        bg_color = "#f5f6fa"
        main = ttk.Frame(self.root, padding=6)
        main.pack(fill=tk.BOTH, expand=True)

        top = tk.Frame(main, bg="#ffffff", bd=0, highlightthickness=1,
                       highlightbackground="#e0e0e0", padx=10, pady=6)
        top.pack(fill=tk.X, pady=(0, 8))

        self._refresh_ui_text(top)

        paned = ttk.PanedWindow(main, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True)

        left = tk.Frame(paned, bg="#ffffff", bd=0, highlightthickness=1,
                        highlightbackground="#e0e0e0")
        self._build_tree(left)
        paned.add(left, weight=1)

        right = ttk.Frame(paned)
        self._build_content(right)
        paned.add(right, weight=3)

    def _switch_ui_lang(self):
        current = self.ui_lang.get()
        new = "English" if current == "中文" else "中文"
        self.ui_lang.set(new)
        save_lang_pref(new)
        self.root.title(_("main_title"))
        for w in self.top_frame.winfo_children():
            w.destroy()
        self._refresh_ui_text(self.top_frame)
        self._populate_tree()
        self._update_progress()

    def _refresh_ui_text(self, top):
        self.top_frame = top
        ttk.Label(top, text=_("lang_label"), style="Header.TLabel").pack(side=tk.LEFT)
        self.btn_cpp = ttk.Button(top, text=_("c_plus_plus"), width=7, command=lambda: self._switch_language("cpp"))
        self.btn_cpp.pack(side=tk.LEFT, padx=2)
        self.btn_py = ttk.Button(top, text=_("python"), width=7, command=lambda: self._switch_language("python"))
        self.btn_py.pack(side=tk.LEFT, padx=2)

        sep = tk.Frame(top, width=1, bg="#d0d0d0")
        sep.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=2)

        self.btn_ai_settings = ttk.Button(top, text=_("ai_settings"), width=10, command=self._open_ai_settings)
        self.btn_ai_settings.pack(side=tk.LEFT, padx=2)

        self.btn_ai_chat = ttk.Button(top, text=_("ask_ai"), width=12, command=self._open_ai_chat)
        self.btn_ai_chat.pack(side=tk.LEFT, padx=2)

        sep2 = tk.Frame(top, width=1, bg="#d0d0d0")
        sep2.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=2)

        self.btn_ai_plan = ttk.Button(top, text=_("ai_plan"), width=10, command=self._ai_plan_course)
        self.btn_ai_plan.pack(side=tk.LEFT, padx=2)

        sep3 = tk.Frame(top, width=1, bg="#d0d0d0")
        sep3.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=2)

        self.btn_calendar = ttk.Button(top, text=_("calendar_btn"), width=8, command=self._open_calendar)
        self.btn_calendar.pack(side=tk.LEFT, padx=2)

        sep4 = tk.Frame(top, width=1, bg="#d0d0d0")
        sep4.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=2)

        lang_btn_text = "EN" if self.ui_lang.get() == "中文" else "中"
        self.btn_lang = ttk.Button(top, text=lang_btn_text, width=4, command=self._switch_ui_lang)
        self.btn_lang.pack(side=tk.LEFT, padx=2)

        self.progress_label = ttk.Label(top, text="", style="Green.TLabel")
        self.progress_label.pack(side=tk.RIGHT, padx=10)

        ttk.Label(top, text=f"  {datetime.now().strftime('%Y-%m-%d')}",
                  font=("Microsoft YaHei", 9), foreground="#95a5a6").pack(side=tk.RIGHT)

    def _build_tree(self, parent):
        ttk.Label(parent, text=_("course_catalog"), style="Header.TLabel",
                  background="#ffffff").pack(anchor=tk.W, pady=(8, 5), padx=8)
        f = ttk.Frame(parent)
        f.pack(fill=tk.BOTH, expand=True, padx=4, pady=(0, 4))
        style = ttk.Style()
        style.configure("Treeview", font=("Microsoft YaHei", 9), rowheight=24)
        self.tree = ttk.Treeview(f, show="tree", selectmode="browse")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll_tree = ttk.Scrollbar(f, orient=tk.VERTICAL, command=self.tree.yview)
        scroll_tree.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll_tree.set)
        self.tree.bind("<<TreeviewSelect>>", self._on_select)

    def _build_content(self, parent):
        # --- 步骤进度条 ---
        step_bar_frame = ttk.Frame(parent)
        step_bar_frame.pack(fill=tk.X, pady=(0, 2))
        self.step_bar = ttk.Progressbar(step_bar_frame, orient=tk.HORIZONTAL, mode="determinate",
                                        style="blue.Horizontal.TProgressbar")
        self.step_bar.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.step_bar_label = ttk.Label(step_bar_frame, text="", font=("Microsoft YaHei", 8),
                                        foreground="#1565c0", width=14, anchor=tk.CENTER)
        self.step_bar_label.pack(side=tk.RIGHT, padx=(6, 0))

        # --- 课程总进度条 ---
        course_bar_frame = ttk.Frame(parent)
        course_bar_frame.pack(fill=tk.X, pady=(0, 4))
        self.course_bar = ttk.Progressbar(course_bar_frame, orient=tk.HORIZONTAL, mode="determinate",
                                          style="green.Horizontal.TProgressbar")
        self.course_bar.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.course_bar_label = ttk.Label(course_bar_frame, text="", font=("Microsoft YaHei", 8),
                                          foreground="#2e7d32", width=14, anchor=tk.CENTER)
        self.course_bar_label.pack(side=tk.RIGHT, padx=(6, 0))

        step_frame = ttk.Frame(parent)
        step_frame.pack(fill=tk.X)
        self.step_label = ttk.Label(step_frame, text="", style="Header.TLabel", foreground="#2980b9")
        self.step_label.pack(side=tk.LEFT)
        ttk.Button(step_frame, text=_("reset_step"), command=self._reset_step,
                   width=10).pack(side=tk.RIGHT)

        ttk.Separator(parent, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=(4, 6))

        canvas = tk.Canvas(parent, highlightthickness=0, bg="#f5f6fa")
        scrollbar = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#f5f6fa")
        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw", tags="inner")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.concept_label = tk.Label(scroll_frame, text="", wraplength=700,
                                       font=("Microsoft YaHei", 10), bg="#eaf4fc", fg="#1a1a2e",
                                       padx=16, pady=14, anchor=tk.W, justify=tk.LEFT,
                                       relief=tk.RIDGE, bd=1, highlightthickness=0)
        self.concept_label.pack(fill=tk.X, padx=5, pady=(0, 6))

        self.example_frame = ttk.LabelFrame(scroll_frame, text=_("example_code"),
                                            padding=4)
        self.example_frame.pack(fill=tk.X, padx=5, pady=(0, 6))
        self.example_text = tk.Text(self.example_frame, height=5, wrap=tk.NONE,
                                     font=("Consolas", 10), bg="#1e1e1e", fg="#d4d4d4",
                                     padx=10, pady=8, relief=tk.FLAT, bd=1,
                                     highlightthickness=0)
        self.example_text.pack(fill=tk.X, padx=5, pady=5)

        desc_frame = ttk.LabelFrame(scroll_frame, text="\U0001F4DD \u7ec3\u4e60\u9898",
                                    padding=4)
        desc_frame.pack(fill=tk.X, padx=5, pady=(0, 6))
        self.exercise_desc = tk.Text(desc_frame, height=3, wrap=tk.WORD, font=("Microsoft YaHei", 10),
                                      bg="#fffbf0", fg="#2c3e50", padx=12, pady=8,
                                      relief=tk.FLAT, bd=1)
        self.exercise_desc.pack(fill=tk.X, padx=5, pady=5)

        io_frame = ttk.LabelFrame(scroll_frame, text="\U0001F4C4 \u6837\u4f8b",
                                  padding=4)
        io_frame.pack(fill=tk.X, padx=5, pady=(0, 6))
        io_inner = ttk.Frame(io_frame)
        io_inner.pack(fill=tk.X, padx=8, pady=4)
        ttk.Label(io_inner, text="\U0001F4E5 \u8f93\u5165:", font=("Microsoft YaHei", 9, "bold"),
                  foreground="#5a6c7d").pack(side=tk.LEFT)
        self.io_input = ttk.Label(io_inner, text="", font=("Consolas", 9), foreground="#7f8c8d")
        self.io_input.pack(side=tk.LEFT, padx=6)
        ttk.Label(io_inner, text="\U0001F4E4 \u671f\u671b\u8f93\u51fa:", font=("Microsoft YaHei", 9, "bold"),
                  foreground="#5a6c7d").pack(side=tk.LEFT, padx=(15, 0))
        self.io_output = ttk.Label(io_inner, text="", font=("Consolas", 9), foreground="#7f8c8d")
        self.io_output.pack(side=tk.LEFT, padx=6)

        code_frame = ttk.LabelFrame(scroll_frame, text="\u270D\uFE0F \u4f60\u7684\u4ee3\u7801",
                                    padding=4)
        code_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=(0, 6))
        self.code_editor = scrolledtext.ScrolledText(code_frame, height=6, wrap=tk.NONE,
                                                      font=("Consolas", 11), bg="#1e1e1e", fg="#d4d4d4",
                                                      insertbackground="white", padx=10, pady=8,
                                                      relief=tk.FLAT, bd=1)
        self.code_editor.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        cpp_frame = ttk.LabelFrame(scroll_frame, text="\U0001F4C4 C++ \u8f93\u51fa\u7c98\u8d34\u533a\uff08\u7528\u4f60\u7684\u7f16\u8bd1\u5668\u8fd0\u884c\u540e\u7c98\u8d34\u7ed3\u679c\u5230\u8fd9\u91cc\uff09",
                                   padding=4)
        self.cpp_output = scrolledtext.ScrolledText(cpp_frame, height=2, wrap=tk.WORD,
                                                      font=("Consolas", 10), bg="#fff3cd", fg="#856404",
                                                      padx=10, pady=5)
        self.cpp_output.pack(fill=tk.X, padx=5, pady=5)
        self.cpp_frame = cpp_frame

        self.lang_note = ttk.Label(scroll_frame, text="", font=("Microsoft YaHei", 9), foreground="#e67e22")
        self.lang_note.pack(anchor=tk.W, padx=8, pady=2)

        btn_frame = ttk.Frame(scroll_frame)
        btn_frame.pack(fill=tk.X, padx=5, pady=6)

        self.btn_prev_step = ttk.Button(btn_frame, text="\u25c0 \u4e0a\u4e00\u6b65", command=self._prev_step, width=12)
        self.btn_prev_step.pack(side=tk.LEFT, padx=2)

        self.btn_run = ttk.Button(btn_frame, text="\u25b6 \u8fd0\u884c\u68c0\u67e5", command=self._run_check, width=12)
        self.btn_run.pack(side=tk.LEFT, padx=2)
        self.btn_skip = ttk.Button(btn_frame, text="\u770b\u7b54\u6848", command=self._show_answer, width=8)
        self.btn_skip.pack(side=tk.LEFT, padx=2)
        btn_ai_help = ttk.Button(btn_frame, text="\U0001F916 AI\u5e2e\u6211", command=self._ask_ai_help, width=10)
        btn_ai_help.pack(side=tk.LEFT, padx=2)

        self.btn_skip_step = ttk.Button(btn_frame, text="\u2935 \u8df3\u8fc7", command=self._skip_step, width=8)
        self.btn_skip_step.pack(side=tk.RIGHT, padx=2)

        self.btn_next = ttk.Button(btn_frame, text="\u4e0b\u4e00\u6b65 \u25b6", command=self._next_step, width=12, state=tk.DISABLED)
        self.btn_next.pack(side=tk.RIGHT, padx=2)

        result_frame = ttk.LabelFrame(scroll_frame, text="\U0001F4AC \u68c0\u67e5\u7ed3\u679c")
        result_frame.pack(fill=tk.X, padx=5, pady=3)
        self.result_text = tk.Text(result_frame, height=3, wrap=tk.WORD, font=("Consolas", 10),
                                    bg="#f8f9fa", padx=12, pady=8, relief=tk.FLAT, bd=1)
        self.result_text.pack(fill=tk.X, padx=5, pady=5)

    def _reset_step(self):
        if self.current_lesson:
            self._load_step(self.current_step_idx)

    def _switch_language(self, lang):
        self.lang.set(lang)
        self.current_step_idx = 0

        base_lessons = self._get_base_lessons(lang)
        base_phases = self._get_base_phases(lang)

        # 追加当前语言的 AI 规划课程
        ai_extra = []
        ai_phases = []
        for plan in self.ai_plans:
            if plan.get("lang") == lang or lang in plan.get("name", ""):
                ai_extra.extend(plan["lessons"])
                ai_phases.extend(plan["phases"])

        self.lessons = base_lessons + ai_extra
        self.phases = base_phases + ai_phases

        if lang == "cpp":
            self.btn_cpp.configure(text="\u2705 C++")
            self.btn_py.configure(text="Python")
            self.cpp_frame.pack(fill=tk.X, padx=5, pady=5, after=self.code_editor.master)
        else:
            self.btn_py.configure(text="\u2705 Python")
            self.btn_cpp.configure(text="C++")
            self.cpp_frame.pack_forget()
        self.lang_note.configure(
            text="\u2139 Python\u5185\u7f6e\u6267\u884c\uff0c\u76f4\u63a5\u5199\u4ee3\u7801\u70b9\u8fd0\u884c\u68c0\u67e5\u5373\u53ef"
            if lang == "python" else
            "\u2139 \u7528\u4f60\u7684\u7f16\u8bd1\u5668\u7f16\u8bd1\u8fd0\u884c\u540e\uff0c\u5c06\u7ed3\u679c\u7c98\u8d34\u5230\u4e0b\u65b9\u518d\u70b9\u68c0\u67e5")
        self._populate_tree()
        if self.lessons:
            saved_lesson_id, saved_step = load_current_pos(lang)
            found = None
            for l in self.lessons:
                if l["id"] == saved_lesson_id:
                    found = l
                    break
            if found:
                self._load_lesson(found, restore_step=False)
                if saved_lesson_id in self._tree_items:
                    self.tree.selection_set(self._tree_items[saved_lesson_id])
                    self.tree.see(self._tree_items[saved_lesson_id])
            else:
                self._load_lesson(self.lessons[0])
        self._update_progress()

    def _get_base_lessons(self, lang):
        if lang == "cpp":
            return lessons_cpp + lessons_cpp_advanced + lessons_cpp_v3
        return lessons_python + lessons_python_advanced + lessons_python_v3

    def _get_base_phases(self, lang):
        if lang == "cpp":
            return PHASES_CPP + PHASES_CPP_ADVANCED + PHASES_CPP_V3
        return PHASES_PYTHON + PHASES_PYTHON_ADVANCED + PHASES_PYTHON_V3

    def _populate_tree(self):
        self.tree.delete(*self.tree.get_children())
        self._tree_items = {}
        for phase in self.phases:
            pid = self.tree.insert("", tk.END, text=phase, open=True)
            for lesson in self.lessons:
                if lesson["phase"] == phase:
                    lid = lesson["id"]
                    done = is_completed(lid, self.lang.get())
                    prefix = "\u2705 " if done else "  "
                    iid = self.tree.insert(pid, tk.END, text=f"{prefix}{_('lesson_fmt', lid, lesson['name'])}", iid=f"l_{lid}")
                    self._tree_items[lid] = iid
        if self._tree_items:
            self.tree.selection_set(self._tree_items[min(self._tree_items.keys())])

    def _on_select(self, e):
        sel = self.tree.selection()
        if not sel:
            return
        iid = sel[0]
        for lid, tiid in self._tree_items.items():
            if tiid == iid:
                for lesson in self.lessons:
                    if lesson["id"] == lid:
                        if self.current_lesson and self.current_lesson["id"] == lid:
                            return
                        self._load_lesson(lesson, restore_step=False)
                        return

    def _load_lesson(self, lesson, restore_step=True):
        self.current_lesson = lesson
        self.current_step_idx = 0
        if restore_step:
            saved_lesson, saved_step = load_current_pos(self.lang.get())
            if saved_lesson == lesson["id"] and saved_step > 0:
                self.current_step_idx = min(saved_step, len(lesson.get("steps", [])) - 1)
        self._load_step(self.current_step_idx)

    def _load_step(self, idx):
        if not self.current_lesson:
            return
        steps = self.current_lesson.get("steps", [])
        if not steps or idx >= len(steps):
            self.step_bar["maximum"] = 1
            self.step_bar["value"] = 0
            self.step_bar_label.configure(text="")
            if self.current_lesson:
                self.step_label.configure(text=f"\u7b2c{self.current_lesson['id']}\u8bfe: {self.current_lesson['name']}")
            self._update_progress()
            return
        self.current_step_idx = idx
        step = steps[idx]
        total = len(steps)
        self.step_bar["maximum"] = total
        self.step_bar["value"] = idx + 1
        self.step_bar_label.configure(text=f"\u6b65\u9aa4 {idx+1}/{total}")
        self.step_label.configure(text=f"\u7b2c{self.current_lesson['id']}\u8bfe: {self.current_lesson['name']}  |  \u6b65\u9aa4 {idx+1}/{total}")
        self.concept_label.configure(text=step["concept"])
        self.example_text.configure(state=tk.NORMAL)
        self.example_text.delete("1.0", tk.END)
        self.example_text.insert("1.0", step.get("example", "# \u65e0\u793a\u4f8b"))
        self.example_text.configure(state=tk.DISABLED)
        ex = step["exercise"]
        self.exercise_desc.delete("1.0", tk.END)
        self.exercise_desc.insert("1.0", ex["description"])
        self.io_input.configure(text=ex["sample_input"] if ex["sample_input"] else "\uff08\u65e0\uff09")
        self.io_output.configure(text=ex["sample_output"])
        self.code_editor.delete("1.0", tk.END)
        template = ex.get("template", "")
        if template:
            self.code_editor.insert("1.0", template)
        elif self.lang.get() == "python":
            self.code_editor.insert("1.0", "# \u8bf7\u5728\u6b64\u7f16\u5199\u4ee3\u7801\n")
        self.cpp_output.delete("1.0", tk.END)
        self.result_text.delete("1.0", tk.END)
        self.result_text.configure(bg="#f8f9fa")
        self.btn_next.configure(state=tk.DISABLED)

        # 更新按钮状态
        self.btn_prev_step.configure(state=tk.NORMAL if idx > 0 else tk.DISABLED)
        self.btn_skip_step.configure(state=tk.NORMAL if idx + 1 < total else tk.DISABLED)

        # 存储当前位置
        if self.current_lesson:
            save_current_pos(self.current_lesson["id"], idx, self.lang.get())

    def _get_context(self):
        if not self.current_lesson:
            return ""
        steps = self.current_lesson.get("steps", [])
        if not steps or self.current_step_idx >= len(steps):
            return ""
        step = steps[self.current_step_idx]
        ex = step["exercise"]
        code = self.code_editor.get("1.0", tk.END).strip()
        result = self.result_text.get("1.0", tk.END).strip()
        return f"\u8bed\u8a00: {self.lang.get()}\n\u8bfe\u7a0b: {self.current_lesson['name']}\n\u6982\u5ff5: {step['concept'][:200]}\n\u7ec3\u4e60: {ex['description'][:200]}\n\u4f60\u7684\u4ee3\u7801: {code[:300]}\n\u68c0\u67e5\u7ed3\u679c: {result[:200]}"

    def _run_check(self):
        if not self.current_lesson:
            return
        steps = self.current_lesson.get("steps", [])
        if not steps or self.current_step_idx >= len(steps):
            return
        step = steps[self.current_step_idx]
        ex = step["exercise"]
        code = self.code_editor.get("1.0", tk.END).strip()
        if not code:
            self._show_result("error", "\u8bf7\u5148\u7f16\u5199\u4ee3\u7801\uff01")
            return
        if self.lang.get() == "python":
            passed, msg = check_python(code, ex["sample_input"], ex["sample_output"])
        else:
            user_output = self.cpp_output.get("1.0", tk.END).strip()
            if not user_output:
                self._show_result("error", "\u8bf7\u5148\u7f16\u8bd1\u8fd0\u884cC++\uff0c\u5c06\u7ed3\u679c\u7c98\u8d34\u5230\u4e0b\u65b9")
                return
            passed, msg = check_cpp_output(user_output, ex["sample_output"])
        if passed:
            record_study(lang=self.lang.get(), run_check=True)
            self._show_result("success", f"\u2705 {msg}")
            self.btn_next.configure(state=tk.NORMAL)
        else:
            self._show_result("error", f"\u274c {msg}")

    def _show_result(self, typ, msg):
        self.result_text.delete("1.0", tk.END)
        self.result_text.configure(bg="#d4edda" if typ == "success" else "#f8d7da",
                                    foreground="#155724" if typ == "success" else "#721c24")
        self.result_text.insert("1.0", msg)

    def _show_answer(self):
        if not self.current_lesson:
            return
        steps = self.current_lesson.get("steps", [])
        if not steps or self.current_step_idx >= len(steps):
            return
        ex = steps[self.current_step_idx]["exercise"]
        self.code_editor.delete("1.0", tk.END)
        if self.lang.get() == "python":
            sample = ex["sample_output"]
            if "\\n" in sample:
                lines = sample.split("\\n")
                code = "\n".join(f'print("{line}")' for line in lines)
            else:
                code = f'print("{sample}")'
            self.code_editor.insert("1.0", code)
        else:
            self.code_editor.insert("1.0", f"// \u53c2\u8003\uff1a\u8f93\u51fa\u671f\u671b\u5185\u5bb9\n// {ex['sample_output']}")
        self._show_result("success", "\u5df2\u663e\u793a\u53c2\u8003\u7b54\u6848\uff0c\u53ef\u4ee5\u7ee7\u7eed\u4e0b\u4e00\u6b65")
        self.btn_next.configure(state=tk.NORMAL)

    def _prev_step(self):
        if not self.current_lesson:
            return
        if self.current_step_idx > 0:
            self._load_step(self.current_step_idx - 1)

    def _next_step(self):
        if not self.current_lesson:
            return
        steps = self.current_lesson.get("steps", [])
        if self.current_step_idx + 1 < len(steps):
            record_study(lang=self.lang.get(), steps_done=1)
            self._load_step(self.current_step_idx + 1)
        else:
            self._mark_completed()

    def _skip_step(self):
        self._next_step()

    def _mark_completed(self):
        lesson = self.current_lesson
        if not lesson:
            return
        mark_lesson_completed(lesson["id"], lesson["name"], self.lang.get())
        record_study(lang=self.lang.get(), lessons_done=1)
        self._update_progress()
        self._populate_tree()
        total = len(self.lessons)
        count = get_completed_count(self.lang.get())
        messagebox.showinfo(_("congrats_title"), _("congrats_msg", lesson["id"], lesson["name"], count, total))
        next_id = lesson["id"] + 1
        if next_id < len(self.lessons):
            if messagebox.askyesno(_("next_lesson_title"), _("next_lesson_ask", self.lessons[next_id]["name"])):
                self._load_lesson(self.lessons[next_id])
                if next_id in self._tree_items:
                    self.tree.selection_set(self._tree_items[next_id])
                    self.tree.see(self._tree_items[next_id])

    def _update_progress(self):
        count = get_completed_count(self.lang.get())
        total = len(self.lessons)
        pct = count / total * 100 if total else 0
        self.progress_label.configure(text=f"\u8fdb\u5ea6\uff1a{count}/{total} ({pct:.0f}%)")
        self.course_bar["maximum"] = total
        self.course_bar["value"] = count
        self.course_bar_label.configure(text=f"{count}/{total}")

    def _update_chat_context_bar(self, frame):
        lang_emoji = "\U0001F40D" if self.lang.get() == "python" else "\U0001F4C4"
        lang_name = self.lang.get().upper()
        lesson_name = self.current_lesson["name"] if self.current_lesson else "\u672a\u9009\u62e9"
        phase_name = self.current_lesson["phase"] if self.current_lesson else ""
        steps = self.current_lesson.get("steps", []) if self.current_lesson else []
        step_idx = min(self.current_step_idx + 1, len(steps)) if steps else 0
        step_total = len(steps) if steps else 0
        text = f"{lang_emoji} {lang_name}  |  \U0001F4D6 {lesson_name}  |  {phase_name}  |  \U0001F4C5 \u6b65\u9aa4 {step_idx}/{step_total}"
        lbl = ttk.Label(frame, text=text, font=("Microsoft YaHei", 9, "bold"),
                         foreground="#2c3e50", padding=(5, 3))
        lbl.pack(side=tk.LEFT)

    # ========== AI \u81ea\u4e3b\u89c4\u5212 ==========

    def _ai_plan_course(self):
        cfg = load_config()
        if not cfg.get("api_key"):
            messagebox.showwarning(_("progress"), _("plan_need_key"))
            return
        from ai_tutor import ensure_openai
        if not ensure_openai():
            messagebox.showerror("Error", _("install_error"))
            return

        win = tk.Toplevel(self.root)
        win.title(_("plan_title"))
        win.geometry("650x500")
        win.minsize(500, 400)

        main = ttk.Frame(win, padding=12)
        main.pack(fill=tk.BOTH, expand=True)

        ttk.Label(main, text=_("plan_title_label"),
                  style="Title.TLabel", font=("Microsoft YaHei", 13, "bold")).pack(anchor=tk.W, pady=(0, 5))
        ttk.Label(main, text=_("plan_desc"),
                  font=("Microsoft YaHei", 9), foreground="#7f8c8d", wraplength=550).pack(anchor=tk.W, pady=(0, 8))

        ttk.Label(main, text=_("plan_example"),
                  font=("Microsoft YaHei", 9, "italic"), foreground="#95a5a6").pack(anchor=tk.W, pady=(0, 6))

        text_frame = ttk.LabelFrame(main, text=_("plan_input_label"), padding=6)
        text_frame.pack(fill=tk.BOTH, expand=True)

        input_text = tk.Text(text_frame, height=7, wrap=tk.WORD, font=("Microsoft YaHei", 10),
                              padx=10, pady=8, relief=tk.FLAT, bd=1)
        input_text.pack(fill=tk.BOTH, expand=True)
        input_text.insert("1.0", _("plan_placeholder") + self.lang.get().upper())
        input_text.focus_set()

        status_label = ttk.Label(main, text="", font=("Microsoft YaHei", 9), foreground="#2980b9")
        status_label.pack(anchor=tk.W, pady=4)

        btn_frame = ttk.Frame(main)
        btn_frame.pack(fill=tk.X, pady=(4, 0))

        def do_plan():
            prompt = input_text.get("1.0", tk.END).strip()
            if not prompt or len(prompt) < 5:
                status_label.configure(text="\u8bf7\u8f93\u5165\u66f4\u5177\u4f53\u7684\u5b66\u4e60\u9700\u6c42", foreground="#e74c3c")
                return

            status_label.configure(text=_("plan_thinking"), foreground="#2980b9")
            plan_btn.configure(state=tk.DISABLED)

            system_prompt = (
                "你是一位资深的编程教育专家。请根据用户的需求，生成一份结构化的课程学习计划。\n"
                "请严格按以下 JSON 格式输出，不要加 markdown 代码块标记，直接输出 JSON 数组：\n"
                "[\n"
                "  {\n"
                '    "name": "课程名称",\n'
                '    "phase": "阶段名称",\n'
                '    "concept": "本课的核心知识点说明，200字以内",\n'
                '    "example": "示例代码片段",\n'
                '    "exercise_desc": "练习题描述",\n'
                '    "sample_output": "期望输出"\n'
                "  },\n"
                "  ...\n"
                "]\n\n"
                "要求：\n"
                "1. 生成 5-12 节课\n"
                "2. 每课涵盖一个独立的知识点\n"
                "3. 按难度递进排列\n"
                "4. 阶段名称按内容分组（如 \"基础语法\"、\"进阶技巧\"、\"实战项目\"）\n"
                "5. 示例代码和练习题要实际可运行\n"
                "6. sample_output 是运行代码后期望看到的输出\n"
                "7. 如果是 C++，代码用 #include <iostream> 和 cout\n"
                "8. 如果是 Python，代码用 print()\n"
                "9. 所有文本用中文"
            )

            user_request = f"\u8bed\u8a00: {self.lang.get().upper()}\n\u7528\u6237\u9700\u6c42: {prompt}"

            def worker():
                ok, result = ask_ai(user_request, context=None, callback=None,
                                   max_tokens=4096, temperature=0.3,
                                   system_override=system_prompt)
                win.after(0, lambda: _on_result(ok, result))

            def _on_result(ok, result):
                if not ok:
                    status_label.configure(text=f"\u274C {result}", foreground="#e74c3c")
                    plan_btn.configure(state=tk.NORMAL)
                    return
                try:
                    import json
                    import re
                    raw = result
                    result = re.sub(r'```[\w]*\n?', '', result)
                    start = result.find('[')
                    end = result.rfind(']')
                    if start == -1 or end == -1 or end <= start:
                        preview = raw[:300].replace('\n', ' ')
                        raise ValueError(_("plan_no_json") + f"\n{_('plan_parse_error')}: {preview}")
                    json_str = result[start:end+1]
                    lessons_data = json.loads(json_str)
                    if not isinstance(lessons_data, list):
                        raise ValueError(_("plan_not_array"))
                    if len(lessons_data) < 2:
                        raise ValueError(_("plan_too_few"))
                    _apply_plan(lessons_data)
                except json.JSONDecodeError as e:
                    preview = raw[:300].replace('\n', ' ')
                    status_label.configure(
                        text=f"\u274C {_('plan_parse_error')}: {e}\nAI: {preview}",
                        foreground="#e74c3c")
                    plan_btn.configure(state=tk.NORMAL)
                except Exception as e:
                    status_label.configure(text=f"\u274C \u89e3\u6790\u5931\u8d25: {e}", foreground="#e74c3c")
                    plan_btn.configure(state=tk.NORMAL)

            def _apply_plan(lessons_data):
                lang = self.lang.get()
                ai_lessons = []
                ai_phase_set = set()
                for i, item in enumerate(lessons_data):
                    raw_phase = item.get('phase', '自定义')
                    phase = f"\U0001F9D0 AI\u89c4\u5212 - {raw_phase}"
                    ai_phase_set.add(phase)
                    lesson = {
                        "id": 9000 + i,
                        "name": item.get("name", f"\u7b2c{i+1}\u8bfe"),
                        "phase": phase,
                        "steps": [
                            {
                                "concept": item.get("concept", ""),
                                "example": item.get("example", ""),
                                "exercise": {
                                    "description": item.get("exercise_desc", "\u8bf7\u5b8c\u6210\u672c\u8282\u5b66\u4e60"),
                                    "template": "",
                                    "sample_input": "",
                                    "sample_output": item.get("sample_output", "")
                                }
                            }
                        ]
                    }
                    ai_lessons.append(lesson)

                ai_phases = sorted(ai_phase_set)
                plan_entry = {
                    "lang": lang,
                    "lessons": ai_lessons,
                    "phases": ai_phases,
                    "name": f"AI\u89c4\u5212 #{len(self.ai_plans) + 1}"
                }
                self.ai_plans.append(plan_entry)

                self.lessons = self._get_base_lessons(lang) + ai_lessons
                self.phases = self._get_base_phases(lang) + ai_phases

                self._populate_tree()
                self._load_lesson(ai_lessons[0])
                if ai_lessons[0]["id"] in self._tree_items:
                    self.tree.selection_set(self._tree_items[ai_lessons[0]["id"]])
                    self.tree.see(self._tree_items[ai_lessons[0]["id"]])
                self._update_progress()

                status_label.configure(text=_("plan_success", len(ai_lessons)), foreground="#27ae60")
                win.after(1500, win.destroy)

            threading.Thread(target=worker, daemon=True).start()

        plan_btn = ttk.Button(btn_frame, text="\U0001F9D0 \u5f00\u59cb\u89c4\u5212", command=do_plan, width=16)
        plan_btn.pack(side=tk.RIGHT)
        ttk.Button(btn_frame, text="\u53d6\u6d88", command=win.destroy, width=10).pack(side=tk.RIGHT, padx=5)

    def _show_welcome(self):
        win = tk.Toplevel(self.root)
        win.title(_("welcome_title"))
        win.geometry("520x300")
        win.resizable(False, False)
        win.transient(self.root)
        win.grab_set()

        win.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() - 520) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - 300) // 2
        win.geometry(f"+{x}+{y}")

        frame = tk.Frame(win, bg="#f0f4ff", padx=30, pady=30)
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text=_("welcome_title_line1"), font=("Microsoft YaHei", 16, "bold"),
                 bg="#f0f4ff", fg="#0d47a1").pack(pady=(10, 5))
        tk.Label(frame, text=_("welcome_title_line2"), font=("Microsoft YaHei", 15, "bold"),
                 bg="#f0f4ff", fg="#1565c0").pack(pady=(0, 20))

        sep = tk.Frame(frame, height=2, bg="#bbdefb")
        sep.pack(fill=tk.X, padx=20)

        tk.Label(frame, text=_("welcome_dev_by"),
                 font=("Microsoft YaHei", 10), bg="#f0f4ff", fg="#37474f").pack(pady=(20, 5))
        tk.Label(frame, text=_("welcome_open_source"),
                 font=("Microsoft YaHei", 10, "bold"), bg="#f0f4ff", fg="#2e7d32").pack(pady=(0, 20))

        def _on_start():
            win.destroy()
            self._show_intro()

        btn = tk.Button(frame, text=_("welcome_start"), font=("Microsoft YaHei", 11, "bold"),
                        bg="#1976d2", fg="white", padx=30, pady=6, bd=0, cursor="hand2",
                        activebackground="#1565c0", activeforeground="white",
                        command=_on_start)
        btn.pack()

        def on_enter(e):
            btn.configure(bg="#1565c0")
        def on_leave(e):
            btn.configure(bg="#1976d2")
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

        win.protocol("WM_DELETE_WINDOW", win.destroy)

    def _show_intro(self):
        win = tk.Toplevel(self.root)
        win.title(_("intro_title"))
        win.geometry("660x540")
        win.resizable(False, False)
        win.transient(self.root)
        win.grab_set()

        win.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() - 660) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - 540) // 2
        win.geometry(f"+{x}+{y}")

        canvas = tk.Canvas(win, highlightthickness=0, bg="#ffffff")
        scrollbar = ttk.Scrollbar(win, orient=tk.VERTICAL, command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#ffffff")
        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw", tags="inner")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        def _on_mousewheel(e):
            canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        frame = tk.Frame(scroll_frame, bg="#ffffff", padx=35, pady=25)
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text=_("intro_architecture"), font=("Microsoft YaHei", 16, "bold"),
                 bg="#ffffff", fg="#0d47a1").pack(anchor=tk.W, pady=(0, 15))

        sep_line = tk.Frame(frame, height=2, bg="#bbdefb")
        sep_line.pack(fill=tk.X, pady=(0, 12))

        sections = [
            (_("intro_section_langs"), [
                (_("intro_python"), _("intro_python_desc")),
                (_("intro_cpp"), _("intro_cpp_desc")),
            ]),
            (_("intro_section_learning"), [
                (_("intro_guided"), _("intro_guided_desc")),
                (_("intro_progress"), _("intro_progress_desc")),
                (_("intro_check"), _("intro_check_desc")),
            ]),
            (_("intro_section_ai"), [
                (_("intro_ai_tutor"), _("intro_ai_tutor_desc")),
                (_("intro_ai_plan"), _("intro_ai_plan_desc")),
                (_("intro_ai_debug"), _("intro_ai_debug_desc")),
            ]),
            (_("intro_section_goals"), [
                (_("intro_zero"), _("intro_zero_desc")),
                (_("intro_comp"), _("intro_comp_desc")),
                (_("intro_oss"), _("intro_oss_desc")),
            ]),
        ]

        for section_title, items in sections:
            tk.Label(frame, text=section_title, font=("Microsoft YaHei", 12, "bold"),
                     bg="#ffffff", fg="#1565c0").pack(anchor=tk.W, pady=(10, 5))
            for item_title, item_content in items:
                item = tk.Frame(frame, bg="#f8f9fa", padx=14, pady=8, bd=1, relief=tk.FLAT)
                item.pack(fill=tk.X, pady=2)
                tk.Label(item, text=item_title, font=("Microsoft YaHei", 10, "bold"),
                         bg="#f8f9fa", fg="#1a1a2e").pack(anchor=tk.W)
                tk.Label(item, text=item_content, font=("Microsoft YaHei", 9),
                         bg="#f8f9fa", fg="#555555", justify=tk.LEFT, wraplength=540).pack(anchor=tk.W, padx=(10, 0))

        final_sep = tk.Frame(frame, height=2, bg="#bbdefb")
        final_sep.pack(fill=tk.X, pady=(15, 10))

        btn = tk.Button(frame, text=_("start_using"), font=("Microsoft YaHei", 12, "bold"),
                        bg="#2e7d32", fg="white", padx=40, pady=8, bd=0, cursor="hand2",
                        activebackground="#1b5e20", activeforeground="white")
        btn.pack(pady=(0, 10))

        def on_enter(e):
            btn.configure(bg="#1b5e20")
        def on_leave(e):
            btn.configure(bg="#2e7d32")
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

        def _close_intro():
            canvas.unbind_all("<MouseWheel>")
            win.destroy()
        btn.configure(command=_close_intro)
        win.protocol("WM_DELETE_WINDOW", _close_intro)

    def _open_calendar(self):
        from calendar import monthrange
        now = datetime.now()
        cur_year, cur_month = now.year, now.month

        win = tk.Toplevel(self.root)
        win.title("\U0001F4C5 \u5b66\u4e60\u65e5\u5fd7")
        win.geometry("640x580")
        win.resizable(False, False)
        win.transient(self.root)
        win.grab_set()
        win.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() - 640) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - 580) // 2
        win.geometry(f"+{x}+{y}")

        header_frame = tk.Frame(win, bg="#1565c0", padx=20, pady=12)
        header_frame.pack(fill=tk.X)
        tk.Label(header_frame, text="\U0001F4C5 \u5b66\u4e60\u65e5\u5fd7", font=("Microsoft YaHei", 15, "bold"),
                 bg="#1565c0", fg="white").pack()

        main_frame = tk.Frame(win, bg="#ffffff", padx=20, pady=12)
        main_frame.pack(fill=tk.BOTH, expand=True)

        nav_frame = tk.Frame(main_frame, bg="#ffffff")
        nav_frame.pack(fill=tk.X, pady=(0, 10))

        display_year = tk.StringVar(value=str(cur_year))
        display_month = tk.StringVar(value=str(cur_month))

        def refresh_calendar():
            for w in cal_frame.winfo_children():
                w.destroy()
            year = int(display_year.get())
            month = int(display_month.get())
            _build_calendar(year, month)

        def prev_month():
            y, m = int(display_year.get()), int(display_month.get())
            if m == 1:
                display_year.set(str(y - 1))
                display_month.set("12")
            else:
                display_month.set(str(m - 1))
            refresh_calendar()

        def next_month():
            y, m = int(display_year.get()), int(display_month.get())
            if m == 12:
                display_year.set(str(y + 1))
                display_month.set("1")
            else:
                display_month.set(str(m + 1))
            refresh_calendar()

        ttk.Button(nav_frame, text="\u25c0", width=3, command=prev_month).pack(side=tk.LEFT)
        month_label = ttk.Label(nav_frame, text="", font=("Microsoft YaHei", 13, "bold"),
                                foreground="#0d47a1")
        month_label.pack(side=tk.LEFT, expand=True)
        ttk.Button(nav_frame, text="\u25b6", width=3, command=next_month).pack(side=tk.RIGHT)

        cal_frame = tk.Frame(main_frame, bg="#ffffff")
        cal_frame.pack(fill=tk.BOTH, expand=True)

        def _build_calendar(year, month):
            month_label.configure(text=_("calendar_month_title", year, month))
            month_data = get_month_data(year, month)
            stats = get_month_stats(year, month)

            weekday_frame = tk.Frame(cal_frame, bg="#ffffff")
            weekday_frame.pack(fill=tk.X, pady=(0, 4))
            weekdays = ["\u4e00", "\u4e8c", "\u4e09", "\u56db", "\u4e94", "\u516d", "\u65e5"]
            for wd in weekdays:
                c = "#e74c3c" if wd == "\u65e5" else "#e67e22" if wd == "\u516d" else "#555555"
                tk.Label(weekday_frame, text=wd, font=("Microsoft YaHei", 9, "bold"),
                         bg="#ffffff", fg=c, width=9, anchor=tk.CENTER).pack(side=tk.LEFT)

            days_in_month = monthrange(year, month)[1]
            first_weekday = monthrange(year, month)[0]
            first_weekday = (first_weekday - 1) % 7

            grid = tk.Frame(cal_frame, bg="#ffffff")
            grid.pack(fill=tk.BOTH, expand=True)

            row = tk.Frame(grid, bg="#ffffff")
            row.pack(fill=tk.X)
            for _ in range(first_weekday):
                tk.Label(row, text="", width=9, font=("Microsoft YaHei", 10),
                         bg="#ffffff").pack(side=tk.LEFT)

            today_str = date.today().isoformat()

            for day in range(1, days_in_month + 1):
                ds = f"{year:04d}-{month:02d}-{day:02d}"
                entry = month_data.get(ds)

                bg_color = "#ffffff"
                fg_color = "#1a1a2e"
                if entry is not None:
                    minutes = entry.get("study_minutes", 0)
                    if minutes >= 30:
                        bg_color = "#1b5e20"
                        fg_color = "white"
                    elif minutes >= 15:
                        bg_color = "#43a047"
                        fg_color = "white"
                    elif minutes >= 5:
                        bg_color = "#a5d6a7"
                        fg_color = "#1a1a2e"
                    else:
                        bg_color = "#e8f5e9"
                        fg_color = "#1a1a2e"

                is_today = ds == today_str
                cell = tk.Frame(row, bg=bg_color, width=68, height=56, bd=1,
                                relief=tk.SOLID if is_today else tk.FLAT,
                                highlightbackground="#90caf9" if is_today else "#e0e0e0")
                cell.pack(side=tk.LEFT, padx=1, pady=1)
                cell.pack_propagate(False)

                day_fg = "#1565c0" if is_today else fg_color
                tk.Label(cell, text=str(day), font=("Microsoft YaHei", 10, "bold" if is_today else "normal"),
                         bg=bg_color, fg=day_fg).pack(anchor=tk.NW, padx=3, pady=1)

                if entry is not None:
                    mins = entry.get("study_minutes", 0)
                    icon = "\U0001F4D6"
                    if mins >= 20:
                        icon = "\U0001F31F"
                    elif mins >= 10:
                        icon = "\U0001F525"
                    lessons = entry.get("lessons_completed", 0)
                    lbl_text = f"{icon} {lessons}\u8bfe" if lessons > 0 else icon
                    tk.Label(cell, text=lbl_text, font=("Microsoft YaHei", 8),
                             bg=bg_color, fg=fg_color).pack(anchor=tk.SE, padx=2, pady=1)

                if (first_weekday + day) % 7 == 0 and day < days_in_month:
                    row = tk.Frame(grid, bg="#ffffff")
                    row.pack(fill=tk.X)

            stats_frame = tk.Frame(cal_frame, bg="#f8f9fa", padx=12, pady=8, bd=1, relief=tk.FLAT)
            stats_frame.pack(fill=tk.X, pady=(8, 0))

            tk.Label(stats_frame, text=_("calendar_stats_month"), font=("Microsoft YaHei", 10, "bold"),
                     bg="#f8f9fa", fg="#0d47a1").pack(anchor=tk.W)
            stat_text = _("calendar_stat_fmt", stats['total_days'], stats['total_lessons'], stats['total_steps'], stats['total_checks'])
            tk.Label(stats_frame, text=stat_text, font=("Microsoft YaHei", 9),
                     bg="#f8f9fa", fg="#555555").pack(anchor=tk.W, padx=(5, 0))

            all_stats = get_all_stats()
            tk.Label(stats_frame, text=_("calendar_stats_all") + ": " + _("calendar_stat_all_fmt", all_stats['total_days'], all_stats['total_lessons'], all_stats['total_steps']),
                     font=("Microsoft YaHei", 9), bg="#f8f9fa", fg="#888888").pack(anchor=tk.W, padx=(5, 0))

        _build_calendar(cur_year, cur_month)

        btn_frame = tk.Frame(win, bg="#ffffff", padx=20, pady=10)
        btn_frame.pack(fill=tk.X)
        ttk.Button(btn_frame, text="\u5173\u95ed", command=win.destroy).pack(side=tk.RIGHT)

    def _open_ai_settings(self):
        win = tk.Toplevel(self.root)
        win.title(_("settings_title"))
        win.geometry("600x560")
        win.resizable(False, False)

        cfg = load_config()

        ttk.Label(win, text="AI " + (_("settings_title") if load_lang_pref() == "中文" else "Settings"),
                  font=("Microsoft YaHei", 14, "bold"),
                  foreground="#2c3e50").pack(pady=10)

        nb = ttk.Notebook(win)
        nb.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        tab1 = ttk.Frame(nb)
        nb.add(tab1, text=_("ai_settings_tab_basic"))

        frame1 = ttk.Frame(tab1, padding=15)
        frame1.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame1, text=_("select_provider"), font=("Microsoft YaHei", 10)).grid(row=0, column=0, sticky=tk.W, pady=5)
        provider_var = tk.StringVar()
        provider_combo = ttk.Combobox(frame1, textvariable=provider_var, values=list(PROVIDER_PRESETS.keys()), state="readonly", width=30)
        provider_combo.grid(row=0, column=1, pady=5, sticky=tk.W)

        saved_provider = cfg.get("provider_name", "")
        if saved_provider in PROVIDER_PRESETS:
            provider_combo.set(saved_provider)
        else:
            provider_combo.set("DeepSeek")

        def on_provider_change(e):
            name = provider_var.get()
            if name in PROVIDER_PRESETS:
                preset = PROVIDER_PRESETS[name]
                if name == "自定义":
                    return
                url_entry.delete(0, tk.END)
                url_entry.insert(0, preset["api_url"])
                model_entry.delete(0, tk.END)
                model_entry.insert(0, preset["model"])

        provider_combo.bind("<<ComboboxSelected>>", on_provider_change)

        ttk.Label(frame1, text=_("api_url"), font=("Microsoft YaHei", 10)).grid(row=1, column=0, sticky=tk.W, pady=5)
        url_entry = ttk.Entry(frame1, width=50)
        url_entry.grid(row=1, column=1, pady=5)
        url_entry.insert(0, cfg.get("api_url", ""))

        ttk.Label(frame1, text=_("api_key_label"), font=("Microsoft YaHei", 10)).grid(row=2, column=0, sticky=tk.W, pady=5)
        key_entry = ttk.Entry(frame1, width=50, show="*")
        key_entry.grid(row=2, column=1, pady=5)
        key_entry.insert(0, cfg.get("api_key", ""))

        ttk.Label(frame1, text=_("model_name"), font=("Microsoft YaHei", 10)).grid(row=3, column=0, sticky=tk.W, pady=5)
        model_entry = ttk.Entry(frame1, width=50)
        model_entry.grid(row=3, column=1, pady=5)
        model_entry.insert(0, cfg.get("model", ""))

        ttk.Label(frame1, text=_("temperature"), font=("Microsoft YaHei", 10)).grid(row=4, column=0, sticky=tk.W, pady=5)
        temp_var = tk.DoubleVar(value=cfg.get("temperature", 0.7))
        temp_scale = ttk.Scale(frame1, from_=0.0, to=2.0, variable=temp_var, orient=tk.HORIZONTAL, length=200)
        temp_scale.grid(row=4, column=1, sticky=tk.W, pady=5)
        temp_label = ttk.Label(frame1, text=f"{temp_var.get():.1f}")
        temp_label.grid(row=4, column=2, padx=5)
        def on_temp_change(e):
            temp_label.configure(text=f"{temp_var.get():.1f}")
        temp_scale.configure(command=on_temp_change)

        tab2 = ttk.Frame(nb)
        nb.add(tab2, text=_("ai_settings_tab_prompt"))

        frame2 = ttk.Frame(tab2, padding=15)
        frame2.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame2, text=_("custom_prompt"),
                  font=("Microsoft YaHei", 9), foreground="#7f8c8d").pack(anchor=tk.W)

        prompt_text = tk.Text(frame2, height=10, wrap=tk.WORD, font=("Microsoft YaHei", 10))
        prompt_text.pack(fill=tk.BOTH, expand=True, pady=5)
        prompt_text.insert("1.0", cfg.get("system_prompt", ""))

        def save_settings():
            new_cfg = {
                "provider_name": provider_var.get(),
                "api_key": key_entry.get().strip(),
                "api_url": url_entry.get().strip(),
                "model": model_entry.get().strip(),
                "temperature": temp_var.get(),
                "max_tokens": cfg.get("max_tokens", 2048),
                "system_prompt": prompt_text.get("1.0", tk.END).strip()
            }
            save_config(new_cfg)
            messagebox.showinfo(_("congrats_title"), _("save") + " " + (_("settings_title") if load_lang_pref() == "中文" else "saved!"))
            win.destroy()

        btn_frame = ttk.Frame(win)
        btn_frame.pack(fill=tk.X, padx=10, pady=10)
        ttk.Button(btn_frame, text=_("save"), command=save_settings, width=15).pack(side=tk.RIGHT, padx=5)
        ttk.Button(btn_frame, text=_("test_connection"), command=lambda: self._test_ai_connection(key_entry.get().strip(), url_entry.get().strip(), model_entry.get().strip()), width=15).pack(side=tk.RIGHT, padx=5)

    def _test_ai_connection(self, api_key, api_url, model):
        if not api_key:
            messagebox.showerror("Error", _("test_key_empty"))
            return
        old_cfg = load_config()
        test_cfg = {"api_key": api_key, "api_url": api_url, "model": model,
                     "temperature": 0.7, "max_tokens": 512,
                     "system_prompt": _("test_prompt")}
        save_config(test_cfg)
        ok, msg = ask_ai(_("test_msg"))
        save_config(old_cfg)
        if ok:
            messagebox.showinfo(_("test_ok"), f"{_('test_ok')}\n{msg}")
        else:
            messagebox.showerror(_("test_fail"), f"{_('test_fail')}:\n{msg}")

    def _ask_ai_help(self):
        cfg = load_config()
        if not cfg.get("api_key"):
            messagebox.showwarning(_("progress"), _("plan_need_key"))
            return
        from ai_tutor import ensure_openai
        if not ensure_openai():
            messagebox.showerror("Error", _("install_error"))
            return
        context = self._get_context()
        if not context:
            messagebox.showinfo(_("progress"), _("enter_lesson"))
            return
        ex = None
        if self.current_lesson:
            steps = self.current_lesson.get("steps", [])
            if steps and self.current_step_idx < len(steps):
                ex = steps[self.current_step_idx]["exercise"]
        code = self.code_editor.get("1.0", tk.END).strip()
        result_info = self.result_text.get("1.0", tk.END).strip()
        prompt = generate_tutor_prompt(
            self.current_lesson["name"] if self.current_lesson else "",
            steps[self.current_step_idx]["concept"][:300] if steps and self.current_step_idx < len(steps) else "",
            ex["description"] if ex else "",
            code, result_info
        )
        self._show_ai_chat_dialog(prompt)

    def _open_ai_chat(self):
        cfg = load_config()
        if not cfg.get("api_key"):
            messagebox.showwarning("\u63d0\u793a", "\u8bf7\u5148\u70b9\u51fb\u201c\u2699 AI\u8bbe\u7f6e\u201d\u914d\u7f6eAPI\u5bc6\u94a5\uff01")
            return
        from ai_tutor import ensure_openai
        if not ensure_openai():
            messagebox.showerror("\u9519\u8bef", "openai \u5e93\u5b89\u88c5\u5931\u8d25\uff0c\u8bf7\u624b\u52a8\u8fd0\u884c: pip install openai")
            return
        self._show_ai_chat_dialog("")

    def _show_ai_chat_dialog(self, initial_prompt=""):
        from ai_tutor import load_history as load_ai_history

        win = tk.Toplevel(self.root)
        win.title(_("chat_title"))
        win.geometry("720x620")
        win.minsize(480, 400)

        main_frame = ttk.Frame(win, padding=5)
        main_frame.pack(fill=tk.BOTH, expand=True)

        ctx_frame = ttk.Frame(main_frame)
        ctx_frame.pack(fill=tk.X)
        def refresh_ctx():
            for w in ctx_frame.winfo_children():
                w.destroy()
            self._update_chat_context_bar(ctx_frame)
        self._update_chat_context_bar(ctx_frame)
        ttk.Button(ctx_frame, text="\u21bb", width=3, command=refresh_ctx).pack(side=tk.RIGHT)

        # 输入区（底部固定）
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(5, 0))

        input_entry = tk.Text(input_frame, height=2, wrap=tk.WORD, font=("Microsoft YaHei", 10),
                               padx=10, pady=6, relief=tk.SUNKEN, bd=1)
        input_entry.pack(fill=tk.X, side=tk.LEFT, expand=True, padx=(0, 5))

        btn_frame = ttk.Frame(input_frame)
        btn_frame.pack(side=tk.RIGHT, fill=tk.Y)

        send_btn = ttk.Button(btn_frame, text="\u53d1\u9001", command=lambda: send_message(), width=8)
        send_btn.pack(fill=tk.X, pady=2)
        ttk.Button(btn_frame, text="\u6e05\u7a7a", command=lambda: clear_chat(), width=8).pack(fill=tk.X, pady=2)

        # 聊天区域 - 自适应 Canvas
        chat_canvas = tk.Canvas(main_frame, highlightthickness=0, bg="#ffffff")
        v_scroll = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=chat_canvas.yview)
        chat_canvas.configure(yscrollcommand=v_scroll.set)
        chat_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        chat_container = ttk.Frame(chat_canvas, padding=5)
        chat_container.bind("<Configure>",
                            lambda e: chat_canvas.configure(scrollregion=chat_canvas.bbox("all")))
        chat_canvas.create_window((0, 0), window=chat_container, anchor="nw", tags="inner_frame")

        # 关键：canvas 宽度变化时，让内层 frame 宽度跟着变
        def _resize_inner(event):
            chat_canvas.itemconfig("inner_frame", width=event.width)
        chat_canvas.bind("<Configure>", _resize_inner)

        # 气泡最大宽度 = canvas 宽度 * 0.75
        def _bubble_wrap_width():
            w = chat_canvas.winfo_width()
            return max(200, int(w * 0.72))

        def _make_selectable_text(parent, text, wraplength, bg, fg, font, bold=False):
            family, size = font
            font_spec = (family, size, "bold") if bold else font
            t = tk.Text(parent, wrap=tk.WORD, bg=bg, fg=fg, font=font_spec,
                         relief=tk.FLAT, bd=0, highlightthickness=0,
                         padx=0, pady=0, cursor="xterm", width=wraplength // 7, height=1)
            t.insert("1.0", text)
            t.configure(state=tk.DISABLED)
            lines = int(float(t.index(tk.END))) - 1
            t.configure(height=min(30, max(1, lines)))
            # 右键菜单复制
            menu = tk.Menu(win, tearoff=0, bg="#ffffff", fg="#2c3e50",
                          activebackground="#e8f0fe", activeforeground="#1a1a2e")
            menu.add_command(label="\u590d\u5236", font=("Microsoft YaHei", 9),
                            command=lambda t=t: _copy_text(t))
            def _show_menu(e):
                menu.tk_popup(e.x_root, e.y_root)
            t.bind("<Button-3>", _show_menu)
            return t

        def _copy_text(widget):
            try:
                text = widget.get("1.0", tk.END).strip()
                if text:
                    win.clipboard_clear()
                    win.clipboard_append(text)
            except:
                pass

        def _make_user_bubble(parent, text):
            wrap = _bubble_wrap_width()
            frame = ttk.Frame(parent)
            frame.pack(fill=tk.X, pady=4, anchor=tk.E)
            inner = tk.Frame(frame, bg="#d1e7ff", padx=12, pady=8)
            inner.pack(side=tk.RIGHT, padx=(wrap // 3, 5))
            txt = _make_selectable_text(inner, text, wrap, "#d1e7ff", "#1a1a2e",
                                         ("Microsoft YaHei", 10))
            txt.pack()

        def _make_ai_bubble(parent, reply):
            import re
            wrap = _bubble_wrap_width()
            frame = ttk.Frame(parent)
            frame.pack(fill=tk.X, pady=4, anchor=tk.W)
            tk.Label(frame, text="\U0001F916", font=("Microsoft YaHei", 11),
                      bg="#ffffff").pack(side=tk.LEFT, padx=(5, 2), anchor=tk.N)
            inner = tk.Frame(frame, bg="#ffffff", padx=12, pady=8)
            inner.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(2, wrap // 3))

            remaining = reply
            while remaining:
                block_start = remaining.find("```")
                if block_start == -1:
                    segs = re.split(r'(`[^`]+`)', remaining)
                    for seg in segs:
                        if seg.startswith("`") and seg.endswith("`"):
                            tk.Label(inner, text=seg[1:-1], font=("Consolas", 9, "bold"),
                                      bg="#fff5f5", fg="#e74c3c", padx=4, pady=1).pack(anchor=tk.W, pady=1)
                        else:
                            txt = _make_selectable_text(inner, seg, wrap, "#ffffff", "#2c3e50",
                                                         ("Microsoft YaHei", 10))
                            txt.pack(anchor=tk.W)
                    break

                before = remaining[:block_start]
                segs = re.split(r'(`[^`]+`)', before)
                for seg in segs:
                    if seg.startswith("`") and seg.endswith("`"):
                        tk.Label(inner, text=seg[1:-1], font=("Consolas", 9, "bold"),
                                  bg="#fff5f5", fg="#e74c3c", padx=4, pady=1).pack(anchor=tk.W, pady=1)
                    else:
                        txt = _make_selectable_text(inner, seg, wrap, "#ffffff", "#2c3e50",
                                                     ("Microsoft YaHei", 10))
                        txt.pack(anchor=tk.W)

                after_marker = remaining[block_start + 3:]
                lang_end = after_marker.find("\n")
                if lang_end == -1:
                    break
                code_start = lang_end + 1
                code_end = after_marker.find("```", code_start)
                if code_end == -1:
                    break
                code = after_marker[code_start:code_end].strip("\n")
                code_lang = after_marker[:lang_end].strip()
                remaining = after_marker[code_end + 3:]

                code_box = tk.Frame(inner, bg="#1e1e1e", padx=10, pady=5)
                code_box.pack(fill=tk.X, pady=4)

                top_bar = tk.Frame(code_box, bg="#1e1e1e")
                top_bar.pack(fill=tk.X)
                tk.Label(top_bar, text=f"  {code_lang.upper()}", font=("Consolas", 8),
                          bg="#1e1e1e", fg="#7f8c8d").pack(side=tk.LEFT)
                copy_btn = tk.Button(top_bar, text="\u2702 \u590d\u5236\u4ee3\u7801",
                                      font=("Microsoft YaHei", 8), bg="#2d2d2d", fg="#cccccc",
                                      relief=tk.FLAT, padx=6, pady=1, cursor="hand2",
                                      command=lambda c=code: _copy_code(c))
                copy_btn.pack(side=tk.RIGHT)

                code_text = tk.Text(code_box, height=max(2, code.count("\n") + 1), wrap=tk.NONE,
                                     font=("Consolas", 10), bg="#1e1e1e", fg="#d4d4d4",
                                     padx=5, pady=3, relief=tk.FLAT, bd=0)
                code_text.insert("1.0", code)
                code_text.configure(state=tk.DISABLED)
                code_text.pack(fill=tk.X)

            tk.Label(inner, text="", bg="#ffffff", height=1).pack()

        def _copy_code(code):
            win.clipboard_clear()
            win.clipboard_append(code)

        def _load_history():
            history = load_ai_history()
            for h in history:
                if h["role"] == "user":
                    _make_user_bubble(chat_container, h["content"][:300])
                elif h["role"] == "assistant":
                    _make_ai_bubble(chat_container, h["content"][:500])
            _scroll_to_bottom()

        def _scroll_to_bottom():
            chat_container.update_idletasks()
            chat_canvas.yview_moveto(1.0)

        _load_history()

        def send_message():
            msg = input_entry.get("1.0", tk.END).strip()
            if not msg:
                return
            input_entry.delete("1.0", tk.END)

            _make_user_bubble(chat_container, msg)
            _scroll_to_bottom()

            loading_frame = ttk.Frame(chat_container)
            loading_frame.pack(fill=tk.X, pady=4, anchor=tk.W)
            loading_lbl = tk.Label(loading_frame, text="\U0001F916 AI\u8001\u5e08\u6b63\u5728\u601d\u8003...",
                                    font=("Microsoft YaHei", 9, "italic"), bg="#ffffff", fg="#95a5a6")
            loading_lbl.pack(padx=(35, 0))
            _scroll_to_bottom()

            ctx = self._get_context()
            full_msg = f"\u3010\u5f53\u524d\u5b66\u4e60\u4e0a\u4e0b\u6587\u3011\n{ctx}\n\n\u3010\u5b66\u751f\u95ee\u9898\u3011\n{msg}" if ctx else msg

            def worker():
                ok, result = ask_ai(full_msg, callback=None)
                win.after(0, lambda: _on_result(ok, result))

            def _on_result(ok, result):
                loading_frame.destroy()
                if ok:
                    _make_ai_bubble(chat_container, result)
                else:
                    err_lbl = tk.Label(chat_container, text=f"\u274C {result}",
                                        font=("Microsoft YaHei", 10), bg="#fff5f5", fg="#e74c3c",
                                        wraplength=_bubble_wrap_width(), justify=tk.LEFT,
                                        padx=12, pady=8)
                    err_lbl.pack(fill=tk.X, pady=4, anchor=tk.W, padx=(35, 0))
                _scroll_to_bottom()

            threading.Thread(target=worker, daemon=True).start()

        def clear_chat():
            from ai_tutor import clear_history as clear_ai_history
            clear_ai_history()
            for w in chat_container.winfo_children():
                w.destroy()

        input_entry.bind("<Control-Return>", lambda e: send_message())
        win.after(100, lambda: input_entry.focus_set())
        if initial_prompt:
            input_entry.insert("1.0", initial_prompt[:80])
            win.after(200, send_message)


if __name__ == "__main__":
    App()
