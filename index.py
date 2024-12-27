import timeit

def brute_force_search(text, pattern):
    """
    Algoritma Brute Force untuk pencarian substring
    """
    n, m = len(text), len(pattern)
    comparisons = 0
    
    for i in range(n - m + 1):
        for j in range(m):
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
        else:
            return i, comparisons
    
    return -1, comparisons

def kmp_search(text, pattern):
    """
    Algoritma Knuth-Morris-Pratt untuk pencarian substring
    """
    def compute_lps(pattern):
        """
        Membuat Longest Proper Prefix which is also Suffix (LPS)
        """
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        comparisons = 0
        
        while i < m:
            comparisons += 1
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps, comparisons
    
    n, m = len(text), len(pattern)
    lps, prefix_comparisons = compute_lps(pattern)
    
    i = j = comparisons = 0
    while i < n:
        comparisons += 1
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            return i - j, comparisons + prefix_comparisons
        
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return -1, comparisons + prefix_comparisons

def measure_performance(text, pattern, iterations):
    """
    Mengukur performa dan efisiensi algoritma dengan beberapa iterasi
    """
    bf_times = []
    kmp_times = []
    bf_comparisons = []
    kmp_comparisons = []
    
    for i in range(iterations):
        bf_execution_time = timeit.timeit(lambda: brute_force_search(text, pattern), number=1)
        kmp_execution_time = timeit.timeit(lambda: kmp_search(text, pattern), number=1)
        
        bf_times.append(bf_execution_time)
        kmp_times.append(kmp_execution_time)
        
        bf_result, bf_comparison = brute_force_search(text, pattern)
        kmp_result, kmp_comparison = kmp_search(text, pattern)
        
        bf_comparisons.append(bf_comparison)
        kmp_comparisons.append(kmp_comparison)
        
        # Tampilkan hasil setiap iterasi
        print(f"\nIterasi ke-{i + 1}:")
        print(f"Brute Force - Waktu Eksekusi: {bf_execution_time:.8f} detik, Jumlah Perbandingan: {bf_comparison}")
        print(f"KMP - Waktu Eksekusi: {kmp_execution_time:.8f} detik, Jumlah Perbandingan: {kmp_comparison}")
    
    bf_avg_time = sum(bf_times) / iterations
    kmp_avg_time = sum(kmp_times) / iterations
    bf_avg_comparisons = sum(bf_comparisons) / iterations
    kmp_avg_comparisons = sum(kmp_comparisons) / iterations
    
    # Cetak hasil rata-rata
    print("\n--- Hasil Analisis Pencarian Substring ---")
    print(f"Substring Dicari: {pattern}")
    print(f"\nJumlah Iterasi: {iterations}")
    print("\nBrute Force:")
    print(f"Waktu Eksekusi Rata-rata: {bf_avg_time:.8f} detik")
    print(f"Jumlah Perbandingan Rata-rata: {bf_avg_comparisons}")
    
    print("\nKnuth-Morris-Pratt (KMP):")
    print(f"Waktu Eksekusi Rata-rata: {kmp_avg_time:.8f} detik")
    print(f"Jumlah Perbandingan Rata-rata: {kmp_avg_comparisons}")
    
    # Perbandingan
    print("\nPerbandingan Efisiensi:")
    if bf_avg_time < kmp_avg_time:
        print("Brute Force lebih cepat")
    elif kmp_avg_time < bf_avg_time:
        print("KMP lebih cepat")
    else:
        print("Kedua algoritma memiliki waktu eksekusi hampir sama")
    
    print(f"\nSelisih Waktu Eksekusi Rata-rata: {abs(bf_avg_time - kmp_avg_time):.8f} detik")
    print(f"Selisih Jumlah Perbandingan Rata-rata: {abs(bf_avg_comparisons - kmp_avg_comparisons)}")

def main():
    print("=== Analisis Perbandingan Algoritma Pencarian Substring ===")
    
    # Input dari pengguna
    text = 'word.txt'
    pattern = input("Masukkan substring yang ingin dicari: ")
    iterations = int(input("Masukkan jumlah iterasi yang diinginkan: "))
    
    # Lakukan pengukuran
    measure_performance(text, pattern, iterations)

# Jalankan program
main()