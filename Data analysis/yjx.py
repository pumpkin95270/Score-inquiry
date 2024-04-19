import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 读取大数据文件
data = pd.read_csv('D:\Code\Filtered_data.csv')

# 计算平均分、合格分数和各个分数线占比
average_score = data['score'].mean()
passing_score = data[data['score'] >= 60]['score'].count() / data['score'].count() * 100
grade_distribution = data['score'].value_counts(normalize=True) * 100

# 计算活跃度
data['active_time'] = data['updateTime'] - data['beginTime']

# 设置下拉菜单
menu1 = ['所有试卷', 'id']
menu2 = ['各个分数线占比', '合格分数', '活跃度', '平均分','指定id分数','指定id活跃度']
selection1 = st.sidebar.selectbox('选择试卷类型', menu1)
selection2 = st.sidebar.selectbox('选择数据类型', menu2)

# 绘制关系图
if selection1 == '所有试卷':
    if selection2 == '平均分':
        st.write(f'平均值：{average_score}')
    elif selection2 == '合格分数':
        st.write(f'合格分数： {passing_score}')
    elif selection2 == '活跃度':
        st.line_chart(data['active_time'])
    elif selection2 =='指定id分数':
        st.write(f'请选择试卷类型为id')
    elif selection2 =='指定id活跃度':
        st.write(f'请选择试卷类型为id')
    else:
        st.bar_chart(grade_distribution)
else:
    # 获取id列表
    id_input = st.selectbox('请输入id号', data['id'].unique())

    # 创建第二个下拉菜单，用于选择“分数”或“活跃度”
    option = st.selectbox('请选择查看选项', ['分数', '活跃度'])

    # 根据选择的选项展示相应的信息
    if option == '分数':
        st.write(f'ID为{id_input}的分数是：{data[data["id"] == id_input]["score"].values[0]}')
    elif option == '活跃度':
        st.write(f'ID为{id_input}的活跃度是：{data[data["id"] == id_input]["active_time"].values[0]}')