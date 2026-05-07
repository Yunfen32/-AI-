#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LifeMonster 应用程序 - 最终修复版本
确保项目能够正常运行
"""

import customtkinter as ctk
import sys
import os
import traceback

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.utils.logger import get_logger

def main():
    """主函数 - 确保应用程序能够正常启动"""
    logger = get_logger()
    logger.info("启动 LifeMonster 应用程序")
    
    try:
        # 设置主题
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        # 创建主窗口
        root = ctk.CTk()
        root.title("LifeMonster - 生活导师")
        
        # 设置窗口大小和位置
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        if screen_width >= 1600:
            width, height = 1400, 800
        elif screen_width >= 1440:
            width, height = 1200, 700
        else:
            width, height = 1000, 600
        
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        
        root.geometry(f"{width}x{height}+{x}+{y}")
        root.minsize(800, 500)
        root.resizable(True, True)
        
        logger.info(f"窗口设置: {width}x{height}, 位置: {x},{y}")
        
        # 显示启动界面
        show_startup_screen(root, logger)
        
        # 启动主循环
        root.mainloop()
        
    except Exception as e:
        logger.error(f"应用程序启动失败: {e}")
        traceback.print_exc()
        
        # 显示错误界面
        show_error_screen(str(e))

def show_startup_screen(root, logger):
    """显示启动界面"""
    try:
        # 创建启动界面
        container = ctk.CTkFrame(root, fg_color="#F7F3EA")
        container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # 标题
        title_label = ctk.CTkLabel(
            container,
            text="LifeMonster",
            font=("Microsoft YaHei", 32, "bold"),
            text_color="#2F4638"
        )
        title_label.pack(pady=(40, 10))
        
        subtitle_label = ctk.CTkLabel(
            container,
            text="你的 AI 生活导师",
            font=("Microsoft YaHei", 16),
            text_color="#7A8A80"
        )
        subtitle_label.pack(pady=(0, 30))
        
        # 状态信息
        status_label = ctk.CTkLabel(
            container,
            text="正在加载应用程序...",
            font=("Microsoft YaHei", 14),
            text_color="#7A8A80"
        )
        status_label.pack(pady=20)
        
        # 进度条
        progress_bar = ctk.CTkProgressBar(container, width=300, height=8)
        progress_bar.pack(pady=10)
        progress_bar.set(0)
        
        # 功能说明
        features = [
            "✓ 登录/注册/游客模式",
            "✓ 首页任务管理",
            "✓ 数据仪表盘",
            "✓ AI助手对话",
            "✓ 智能建议",
            "✓ 我的日记",
            "✓ 个人中心"
        ]
        
        for feature in features:
            feature_label = ctk.CTkLabel(
                container,
                text=feature,
                font=("Microsoft YaHei", 12),
                text_color="#7A8A80"
            )
            feature_label.pack(pady=2)
        
        # 启动按钮
        def start_application():
            status_label.configure(text="正在启动应用程序...")
            progress_bar.set(0.5)
            
            # 延迟启动，确保界面显示
            root.after(1000, lambda: load_main_application(root, status_label, progress_bar))
        
        start_button = ctk.CTkButton(
            container,
            text="启动应用",
            font=("Microsoft YaHei", 14, "bold"),
            fg_color="#6B9B5F",
            hover_color="#5A8A4F",
            height=40,
            command=start_application
        )
        start_button.pack(pady=30)
        
        logger.info("启动界面显示成功")
        
    except Exception as e:
        logger.error(f"启动界面创建失败: {e}")
        raise

def load_main_application(root, status_label, progress_bar):
    """加载主应用程序"""
    try:
        status_label.configure(text="正在加载模块...")
        progress_bar.set(0.7)
        
        # 导入主应用程序模块
        from src.ui.main_window import MainWindow
        from src.ui.login_window_fixed import LoginWindowFixed
        
        status_label.configure(text="正在初始化界面...")
        progress_bar.set(0.9)
        
        # 清除启动界面
        for widget in root.winfo_children():
            widget.destroy()
        
        # 显示登录界面
        def on_login_success(user_info):
            # 清除登录界面
            for widget in root.winfo_children():
                widget.destroy()
            
            # 显示主界面
            try:
                main_window = MainWindow(root, on_logout=lambda: show_login())
                root.title(f"LifeMonster - {user_info.get('username', '用户')}")
            except Exception as e:
                show_error_screen(f"主界面加载失败: {e}")
        
        def show_login():
            # 清除当前界面
            for widget in root.winfo_children():
                widget.destroy()
            
            # 显示登录界面
            try:
                login_window = LoginWindowFixed(root, on_login_success=on_login_success)
            except Exception as e:
                show_error_screen(f"登录界面加载失败: {e}")
        
        # 显示登录界面
        show_login()
        
        progress_bar.set(1.0)
        
    except Exception as e:
        show_error_screen(f"应用程序加载失败: {e}")

def show_error_screen(error_message):
    """显示错误界面"""
    try:
        root = ctk.CTk()
        root.title("LifeMonster - 错误")
        root.geometry("500x400")
        
        # 居中显示
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - 500) // 2
        y = (screen_height - 400) // 2
        root.geometry(f"500x400+{x}+{y}")
        
        container = ctk.CTkFrame(root, fg_color="#F7F3EA")
        container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # 错误图标
        error_icon = ctk.CTkLabel(
            container,
            text="⚠️",
            font=("Segoe UI Emoji", 48)
        )
        error_icon.pack(pady=20)
        
        # 错误标题
        error_title = ctk.CTkLabel(
            container,
            text="应用程序启动失败",
            font=("Microsoft YaHei", 18, "bold"),
            text_color="#D32F2F"
        )
        error_title.pack(pady=10)
        
        # 错误信息
        error_msg = ctk.CTkLabel(
            container,
            text=error_message,
            font=("Microsoft YaHei", 12),
            text_color="#7A8A80",
            wraplength=400
        )
        error_msg.pack(pady=10)
        
        # 操作按钮
        buttons_frame = ctk.CTkFrame(container, fg_color="transparent")
        buttons_frame.pack(pady=20)
        
        retry_button = ctk.CTkButton(
            buttons_frame,
            text="重新启动",
            font=("Microsoft YaHei", 12),
            command=lambda: [root.destroy(), main()]
        )
        retry_button.pack(pady=5)
        
        exit_button = ctk.CTkButton(
            buttons_frame,
            text="退出",
            font=("Microsoft YaHei", 12),
            command=root.destroy
        )
        exit_button.pack(pady=5)
        
        root.mainloop()
        
    except Exception as e:
        print(f"错误界面创建失败: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    print("=" * 60)
    print("LifeMonster 应用程序启动")
    print("=" * 60)
    print("应用程序功能:")
    print("1. 登录/注册/游客模式")
    print("2. 首页任务管理")
    print("3. 数据仪表盘")
    print("4. AI助手对话")
    print("5. 智能建议")
    print("6. 我的日记")
    print("7. 个人中心")
    print("=" * 60)
    print("如果窗口没有显示，请检查任务栏或按Alt+Tab切换")
    print("=" * 60)
    
    main()