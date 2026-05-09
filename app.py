import customtkinter as ctk
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.ui.main_window import MainWindow
from src.ui.login_window import LoginWindow
from src.utils.logger import get_logger

class LifeMonsterApp:
    def __init__(self):
        self.logger = get_logger()
        self.logger.info("启动 LifeMonster 应用")
        
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        self.root = ctk.CTk()
        self.root.title("LifeMonster - 生活导师")
        
        try:
            logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "logo", "logo.png")
            if os.path.exists(logo_path):
                from PIL import Image, ImageTk
                logo_image = Image.open(logo_path)
                logo_image = logo_image.resize((256, 256), Image.Resampling.LANCZOS)
                self.icon_photo = ImageTk.PhotoImage(logo_image)
                self.root.iconphoto(True, self.icon_photo)
        except Exception as e:
            self.logger.warning(f"设置应用图标失败: {e}")
        
        self.show_login()
    
    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        self.logger.info(f"屏幕尺寸: {screen_width}x{screen_height}, 窗口位置: {x},{y}")
    
    def show_login(self):
        self.login_window = LoginWindow(self.root, on_login_success=self.on_login)
    
    def on_login(self, user_info):
        username = user_info.get('username', '未知用户')
        self.logger.info(f"用户登录成功: {username}")
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.title("LifeMonster - 生活导师")
        
        # 自适应分辨率设置
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # 根据屏幕分辨率设置窗口大小
        if screen_width >= 1600:
            window_width, window_height = 1500, 900
        elif screen_width >= 1440:
            window_width, window_height = 1400, 900
        else:
            window_width, window_height = 1200, 800
        
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.minsize(1100, 700)  # 最小尺寸稍微减小以适应小屏幕
        self.root.resizable(True, True)
        self.center_window(window_width, window_height)

        self.main_window = MainWindow(self.root, on_logout=self.show_login)
    
    def run(self):
        self.logger.info("应用主循环启动")
        self.root.mainloop()

if __name__ == "__main__":
    try:
        app = LifeMonsterApp()
        print("应用启动成功，开始运行...")
        app.run()
    except KeyboardInterrupt:
        print("应用被用户中断")
    except ImportError as e:
        print(f"依赖包缺失: {e}")
        print("请检查 requirements.txt 并安装缺失的包")
    except Exception as e:
        print(f"应用启动失败: {e}")
        import traceback
        traceback.print_exc()
        
        # 尝试降级启动
        print("\n尝试降级启动...")
        try:
            import customtkinter as ctk
            root = ctk.CTk()
            root.title("LifeMonster - 紧急模式")
            root.geometry("400x200")
            
            error_frame = ctk.CTkFrame(root, fg_color="#F7F3EA")
            error_frame.pack(fill="both", expand=True, padx=20, pady=20)
            
            ctk.CTkLabel(error_frame, text="⚠️ 系统启动异常", 
                        font=("Microsoft YaHei", 18, "bold"),
                        text_color="#2F4638").pack(pady=10)
            
            ctk.CTkLabel(error_frame, text="应用程序遇到问题，但已进入安全模式",
                        font=("Microsoft YaHei", 12),
                        text_color="#7A8A80", wraplength=350).pack(pady=5)
            
            ctk.CTkLabel(error_frame, text=f"错误信息: {str(e)[:100]}...",
                        font=("Microsoft YaHei", 10),
                        text_color="#9BA89E").pack(pady=5)
            
            def open_manual_mode():
                try:
                    from src.ui.login_window import LoginWindow
                    for widget in root.winfo_children():
                        widget.destroy()
                    LoginWindow(root, lambda x: None)
                except:
                    messagebox.showerror("错误", "无法进入手动模式")
            
            ctk.CTkButton(error_frame, text="尝试手动启动",
                         command=open_manual_mode).pack(pady=10)
            
            root.mainloop()
        except Exception as fallback_error:
            print(f"降级启动也失败: {fallback_error}")
