import streamlit as st
import random

# 设置页面标题
st.title('猜数字游戏')

# 游戏逻辑
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 200)
    st.session_state.attempts = 0

# 使用 Markdown 结合 HTML 和 CSS 来创建带有背景图片和动画的按钮
st.markdown("""
    <style>
        .button-with-image {
            background-image: url('https://via.placeholder.com/150'); /* 设置按钮的背景图片 */
            background-size: cover;
            background-repeat: no-repeat;
            width: 300px;
            height: 100px;
            color: white;
            font-size: 18px;
            display: flex;
            justify-content: center;
            align-items: center;
            border: none;
            cursor: pointer;
            transition: transform 0.3s ease;  /* 添加按钮动画 */
        }
        .button-with-image:hover {
            transform: scale(1.1);  /* 鼠标悬停时放大按钮 */
            background-color: rgba(0, 0, 0, 0.4);  /* 增加半透明的背景色 */
        }
    </style>
    <button class="button-with-image">我就猜这个了嗷</button> <!-- 自定义按钮 -->
""", unsafe_allow_html=True)

# 输入框，让用户猜数字
user_guess = st.number_input('亲爱的同学，请输入一个1到200之间的数字吧:', min_value=1, max_value=200)

# 按钮点击事件
if st.button('我就猜这个了嗷'):
    st.session_state.attempts += 1
    if user_guess < st.session_state.number:
        st.write("你瞅你猜那玩意，数太小！")
    elif user_guess > st.session_state.number:
        st.write("你瞅瞅你，猜的数字太大了！")
    else:
        st.write(f"牛逼了，让你猜对了，回头让李明航给你发红包！你猜了 {st.session_state.attempts} 次！")
        st.session_state.number = random.randint(1, 200)  # 重新生成一个新的数字
        st.session_state.attempts = 0  # 重置尝试次数

# 显示尝试次数
st.write(f"你已经尝试了 {st.session_state.attempts} 次")
