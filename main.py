import streamlit as st
import sys
from streamlit import cli as stcli
import pandas as pd
from ShapeCalculator import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle


def streamlit_figure_slide():
    figure = st.selectbox("Выберете фигуру",
                          ["Квадрат", "Круг", "Прямоугольник", "ромб", "параллелепипед", "куб", "трапеция",
                           "Треугольник", "Сфера", "Пирамида", "целиндр", "Конус"])
    if figure == 'Квадрат':
        st.image('photo/qwadro.png', width=240)
        x = st.number_input('Ведите длину стороны')

        st.title('Площадь квадрата равна')
        st.text(x * 2 * 2)

        if x != float(0.00) or int(0):
            fig, ax = plt.subplots(1)
            rect = patches.Rectangle((1, 2), x, x, facecolor='none', edgecolor='black', linewidth=2)
            ax.add_patch(rect)
            ax.set_xlim([-(x * 3), x + x * 3])
            ax.set_ylim([-(x * 3), x + x * 3])
            st.pyplot(fig)

    if figure == 'Круг':
        st.image('photo/Круг.png', width=240)

        x = st.number_input('Ведите диаметр')

        st.title('Площадь диаметра равна')
        st.text(x * 2)
        if x != float(0.00) or int(0):
            fig, ax = plt.subplots(1)
            circle = plt.Circle((1, 1), x, facecolor='none', edgecolor='black', linewidth=2)
            ax.add_patch(circle)
            ax.set_xlim([-(x * 3), x + x * 3])
            ax.set_ylim([-(x * 3), x + x * 3])
            st.pyplot(fig)

    if figure == 'Прямоугольник':
        st.image('photo/прямоугольник.png', width=240)

        x = st.number_input('Ведите длину стороны', key=None)
        y = st.number_input('Ведите длину стороны', key=1)
        st.title('Площадь прямоугольника равна')
        st.text(x * 2 * 2)

        if x != float(0.00) or int(0):
            fig, ax = plt.subplots(1)
            rect = patches.Rectangle((1, 2), x, y, facecolor='none', edgecolor='black', linewidth=2)
            ax.add_patch(rect)
            ax.set_xlim([-(x * 3), x + x * 3])
            ax.set_ylim([-(x * 3), x + x * 3])
            st.pyplot(fig)

    if figure == 'ромб':
        st.image('photo/ромб.png', width=240)
        x = st.number_input('Ведите длину стороны', key=None)
        y = st.number_input('Ведите длину стороны', key=1)
        st.title('Площадь ромба равна')
        st.text(x * 2 * 2)

        if x != float(0.00) or int(0):
            fig, ax = plt.subplots(1)
            rect = patches.Polygon(((0.5, 0.2), (0.7, 0.525), (0.5, 0.85), (0.3, 0.525)), facecolor='none', edgecolor='black', linewidth=2)
            ax.add_patch(rect)
            ax.set_xlim([-(x * 3), x + x * 3])
            ax.set_ylim([-(x * 3), x + x * 3])
            st.pyplot(fig)

    if figure == 'параллелепипед':
        st.image('photo/пара.png', width=240)
    if figure == 'куб':
        st.image('photo/cube.png', width=240)
    if figure == 'трапеция':
        st.image('photo/Trapezoid.png', width=240)
    if figure == 'Треугольник':
        st.image('photo/Triangle.png', width=240)

    if figure == 'Сфера':
        st.image('photo/scale.png', width=240)
        x = st.number_input('Ведите радиус')

        st.title('Площадь сферы равна')
        st.text(x)
        if x != float(0.00) or int(0):
            u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
            x = np.cos(u) * np.sin(v)
            y = np.sin(u) * np.sin(v)
            z = np.cos(v)
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_wireframe(x, y, z)

            st.pyplot(fig)

    if figure == 'Пирамида':
        st.image('photo/пирамида.png', width=240)
    if figure == 'Целиндр':
        st.image('photo/Cylinder.png', width=240)
    if figure == 'Конус':
        st.image('photo/конус.png', width=240)


def main():
    st.title('Геометрический калькулятор')

    streamlit_figure_slide()


if __name__ == '__main__':
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())

