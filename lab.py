import matplotlib.pyplot as plt

# Данные для каждого региона
regions = ['Казахстан', 'Кыргызстан', 'Таджикистан', 'Узбекистан']
kaz_values = [0.0737473506983265, 0.044529239425859325, 0.07208697980276833, 0.09025550050680399]
kgz_values = [0.1875365079274166, 0.21059007745097164, 0.19581301002148638, 0.19449654750600165]
tjk_values = [0.13234311608076732, 0.11086727498562164, 0.19598527440470287, 0.23921461895440915]
uzb_values = [0.09872602667454446, 0.12482079148104783, 0.1033934827101725, 0.16342414956949367]

# Построение линейных графиков с улучшениями
plt.figure(figsize=(10, 6))

plt.plot(regions, kaz_values, marker='o', label='Казахстан', linestyle='-', color='blue')
plt.plot(regions, kgz_values, marker='s', label='Кыргызстан', linestyle='--', color='green')
plt.plot(regions, tjk_values, marker='^', label='Таджикистан', linestyle='-.', color='orange')
plt.plot(regions, uzb_values, marker='d', label='Узбекистан', linestyle=':', color='red')

plt.title('Вероятности для разных регионов Центральной Азии')
plt.xlabel('Регион')
plt.ylabel('Вероятность')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Поворот подписей оси X для лучшей читаемости

plt.tight_layout()
plt.show()
