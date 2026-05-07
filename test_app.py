#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试应用程序功能
"""

import sys
import os
import traceback

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_modules():
    """测试所有模块导入"""
    print("=" * 60)
    print("测试 LifeMonster 应用程序模块")
    print("=" * 60)
    
    modules_to_test = [
        ("customtkinter", "UI框架"),
        ("PIL.Image", "图像处理"),
        ("src.utils.logger", "日志模块"),
        ("src.data.database_config", "数据库配置"),
        ("src.services.auth_service", "认证服务"),
        ("src.utils.user_state", "用户状态"),
        ("src.ui.theme", "主题配置"),
        ("src.ui.login_window_fixed", "登录窗口"),
        ("src.ui.main_window", "主窗口"),
        ("src.ui.home_tab", "首页"),
        ("src.ui.dashboard_tab", "仪表盘"),
        ("src.ui.chat_tab", "AI助手"),
        ("src.ui.suggestion_tab", "智能建议"),
        ("src.ui.diary_tab", "我的日记"),
        ("src.ui.profile_tab", "个人中心")
    ]
    
    success_count = 0
    
    for module_path, description in modules_to_test:
        try:
            if "." in module_path:
                # 处理子模块导入
                parts = module_path.split(".")
                module_name = parts[0]
                for part in parts[1:]:
                    module_name += "." + part
                __import__(module_name)
            else:
                __import__(module_path)
            
            print(f"OK - {module_path:<30} - {description}")
            success_count += 1
            
        except Exception as e:
            print(f"ERROR - {module_path:<30} - {description}")
            print(f"  错误: {e}")
    
    print("=" * 60)
    print(f"测试结果: {success_count}/{len(modules_to_test)} 个模块导入成功")
    
    if success_count == len(modules_to_test):
        print("✓ 所有模块导入成功，应用程序可以正常运行")
        return True
    else:
        print("⚠ 部分模块导入失败，应用程序可能无法完全正常运行")
        return False

def test_app_creation():
    """测试应用程序创建"""
    print("\n" + "=" * 60)
    print("测试应用程序创建")
    print("=" * 60)
    
    try:
        import customtkinter as ctk
        
        # 创建测试窗口
        root = ctk.CTk()
        root.withdraw()  # 隐藏窗口
        
        # 测试登录窗口
        from src.ui.login_window_fixed import LoginWindowFixed
        
        def dummy_callback(user_info):
            print("登录成功回调触发")
        
        login_window = LoginWindowFixed(root, on_login_success=dummy_callback)
        print("OK - 登录窗口创建成功")
        
        # 测试主窗口
        from src.ui.main_window import MainWindow
        
        def dummy_logout():
            print("登出回调触发")
        
        main_window = MainWindow(root, on_logout=dummy_logout)
        print("OK - 主窗口创建成功")
        
        root.destroy()
        print("OK - 应用程序创建测试完成")
        return True
        
    except Exception as e:
        print(f"✗ 应用程序创建失败: {e}")
        traceback.print_exc()
        return False

def test_resource_links():
    """测试资源链接功能"""
    print("\n" + "=" * 60)
    print("测试资源链接功能")
    print("=" * 60)
    
    try:
        import customtkinter as ctk
        from src.ui.home_tab import HomeTab
        
        root = ctk.CTk()
        root.withdraw()
        
        home_tab = HomeTab(root)
        
        # 测试目标加载
        goal = home_tab.load_goal()
        print(f"用户目标: {goal}")
        
        # 测试资源链接生成
        import urllib.parse
        
        if "还没有设置目标" in goal:
            search_keyword = "学习提升"
        else:
            search_keyword = goal.split(" - ")[0] if " - " in goal else goal
        
        encoded_keyword = urllib.parse.quote(search_keyword)
        
        resources = [
            ("哔哩哔哩", f"https://www.bilibili.com/search?keyword={encoded_keyword}"),
            ("抖音", f"https://www.douyin.com/search/{encoded_keyword}"),
            ("Edge浏览器", f"https://www.bing.com/search?q={encoded_keyword}"),
            ("GitHub", f"https://github.com/search?q={encoded_keyword}+tutorial")
        ]
        
        for name, url in resources:
            print(f"OK - {name}: {url}")
        
        root.destroy()
        print("OK - 资源链接功能测试完成")
        return True
        
    except Exception as e:
        print(f"✗ 资源链接功能测试失败: {e}")
        traceback.print_exc()
        return False

def main():
    """主测试函数"""
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print("LifeMonster 应用程序功能测试")
    print("=" * 60)
    
    # 测试模块导入
    modules_ok = test_modules()
    
    # 测试应用程序创建
    if modules_ok:
        app_ok = test_app_creation()
    else:
        app_ok = False
        print("跳过应用程序创建测试（模块导入失败）")
    
    # 测试资源链接
    resource_ok = test_resource_links()
    
    print("\n" + "=" * 60)
    print("测试总结")
    print("=" * 60)
    
    if modules_ok and app_ok and resource_ok:
        print("SUCCESS - 所有测试通过！应用程序可以正常运行")
        print("\n启动应用程序命令:")
        print("python app_final.py")
    else:
        print("WARNING - 部分测试失败，应用程序可能无法完全正常运行")
        print("\n建议:")
        if not modules_ok:
            print("- 检查依赖安装: pip install -r requirements.txt")
        if not app_ok:
            print("- 检查应用程序代码错误")
        if not resource_ok:
            print("- 检查资源链接配置")
    
    print("=" * 60)

if __name__ == "__main__":
    main()