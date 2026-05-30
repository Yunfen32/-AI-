#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LifeMonster 桌面应用入口 — CustomTkinter + 后台 Flask API"""
import sys
import os
import threading
import time
import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import customtkinter as ctk
from src.ui.login_window import LoginWindow
from src.ui.main_window import MainWindow
from src.data.database_config import get_database_manager
from src.services.auth_service import auth_manager
from src.utils.logger import get_logger


FLASK_URL = "http://127.0.0.1:5000"


def start_flask():
    """在后台线程中启动 Flask API 服务器"""
    from flask_api import app
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)


def wait_for_flask(timeout=10):
    """等待 Flask 服务就绪"""
    start = time.time()
    while time.time() - start < timeout:
        try:
            resp = requests.get(f"{FLASK_URL}/api/health", timeout=2)
            if resp.status_code == 200:
                return True
        except Exception:
            pass
        time.sleep(0.3)
    return False


def main():
    logger = get_logger()
    logger.info("LifeMonster 启动中...")

    # 初始化数据库
    get_database_manager()
    logger.info("数据库初始化完成")

    # 后台启动 Flask
    
    
    flask_thread = threading.Thread(target=start_flask, daemon=True)
    flask_thread.start()
    logger.info("Flask API 后台线程已启动")

    # 等待 Flask 就绪
    if not wait_for_flask():
        logger.warning("Flask API 启动超时，部分功能可能不可用")

    # 启动 CustomTkinter 桌面界面
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")

    root = ctk.CTk()
    root.title("LifeMonster - 生活导师")

    # 窗口尺寸
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    w, h = 1400, 900
    x = (sw - w) // 2
    y = (sh - h) // 2
    root.geometry(f"{w}x{h}+{x}+{y}")
    root.minsize(1200, 760)

    # 登录成功回调：同步 auth 状态，销毁登录窗口，创建主窗口
    def on_login_success(user):
        auth_manager.login(user)
        for widget in root.winfo_children():
            widget.destroy()
        MainWindow(root, on_logout=show_login)

    # 登出回调：返回登录界面
    def show_login():
        for widget in root.winfo_children():
            widget.destroy()
        LoginWindow(root, on_login_success=on_login_success)

    # 显示登录窗口
    LoginWindow(root, on_login_success=on_login_success)

    try:
        root.mainloop()
    except KeyboardInterrupt:
        logger.info("用户中断，应用退出")
    except Exception as e:
        logger.error(f"应用异常退出: {e}")
        raise


if __name__ == "__main__":
    main()
