from simpson import*
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2*x**2 + 5*x + 10

def exact_integral(a, b):
    # Fungsi eksak untuk menghitung integral
    return (2/3)*(b**3) + (5/2)*(b**2) + 10*b - ((2/3)*(a**3) + (5/2)*(a**2) + 10*a)

a = float(input('batas bawah = '))
b = float(input('batas atas = '))
n = int(input('jumlah grid = '))

# Menghitung nilai x dan y untuk plot fungsi asli
x_values = np.linspace(a, b, 1000)
y_values = f(x_values)

# Menghitung integral eksak
exact_result = exact_integral(a, b)

# Menghitung integral menggunakan metode trapezoid
integral = simpson(f, a, b, n)

# Menampilkan hasil integral
print('Integral Eksak = ', exact_result)
print('Integral (Simpson) = ', integral)

# Memplot grafik fungsi asli dan area di bawah kurva
plt.plot(x_values, y_values, label='Eksak')
plt.fill_between(x_values, y_values, color='gray', alpha=0.2, label='Area di bawah kurva')

# Plot garis trapezoid
x_simpson = np.linspace(a, b, n+1)
y_simpson = f(x_simpson)
plt.plot(x_simpson, y_simpson, '-', label='Simpson')

# Menandai titik ujung trapezoid
plt.scatter([a, b], [f(a), f(b)], color='red', zorder=5)

# Menambahkan label pada pinggir grafik
plt.annotate(f'Eksak = {exact_result:.2f}', xy=(1, 0.5), xycoords='axes fraction', ha='left', va='center', color='blue')
plt.annotate(f'Simpson = {integral:.2f}', xy=(1, 0.45), xycoords='axes fraction', ha='left', va='center', color='orange')

plt.title('Metode Simpson untuk Integral Numerik')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
