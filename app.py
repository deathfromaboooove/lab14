import streamlit as st
import matplotlib.pyplot as plt




# Данные для каждого региона
regions = ['Казахстан', 'Кыргызстан', 'Таджикистан', 'Узбекистан']
kaz_values = [0.0737473506983265, 0.044529239425859325, 0.07208697980276833, 0.09025550050680399]
kgz_values = [0.1875365079274166, 0.21059007745097164, 0.19581301002148638, 0.19449654750600165]
tjk_values = [0.13234311608076732, 0.11086727498562164, 0.19598527440470287, 0.23921461895440915]
uzb_values = [0.09872602667454446, 0.12482079148104783, 0.1033934827101725, 0.16342414956949367]

# Годы для оси X
years = [2014, 2015, 2016, 2017]


st.set_page_config(
    page_title='Продовольственная безопасность в Центральной Азии',
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Создание заголовка приложения
st.title('Интерактивный график трендов продовольственной безопасности стран Центральной Азии')
st.write('Это интерактивное веб-приложение позволяет изучать тренды продовольственной безопасности в странах Центральной Азии. Выберите регион из списка ниже, чтобы увидеть соответствующий график.')

# Добавление интерактивных элементов веб-приложения
selected_region = st.sidebar.selectbox('Выберите регион', regions)

# Отображение графика в зависимости от выбранного региона
if selected_region == 'Казахстан':
    st.header('График для выбранного региона: Казахстан')
    st.line_chart(dict(zip(years, kaz_values)), use_container_width=True)
elif selected_region == 'Кыргызстан':
    st.header('График для выбранного региона: Кыргызстан')
    st.line_chart(dict(zip(years, kgz_values)), use_container_width=True)
elif selected_region == 'Таджикистан':
    st.header('График для выбранного региона: Таджикистан')
    st.line_chart(dict(zip(years, tjk_values)), use_container_width=True)
elif selected_region == 'Узбекистан':
    st.header('График для выбранного региона: Узбекистан')
    st.line_chart(dict(zip(years, uzb_values)), use_container_width=True)

# Создаем заголовок для графика всех стран
st.subheader('График для всех стран')

# Отображение графика для всех стран
all_countries_chart = st.line_chart({
    'Казахстан': kaz_values,
    'Кыргызстан': kgz_values,
    'Таджикистан': tjk_values,
    'Узбекистан': uzb_values
} )

# Добавим возможность выбора цветовой схемы и размера графиков
color_scheme = st.sidebar.selectbox('Выберите цветовую схему', ['По умолчанию', 'Темная', 'Светлая'])
if color_scheme == 'Темная':
    plt.style.use('dark_background')
elif color_scheme == 'Светлая':
    plt.style.use('default')

st.write('Лабораторная работа 14. Выполнил Амин Райымбек, 22-07.')
