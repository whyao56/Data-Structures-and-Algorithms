# 数据结构说明：
# 1. 使用列表（list）存储所有待办事项，每个待办是一个字典（dict）
# 2. 字典包含：title(标题), priority(优先级), due_date(截止日期), completed(完成状态), completed_at(完成时间)
# 3. 为什么这样设计：
#    - 列表：有序存储，保持添加顺序，支持索引访问
#    - 字典：键值对清晰，便于通过字段名访问数据，易于理解和维护
#    - 使用列表+字典的组合，适合小规模数据，代码简单直观
#
# 如果数据量达到100万：
# 1. 使用数据库（如SQLite或MySQL）替代JSON文件存储
# 2. 添加索引（如优先级、完成状态）提高查询效率
# 3. 分页加载，避免一次性加载全部数据
# 4. 使用缓存机制，减少数据库访问
# 5. 考虑使用NoSQL数据库（如MongoDB）存储文档型数据


import json
import os
from datetime import datetime


def main():
    storage_file = "todos.json"

    # 如果文件存在，加载数据
    if os.path.exists(storage_file):
        try:
            with open(storage_file, "r", encoding="utf-8") as f:
                todos = json.load(f)
            if not isinstance(todos, list):
                print("数据格式错误，重新初始化")
                todos = []

            elif len(todos) > 0 and not isinstance(todos[0], dict):
                print("数据格式错误，重新初始化")
                todos = []

            else:
                print("已加载已保存的待办")
        except:
            print("读取数据错误，重新初始化")
            todos = []

    else:
        todos = []  # 存储待办事项的列表

    print("=" * 40)
    print("待办事项管理系统")
    print("=" * 40)

    while True:
        print("\n1. 添加待办")
        print("2. 查看待办")
        print("3. 标记完成")
        print("4. 查看已完成待办")
        print("5. 退出")

        choice = input("请选择：").strip()

        if choice == "1":
            # 添加待办
            title = input("标题：")
            # 校验：标题不为空
            if not title:
                print("标题不能为空")
                continue

            # 校验：优先级
            try:
                priority = int(input("优先级（1-5）："))
                if not (1 <= priority <= 5):
                    print("优先级必须在1-5之间")
                    continue
            except ValueError:
                print("优先级必须是整数")
                continue

            due_date = input("截止日期（YYYY-MM-DD）")

            # 创建一个待办字典
            todo = {
                "title": title,
                "priority": priority,
                "due_date": due_date,
                "completed": False,  # 新增：完成状态
                "completed_at": None  # 新增：完成时间
            }

            todos.append(todo)  # 添加到列表

            # 保存到文件
            with open(storage_file, "w", encoding="utf-8") as f:
                json.dump(todos, f, ensure_ascii=False, indent=2)

            print(f"已添加：{title}")


        elif choice == "2":
            # 查看待办：显示未完成的
            unfinished = [t for t in todos if not t["completed"]]

            if not unfinished:
                print("暂无未完成的待办")
            else:
                # 按优先级排序（数字越小越靠前）
                sorted_todos = sorted(unfinished, key=lambda x: (x["priority"], x["title"]))


                print("\n未完成的待办（按优先级排序）：")
                print("-" * 70)
                for i, todo in enumerate(sorted_todos, 1):
                    print(f"{i}. {todo['title']} | 优先级：{todo['priority']} | 截止：{todo['due_date']}")
                print("-" * 70)
                print(f"共 {len(sorted_todos)} 项未完成")

        elif choice == "3":
            # # 标记完成 - 按标题
            # title = input("请输入要标记完成的待办标题：").strip()
            #
            # # 查看未完成中匹配的待办
            # found = None
            # for todo in todos:
            #     if todo["title"] == title and not todo["completed"]:
            #         found = todo
            #         break
            #
            # if found:
            #     found["completed"] = True
            #     # 保存到文件 - 注意保存整个 todos 列表
            #     with open(storage_file, "w", encoding="utf-8") as f:
            #         json.dump(todos, f, ensure_ascii=False, indent=2)
            #     print(f"已完成：{title}")
            # else:
            #     print(f"未找到标题为 '{title}' 的未完成待办")


            # 标记完成 - 按序号
            # 先显示所有未完成的待办
            unfinished = [t for t in todos if not t["completed"]]

            if not unfinished:
                print("没有未完成的待办需要标记")
                continue

            # 显示待办列表供选择
            sorted_todos = sorted(unfinished, key = lambda x: (x["priority"], x["title"]))
            print("\n选择要标记完成的待办：")
            for i, todo in enumerate(sorted_todos, 1):
                print(f"{i}. {todo['title']} | 优先级：{todo['priority']} | 截止：{todo['due_date']}")

            try:
                num = int(input("请输入序号；"))
                if 1 <= num <= len(sorted_todos):
                    todo = sorted_todos[num - 1]
                    todo["completed"] = True
                    todo["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    print(f"已完成：{sorted_todos[num - 1]['title']}")
                    with open(storage_file, "w", encoding="utf-8") as f:
                        json.dump(todos, f, ensure_ascii=False, indent=2)
                else:
                    print("序号不存在")

            except ValueError:
                print("输入错误，请输入有效数字")


        elif choice == "4":
            # 查看已完成待办
            finished = [t for t in todos if t["completed"]]

            if not finished:
                print("暂无已完成的待办")
            else:
                # 按完成时间顺序显示（最近完成的排在最前）
                sorted_finished = sorted(finished, key=lambda x: x.get("completed_at") or "", reverse=True)  # 用 x.get("completed_at") 避免 KeyError，or "" 把 None 转成空字符串（空串会排到最后）。

                print("\n已完成的待办（按完成时间排序）：")
                print("-" * 70)
                for i, todo in enumerate(sorted_finished, 1):
                    print(f"{i}. {todo['title']} | 优先级：{todo['priority']} | 截止：{todo['due_date']} | 完成于{todo['completed_at']}")
                print("-" * 70)
                print(f"共 {len(sorted_finished)} 项已完成")


        elif choice == "5":
            print("再见！")
            break


        else:
            print("无效选项")

if __name__ == "__main__":
    main()
