import numpy as np

# Fungsi untuk menghitung Euclidean distance
def euclidean_distance(x, y):
    return np.sqrt(np.sum((x - y) ** 2))

# Fungsi untuk menghitung Manhattan distance

def manhattan_distance(x, y):
    return np.sum(np.abs(x - y))

# Data dari tabel
data = [
    ["excellent", 3, 80, "B"],
    ["fair", 2, 50, "D"],
    ["good", 1, 90, "A"],
    ["excellent", 3, 75, "B"],
    ["fair", 2, 82, "B"],
    ["good", 1, 65, "C"]
]

# Konversi data keaktifan ke dalam bentuk angka
keaktifan_mapping = {"excellent": 3, "fair": 2, "good": 1}
for row in data:
    row[1] = keaktifan_mapping[row[0]]

# Hitung jumlah data dan atribut
num_data = len(data)
num_attributes = len(data[0])

# Matriks dissimilarity campuran
dissimilarity_matrix = np.zeros((num_data, num_data))

# Hitung jarak untuk setiap pasangan data
for i in range(num_data):
    for j in range(num_data):
        dissimilarity = 0
        for k in range(1, num_attributes):  # Mulai dari indeks 1 untuk mengabaikan atribut nominal
            if k == 1:
                dissimilarity += euclidean_distance(data[i][k], data[j][k])
            elif k == 2:
                dissimilarity += manhattan_distance(data[i][k], data[j][k])
            else:
                dissimilarity += 1 if data[i][k] != data[j][k] else 0
        dissimilarity_matrix[i][j] = dissimilarity

# Tampilkan matriks dissimilarity
print("Matriks Dissimilarity Campuran:")
#print(dissimilarity_matrix)
print(manhattan_distance(x,y))