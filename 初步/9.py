# 游戏开始！！！

import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import time

class Minesweeper:
    def __init__(self, root):
        self.app_version = "1.3.1"
        self.root = root
        self.root.title(f"扫雷 - Windows 7 风格 v{self.app_version}")
        self.root.resizable(False, False)
        
        # 默认难度配置 (初级)
        self.difficulty_levels = {
            "简单": {"rows": 9, "cols": 9, "mines": 10},
            "中等": {"rows": 16, "cols": 16, "mines": 40},
            "困难": {"rows": 16, "cols": 30, "mines": 99}
        }
        
        self.current_difficulty = "简单"
        self.rows = self.difficulty_levels[self.current_difficulty]["rows"]
        self.cols = self.difficulty_levels[self.current_difficulty]["cols"]
        self.mines_count = self.difficulty_levels[self.current_difficulty]["mines"]
        
        # 状态变量
        self.game_over = False
        self.first_click = True
        self.flags_remaining = self.mines_count
        self.timer_start = None
        self.timer_running = False
        self.flag_mode = False
        
        # 界面颜色配置 (Win7 风格)
        self.colors = {
            'bg': "#e9e9e9",
            'cell_bg': "#80bf5a",
            'cell_revealed': "#157412",
            'border_light': "#adffaf",
            'border_dark': "#8AFF86",
            'text_colors': {
                1: '#0000ff', 2: '#008000', 3: '#ff0000', 4: '#000080',
                5: '#800000', 6: '#008080', 7: '#000000', 8: '#808080'
            }
        }
        
        self.create_menu()
        self.setup_ui()
        self.init_game_data()
        self.setup_shortcuts()
    
    def create_menu(self):
        """创建菜单栏"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # 游戏菜单
        game_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="游戏(G)", menu=game_menu)
        
        # 难度选择子菜单
        difficulty_menu = tk.Menu(game_menu, tearoff=0)
        game_menu.add_cascade(label="难度(D)", menu=difficulty_menu)
        
        difficulty_menu.add_command(label="简单 (9×9, 10个雷)", 
                                   command=lambda: self.change_difficulty("简单"),
                                   accelerator="F1")
        difficulty_menu.add_command(label="中等 (16×16, 40个雷)", 
                                   command=lambda: self.change_difficulty("中等"),
                                   accelerator="F2")
        difficulty_menu.add_command(label="困难 (16×30, 99个雷)", 
                                   command=lambda: self.change_difficulty("困难"),
                                   accelerator="F3")
        difficulty_menu.add_separator()
        difficulty_menu.add_command(label="自定义...", 
                                   command=self.custom_difficulty,
                                   accelerator="F4")
        
        game_menu.add_command(label="重新开始(R)", command=self.restart_game, accelerator="F5")
        game_menu.add_separator()
        game_menu.add_command(label="退出(Q)", command=self.root.quit, accelerator="Alt+F4")
        
        # 帮助菜单
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="帮助(H)", menu=help_menu)
        help_menu.add_command(label="游戏规则(R)", command=self.show_rules, accelerator="F11")
        help_menu.add_command(label="快捷键帮助(K)", command=self.show_shortcut_help, accelerator="F12")
        help_menu.add_separator()
        help_menu.add_command(label="关于(A)", command=self.show_about, accelerator="Ctrl+I")
    
    def setup_shortcuts(self):
        """设置快捷键绑定"""
        # 全局快捷键
        self.root.bind("<F1>", lambda e: self.change_difficulty("简单"))
        self.root.bind("<F2>", lambda e: self.change_difficulty("中等"))
        self.root.bind("<F3>", lambda e: self.change_difficulty("困难"))
        self.root.bind("<F4>", lambda e: self.custom_difficulty())
        self.root.bind("<F5>", lambda e: self.restart_game())
        self.root.bind("<F11>", lambda e: self.show_rules())
        self.root.bind("<F12>", lambda e: self.show_shortcut_help())
        
        # Ctrl组合键
        self.root.bind("<Control-i>", lambda e: self.show_about())
        self.root.bind("<Control-r>", lambda e: self.restart_game())
        self.root.bind("<Control-n>", lambda e: self.restart_game())
        
        # Alt组合键
        self.root.bind("<Alt-F4>", lambda e: self.root.quit())
        
        # 游戏操作快捷键
        self.root.bind("<Escape>", lambda e: self.restart_game())
        self.root.bind("<space>", lambda e: self.toggle_flag_mode())
        self.root.bind("<Return>", lambda e: self.reveal_selected())
        self.root.bind("<Delete>", lambda e: self.clear_flags())
        
        # 方向键移动选择
        self.root.bind("<Left>", lambda e: self.move_selection(-1, 0))
        self.root.bind("<Right>", lambda e: self.move_selection(1, 0))
        self.root.bind("<Up>", lambda e: self.move_selection(0, -1))
        self.root.bind("<Down>", lambda e: self.move_selection(0, 1))
        
        # 数字键快速标记
        for i in range(1, 9):
            self.root.bind(str(i), lambda e, num=i: self.quick_mark(num))
    
    def toggle_flag_mode(self):
        """切换标记模式（空格键）"""
        if not self.game_over:
            self.flag_mode = not self.flag_mode
            status = "已开启" if self.flag_mode else "已关闭"
            messagebox.showinfo("标记模式", f"空格标记模式{status}，可直接在当前选中格子上放置/取消旗子。")
            if hasattr(self, 'selected_row') and hasattr(self, 'selected_col'):
                self.on_right_click(self.selected_row, self.selected_col)
    
    def reveal_selected(self):
        """揭示选中的格子（回车键）"""
        if hasattr(self, 'selected_row') and hasattr(self, 'selected_col'):
            if self.flag_mode:
                self.on_right_click(self.selected_row, self.selected_col)
            elif not self.game_over and not self.flagged[self.selected_row][self.selected_col]:
                self.on_left_click(self.selected_row, self.selected_col)
    
    def clear_flags(self):
        """清除所有标记（Delete键）"""
        if not self.game_over:
            response = messagebox.askyesno("清除标记", "确定要清除所有标记吗？")
            if response:
                for r in range(self.rows):
                    for c in range(self.cols):
                        if self.flagged[r][c]:
                            self.flagged[r][c] = False
                            self.buttons[r][c].config(text="", bg=self.colors['cell_bg'])
                self.flags_remaining = self.mines_count
                self.update_mine_counter()
    
    def move_selection(self, dx, dy):
        """移动选择（方向键）"""
        if not hasattr(self, 'selected_row'):
            self.selected_row = 0
            self.selected_col = 0
        
        # 清除之前的选择
        if hasattr(self, 'selected_button'):
            self.selected_button.config(relief=tk.RAISED)
        
        # 计算新位置
        new_row = (self.selected_row + dy) % self.rows
        new_col = (self.selected_col + dx) % self.cols
        
        self.selected_row = new_row
        self.selected_col = new_col
        
        # 高亮显示当前选择
        self.selected_button = self.buttons[new_row][new_col]
        self.selected_button.config(relief=tk.SUNKEN)
    
    def quick_mark(self, number):
        """快速标记数字对应的格子（数字键1-8）"""
        if not self.game_over and hasattr(self, 'selected_row') and hasattr(self, 'selected_col'):
            row, col = self.selected_row, self.selected_col
            if not self.revealed[row][col]:
                # 标记为数字（用于标记可能有地雷的格子）
                btn = self.buttons[row][col]
                if btn.cget("text") == str(number):
                    btn.config(text="")
                else:
                    color = self.colors['text_colors'].get(number, 'black')
                    btn.config(text=str(number), fg=color)
    
    def change_difficulty(self, level):
        """切换游戏难度"""
        if level in self.difficulty_levels:
            self.current_difficulty = level
            config = self.difficulty_levels[level]
            self.rows = config["rows"]
            self.cols = config["cols"]
            self.mines_count = config["mines"]
            
            # 重新创建游戏界面
            self.game_frame.destroy()
            self.setup_game_area()
            self.init_game_data()
            
            # 调整窗口大小以适应新难度
            self.root.update_idletasks()
            self.root.geometry("")  # 重置窗口大小
            self.root.resizable(False, False)
            
            messagebox.showinfo("难度已更改", f"已切换到{level}难度")
    
    def custom_difficulty(self):
        """自定义游戏难度"""
        dialog = tk.Toplevel(self.root)
        dialog.title("自定义难度")
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.grab_set()
        
        # 居中显示对话框
        dialog.geometry("300x200")
        dialog.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() - dialog.winfo_width()) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - dialog.winfo_height()) // 2
        dialog.geometry(f"+{x}+{y}")
        
        # 添加快捷键提示
        dialog.bind("<Return>", lambda e: apply_custom())
        dialog.bind("<Escape>", lambda e: cancel())
        
        # 输入框和标签
        tk.Label(dialog, text="行数 (5-30):").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        rows_var = tk.StringVar(value=str(self.rows))
        rows_entry = tk.Entry(dialog, textvariable=rows_var, width=10)
        rows_entry.grid(row=0, column=1, padx=10, pady=10)
        rows_entry.focus_set()
        
        tk.Label(dialog, text="列数 (5-40):").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        cols_var = tk.StringVar(value=str(self.cols))
        cols_entry = tk.Entry(dialog, textvariable=cols_var, width=10)
        cols_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(dialog, text="地雷数量:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        mines_var = tk.StringVar(value=str(self.mines_count))
        mines_entry = tk.Entry(dialog, textvariable=mines_var, width=10)
        mines_entry.grid(row=2, column=1, padx=10, pady=10)
        
        def apply_custom():
            try:
                rows = int(rows_var.get())
                cols = int(cols_var.get())
                mines = int(mines_var.get())
                
                # 验证输入
                if not (5 <= rows <= 30):
                    messagebox.showerror("错误", "行数必须在5-30之间")
                    return
                if not (5 <= cols <= 40):
                    messagebox.showerror("错误", "列数必须在5-40之间")
                    return
                if not (20 <= mines <= rows * cols - 9):
                    messagebox.showerror("错误", f"地雷数量必须在20-{rows*cols-9}之间")
                    return
                
                self.rows = rows
                self.cols = cols
                self.mines_count = mines
                self.current_difficulty = "自定义"
                
                # 重新创建游戏界面
                self.game_frame.destroy()
                self.setup_game_area()
                self.init_game_data()
                
                # 调整窗口大小
                self.root.update_idletasks()
                self.root.geometry("")
                self.root.resizable(False, False)
                
                dialog.destroy()
                messagebox.showinfo("自定义难度", f"已设置为自定义难度: {rows}×{cols}, {mines}个雷")
                
            except ValueError:
                messagebox.showerror("错误", "请输入有效的数字")
        
        def cancel():
            dialog.destroy()
        
        # 按钮
        btn_frame = tk.Frame(dialog)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        tk.Button(btn_frame, text="确定(Enter)", command=apply_custom, width=12).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="取消(Esc)", command=cancel, width=12).pack(side=tk.LEFT, padx=10)
    
    def setup_ui(self):
        """设置游戏界面"""
        # 顶部面板
        top_frame = tk.Frame(self.root, bg=self.colors['bg'], bd=2, relief=tk.SUNKEN)
        top_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # 地雷计数器
        self.mine_label = tk.Label(top_frame, text=f"{self.mines_count:03d}", 
                                   font=("Digital-7", 20, "bold"), fg="red", 
                                   bg="black", width=3, anchor="e")
        self.mine_label.pack(side=tk.LEFT, padx=5, pady=2)
        
        # 重置按钮 (笑脸)
        self.reset_btn = tk.Button(top_frame, text="😊", font=("Arial", 16), 
                                   width=2, command=self.restart_game,
                                   relief=tk.RAISED, bd=2)
        self.reset_btn.pack(side=tk.LEFT, expand=True, padx=5)
        self.reset_btn.bind("<ButtonPress-1>", lambda e: self.reset_btn.config(relief=tk.SUNKEN))
        self.reset_btn.bind("<ButtonRelease-1>", lambda e: self.reset_btn.config(relief=tk.RAISED))
        
        # 难度显示标签
        self.difficulty_label = tk.Label(top_frame, text=f"难度: {self.current_difficulty}", 
                                         font=("Arial", 10), bg=self.colors['bg'])
        self.difficulty_label.pack(side=tk.LEFT, padx=10)
        
        # 计时器
        self.time_label = tk.Label(top_frame, text="000", 
                                   font=("Digital-7", 20, "bold"), fg="red", 
                                   bg="black", width=3, anchor="e")
        self.time_label.pack(side=tk.RIGHT, padx=5, pady=2)
        
        # 游戏区域
        self.setup_game_area()
    
    def setup_game_area(self):
        """设置游戏区域"""
        self.game_frame = tk.Frame(self.root, bd=3, relief=tk.SUNKEN, bg=self.colors['border_dark'])
        self.game_frame.pack(padx=5, pady=5)
        
        self.buttons = []
        for r in range(self.rows):
            row_buttons = []
            for c in range(self.cols):
                btn = tk.Button(self.game_frame, width=2, height=1, 
                                font=("Arial", 10, "bold"),
                                bg=self.colors['cell_bg'],
                                relief=tk.RAISED,
                                bd=1)
                btn.grid(row=r, column=c, padx=0, pady=0)
                
                # 绑定事件
                btn.bind("<Button-1>", lambda e, row=r, col=c: self.on_left_click(row, col))
                btn.bind("<Button-3>", lambda e, row=r, col=c: self.on_right_click(row, col))
                
                row_buttons.append(btn)
            self.buttons.append(row_buttons)
    
    def init_game_data(self):
        """初始化游戏数据"""
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.revealed = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.flagged = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.game_over = False
        self.first_click = True
        self.flags_remaining = self.mines_count
        self.update_mine_counter()
        self.update_difficulty_label()
        self.time_label.config(text="000")
        self.stop_timer()
        
        # 清除选择状态
        if hasattr(self, 'selected_button'):
            self.selected_button.config(relief=tk.RAISED)
        if hasattr(self, 'selected_row'):
            delattr(self, 'selected_row')
        if hasattr(self, 'selected_col'):
            delattr(self, 'selected_col')
    
    def update_difficulty_label(self):
        """更新难度显示标签"""
        self.difficulty_label.config(text=f"难度: {self.current_difficulty}")
    
    def place_mines(self, safe_row, safe_col):
        """放置地雷"""
        mines_placed = 0
        while mines_placed < self.mines_count:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            
            # 确保不在第一次点击的位置及其周围放置地雷
            if abs(r - safe_row) <= 1 and abs(c - safe_col) <= 1:
                continue
                
            if self.board[r][c] != -1:
                self.board[r][c] = -1
                mines_placed += 1
                
                # 更新周围数字
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.rows and 0 <= nc < self.cols and self.board[nr][nc] != -1:
                            self.board[nr][nc] += 1
    
    def on_left_click(self, row, col):
        """左键点击处理"""
        if self.game_over or self.flagged[row][col]:
            return
            
        if self.first_click:
            self.first_click = False
            self.place_mines(row, col)
            self.start_timer()
            
        self.reveal_cell(row, col)
        self.check_win()
    
    def on_right_click(self, row, col):
        """右键点击处理"""
        if self.game_over or self.revealed[row][col]:
            return
            
        btn = self.buttons[row][col]
        
        if not self.flagged[row][col]:
            self.flagged[row][col] = True
            self.flags_remaining -= 1
            btn.config(text="🚩", fg="red")
        else:
            self.flagged[row][col] = False
            self.flags_remaining += 1
            btn.config(text="", bg=self.colors['cell_bg'])
            
        self.update_mine_counter()
    
    def reveal_cell(self, row, col):
        """揭示单元格"""
        if (row < 0 or row >= self.rows or col < 0 or col >= self.cols or 
            self.revealed[row][col] or self.flagged[row][col]):
            return
            
        self.revealed[row][col] = True
        btn = self.buttons[row][col]
        btn.config(relief=tk.SUNKEN, bg=self.colors['cell_revealed'])
        
        value = self.board[row][col]
        
        if value == -1:
            self.game_lost()
        elif value > 0:
            color = self.colors['text_colors'].get(value, 'black')
            btn.config(text=str(value), fg=color)
        else:
            # 空白格，递归展开
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    self.reveal_cell(row + dr, col + dc)
    
    def game_lost(self):
        """游戏失败处理"""
        self.game_over = True
        self.stop_timer()
        self.reset_btn.config(text="😵")
        
        # 显示所有地雷
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == -1:
                    btn = self.buttons[r][c]
                    if not self.flagged[r][c]:
                        btn.config(text="💣", bg="#ffcccc")
                elif self.flagged[r][c] and self.board[r][c] != -1:
                    # 标错的地雷
                    btn.config(text="❌")
                    
        messagebox.showinfo("游戏结束", "你踩到地雷了！")
    
    def check_win(self):
        """检查是否获胜"""
        if self.game_over:
            return
            
        revealed_count = sum(sum(1 for cell in row if cell) for row in self.revealed)
        total_safe_cells = self.rows * self.cols - self.mines_count
        
        if revealed_count == total_safe_cells:
            self.game_over = True
            self.stop_timer()
            self.reset_btn.config(text="😎")
            self.flags_remaining = 0
            self.update_mine_counter()
            messagebox.showinfo("恭喜", "你赢了！")
    
    def update_mine_counter(self):
        """更新地雷计数器"""
        self.mine_label.config(text=f"{max(0, self.flags_remaining):03d}")
    
    def start_timer(self):
        """启动计时器"""
        if not self.timer_running:
            self.timer_running = True
            self.timer_start = time.time()
            self.update_timer()
    
    def stop_timer(self):
        """停止计时器"""
        self.timer_running = False
    
    def update_timer(self):
        """更新计时器显示"""
        if self.timer_running:
            elapsed = int(time.time() - self.timer_start)
            if elapsed > 999:
                elapsed = 999
            self.time_label.config(text=f"{elapsed:03d}")
            self.root.after(1000, self.update_timer)
    
    def restart_game(self):
        """重新开始游戏"""
        # 重置所有按钮外观
        for r in range(self.rows):
            for c in range(self.cols):
                btn = self.buttons[r][c]
                btn.config(text="", bg=self.colors['cell_bg'], relief=tk.RAISED)
        
        self.reset_btn.config(text="😊")
        self.init_game_data()
    
    def show_rules(self):
        """显示游戏规则"""
        rules = """扫雷游戏规则：
        
        1. 游戏目标：在不触雷的情况下，揭开所有非地雷的格子。
        
        2. 操作方法：
           - 左键点击：揭开格子
           - 右键点击：标记/取消标记地雷（插旗）
        
        3. 数字含义：每个数字表示周围8个格子中的地雷数量。
        
        4. 游戏技巧：
           - 从数字推断周围地雷位置
           - 使用右键标记确定的地雷
           - 空白格子会自动展开
        
        5. 胜利条件：揭开所有非地雷格子。
        6. 失败条件：点击到地雷格子。
        
        快捷键说明：
        - F1/F2/F3: 切换难度
        - F4: 自定义难度
        - F5/ESC: 重新开始游戏
        - 空格键: 切换标记模式
        - 方向键: 移动选择
        - 回车键: 揭开选中格子
        - Delete键: 清除所有标记
        - 数字键1-8: 快速标记数字"""
        
        messagebox.showinfo("游戏规则", rules)
    
    def show_shortcut_help(self):
        """显示快捷键帮助"""
        shortcuts = """快捷键列表：
        
        游戏操作：
        - F5 或 ESC: 重新开始游戏
        - 空格键: 切换标记模式
        - 回车键: 揭开选中格子
        - Delete键: 清除所有标记
        - 方向键: 在格子间移动选择
        - 数字键1-8: 快速标记数字
        
        难度设置：
        - F1: 简单难度 (9×9, 10个雷)
        - F2: 中等难度 (16×16, 40个雷)
        - F3: 困难难度 (16×30, 99个雷)
        - F4: 自定义难度
        
        其他功能：
        - F12: 显示此帮助
        - Ctrl+I: 显示关于信息
        - Alt+F4: 退出游戏
        
        鼠标操作：
        - 左键点击: 揭开格子
        - 右键点击: 标记/取消标记地雷"""
        
        messagebox.showinfo("快捷键帮助", shortcuts)
    
    def show_about(self):
        """显示关于信息"""
        about_text = f"""扫雷游戏 (Windows 7 风格)
        
        当前难度：{self.current_difficulty}
        棋盘大小：{self.rows} × {self.cols}
        地雷数量：{self.mines_count}
        
        使用Python和Tkinter开发
        支持多种难度级别和自定义设置
        提供完整的快捷键支持
        
        版本：{self.app_version}"""

        
        messagebox.showinfo("关于", about_text)

if __name__ == "__main__":
    root = tk.Tk()
    # 尝试设置字体，如果系统没有Digital-7则使用默认
    try:
        from tkinter import font
        font.families()
    except:
        pass
        
    game = Minesweeper(root)
    root.mainloop()
