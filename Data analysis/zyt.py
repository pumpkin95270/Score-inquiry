import streamlit as st
import pandas as pd
import numpy as np


def main():
    st.title('Streamlit 应用示例')

    # 创建一个 DataFrame
    data = {'A': np.random.randn(50),
            'B': np.random.rand(50)}
    df = pd.DataFrame(data)

    # 在 Streamlit 中显示 DataFrame
    st.write('显示 DataFrame:')
    st.write(df)


if __name__ == '__main__':
    main()





import streamlit as st
import pandas as pd

def main():
    st.title('在 Streamlit 中显示 CSV 文件')

    # 通过 Streamlit 组件上传文件
    uploaded_file = st.file_uploader("上传 CSV 文件", type=['csv'])

    if uploaded_file is not None:
        # 使用 Pandas 读取上传的 CSV 文件
        df = pd.read_csv(uploaded_file)

        # 显示前 10000 行数据
        st.write('显示前 10000 行数据:')
        st.write(df.head(10000))

if __name__ == '__main__':
    main()










import streamlit as st
import pandas as pd

def main():
    st.title('在 Streamlit 中删除列并显示 CSV 数据')

    # 通过 Streamlit 组件上传文件
    uploaded_file = st.file_uploader("上传 CSV 文件", type=['csv'])

    if uploaded_file is not None:
        # 使用 Pandas 读取上传的 CSV 文件
        df = pd.read_csv(uploaded_file)

        # 删除指定列
        if "lastLearnTime" in df.columns:
            df.drop(columns="lastLearnTime", inplace=True)

        # 显示前 10000 行数据
        st.write('显示前 10000 行数据:')
        st.write(df.head(10000))

if __name__ == '__main__':
    main()

import streamlit as st
import pandas as pd


def main():
    st.title('在 Streamlit 中执行去重和重置索引')

    # 通过 Streamlit 组件上传文件
    uploaded_file = st.file_uploader("上传 CSV 文件", type=['csv'])

    if uploaded_file is not None:
        # 使用 Pandas 读取上传的 CSV 文件
        df = pd.read_csv(uploaded_file)

        # 执行去重操作
        df.drop_duplicates(keep="first", inplace=True)

        # 重置索引
        df.reset_index(drop=True, inplace=True)

        # 显示处理后的数据
        st.write('处理后的数据:')
        st.write(df)


if __name__ == '__main__':
    main()



import streamlit as st
import pandas as pd

def main():
    st.title('在 Streamlit 中显示数据信息和唯一值')

    # 通过 Streamlit 组件上传文件
    uploaded_file = st.file_uploader("上传 CSV 文件", type=['csv'])

    if uploaded_file is not None:
        # 使用 Pandas 读取上传的 CSV 文件
        df = pd.read_csv(uploaded_file)

        # 显示数据信息
        st.write('数据信息:')
        st.write(df.info())

        # 显示唯一值
        st.write('role 列的唯一值:')
        st.write(df['role'].unique())

if __name__ == '__main__':
    main()




import streamlit as st

class Member:
    def __init__(self, userId, orderId):
        self.userId = userId
        self.orderId = orderId

class Student(Member):
    def __init__(self, userId, orderId):
        super().__init__(userId, orderId)
        self.role = "Student"

class Teacher(Member):
    def __init__(self, userId, orderId):
        super().__init__(userId, orderId)
        self.role = "Teacher"

def main():
    st.title('在 Streamlit 中显示类的基本信息和角色')

    # 示例数据
    class_members = [
        Student("4", 0),
        Student("1161", 141),
        Teacher("3", 0),
        Teacher("975", 0)
    ]

    # 提取基本信息和角色并在 Streamlit 中显示
    for member in class_members:
        st.write(f"使用者: {member.userId}, 顺序: {member.orderId}")
        if isinstance(member, Student):
            st.write(f"角色: {member.role}")
        elif isinstance(member, Teacher):
            st.write(f"角色: {member.role}")
        st.write("---")

if __name__ == '__main__':
    main()


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data(file_path):
    # 读取CSV文件
    df = pd.read_csv(file_path)

    # 将时间字符串转换为datetime格式
    df['updatedTime'] = pd.to_datetime(df['updatedTime'])
    df['createdTime'] = pd.to_datetime(df['createdTime'])

    # 提取时间信息，例如年份和月份
    df['updatedYear'] = df['updatedTime'].dt.year
    df['updatedMonth'] = df['updatedTime'].dt.month
    df['createdYear'] = df['createdTime'].dt.year
    df['createdMonth'] = df['createdTime'].dt.month

    return df

def main():
    st.title('时间统计信息')

    file_path = r'D:\10\classroom_member.csv'
    df = load_data(file_path)

    # 统计更新时间和创建时间的数量
    update_counts = df.groupby(['updatedYear', 'updatedMonth']).size().unstack(fill_value=0)
    create_counts = df.groupby(['createdYear', 'createdMonth']).size().unstack(fill_value=0)

    # 绘制树状统计图
    st.subheader('更新时间统计')
    st.bar_chart(update_counts)

    st.subheader('创建时间统计')
    st.bar_chart(create_counts)

if __name__ == '__main__':
    main()



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data(file_path):
    # 读取Excel文件
    df = pd.read_csv(file_path)

    # 将日期列转换为datetime类型
    df['lastLearnTime'] = pd.to_datetime(df['lastLearnTime'])
    df['learnedNum'] = pd.to_datetime(df['learnedNum'])

    return df

def main():
    st.title('学习时间统计')

    file_path = r'D:\10\classroom_member.csv'
    df = load_data(file_path)

    # 设置图形大小
    fig, ax = plt.subplots(figsize=(10, 6))

    # 绘制折线图
    ax.plot(df['lastLearnTime'], label='lastLearnTime')
    ax.plot(df['learnedNum'], label='learnedNum')

    # 添加图例
    ax.legend()

    # 添加标题和标签
    ax.set_title('Last Learned Time vs Learned Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Time')

    # 自动调整日期显示格式
    fig.autofmt_xdate()

    # 显示图形
    st.pyplot(fig)

if __name__ == '__main__':
    main()