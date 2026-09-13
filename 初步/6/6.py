import easygui # import是用于导入模块的关键字，easygui是一个模块的名字
easygui.msgbox("Hello, World!") # 显示一个消息框，消息框的内容是Hello, World!】

# 输入
name = easygui.enterbox("请输入您的姓名: ") #enterbox是一个输入框，用户可以在输入框中输入内容
easygui.msgbox("您好, " + name + "!")

choice = easygui.buttonbox("请选择您的性别:", choices=["男", "女"])  # buttonbox是一个按钮框，用户可以通过点击按钮来选择选项
easygui.msgbox("您选择的性别是: " + choice)

choice = easygui.choicebox("请选择您的爱好:", choices=["阅读", "运动", "音乐", "旅行"]) #choicebox是一个选择框，用户可以从给定的选项中选择一个
easygui.msgbox("您选择的爱好是: " + choice)
