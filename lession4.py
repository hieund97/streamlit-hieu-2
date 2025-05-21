

import streamlit as st

import time


st.title("Kiểm tra")

name  = st.text_input("Nhập tên vào đây: ")

my_bar = st.progress(0)

if st.button("Kiểm tra độ dài tên"):
    st.write(len(name))
    
"""
1. Tạo 1 nút bấm
2. Sau khi bấm nút hiển thị bóng bay và 1 chữ "Chúc mừng" nền màu xanh lá cây


"""

if st.button("Click"):
    st.balloons()
    st.success("Chúc mừng bạn đã bấm nút   ")


