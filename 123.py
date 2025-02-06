import streamlit as st
import random

# 设置页面标题
st.title('猜数字游戏')

# 游戏逻辑
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0

# 输入框，让用户猜数字
user_guess = st.number_input('请输入一个1到100之间的数字:', min_value=1, max_value=100)

# 按钮点击事件
if st.button('提交'):
    st.session_state.attempts += 1
    if user_guess < st.session_state.number:
        st.write("略略略、你猜的数字真的是小了！")
    elif user_guess > st.session_state.number:
        st.write("哼、你猜的数字太大了！")
    else:
        st.write(f"恭喜你宝宝，猜对了！你猜了 {st.session_state.attempts} 次！")
        st.session_state.number = random.randint(1, 100)  # 重新生成一个新的数字
        st.session_state.attempts = 0  # 重置尝试次数

# 显示尝试次数
st.write(f"你已经尝试了 {st.session_state.attempts} 次")
