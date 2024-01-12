import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Specify the full path to the CSV file
file_path = r"D:\MACHINE LEARNING\Dicoding ML\Belajar Analisis Data dengan Python\submission_bike_sharing\dashboard\bike_sharing.csv"

# Load your dataset
bike_merge = pd.read_csv(file_path)

# Function to plot the seasonal analysis
def plot_seasonal_analysis():
    seasonal_data = bike_merge.groupby('season_daily')['cnt_daily'].mean()
    season_names = ['Spring', 'Summer', 'Fall', 'Winter']

    fig, ax = plt.subplots()
    ax.bar(season_names, seasonal_data)
    ax.set_xlabel('Musim')
    ax.set_ylabel('Rata-rata Jumlah Sewa Harian')
    ax.set_title('Pengaruh Musim Terhadap Jumlah Sewa Sepeda Harian')

    st.pyplot(fig)

# Function to plot the monthly and hourly patterns
def plot_monthly_hourly_patterns():
    # Pola berdasarkan bulan
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    sns.lineplot(x="mnth_daily", y="cnt_daily", data=bike_merge, ci=None)
    plt.title("Pola Jumlah Sewa Sepeda Harian Berdasarkan Bulan")
    plt.xlabel("Bulan")
    plt.ylabel("Jumlah Sewa Sepeda Harian")
    fig1 = plt.gcf()  # Get the current figure
    st.pyplot(fig1)

    # Pola berdasarkan jam
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="hr", y="cnt_hourly", data=bike_merge, ci=None)
    plt.title("Pola Jumlah Sewa Sepeda Harian Berdasarkan Jam")
    plt.xlabel("Jam")
    plt.ylabel("Jumlah Sewa Sepeda Harian")
    fig2 = plt.gcf()  # Get the current figure
    st.pyplot(fig2)


# Function to plot the influence of weathersit
def plot_weathersit_influence():
    # Pengaruh Weathersit
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x="weathersit_daily", y="cnt_daily", data=bike_merge, ax=ax)
    ax.set_title("Pengaruh Weathersit Terhadap Jumlah Sewa Sepeda Harian")
    ax.set_xlabel("Weathersit")
    ax.set_ylabel("Jumlah Sewa Sepeda Harian")
    st.pyplot(fig)

# Function to compare working day and holiday
def compare_workingday_holiday():
    # Perbandingan hari kerja dan hari libur
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x="workingday_daily", y="cnt_daily", data=bike_merge, ax=ax)
    ax.set_title("Perbedaan Antara Hari Kerja dan Hari Libur dalam Jumlah Sewa Sepeda Harian")
    ax.set_xlabel("Workingday")
    ax.set_ylabel("Jumlah Sewa Sepeda Harian")
    st.pyplot(fig)

# Streamlit App
def main():
    st.sidebar.title("Analisis Data Sepeda")
    st.sidebar.image('https://www.marketplace.org/wp-content/uploads/2021/10/GettyImages-1221065582.jpg', use_column_width=True)

    analysis_option = st.sidebar.selectbox("Pilih Analisis:", ["Hubungan Musim dan Jumlah Sewa", "Pola Bulan dan Jam",
                                                              "Pengaruh Cuaca", "Perbandingan Hari Kerja dan Libur"])

    if analysis_option == "Hubungan Musim dan Jumlah Sewa":
        st.header("Analisis Hubungan Musim dan Jumlah Sewa Sepeda Harian")
        plot_seasonal_analysis()

        # Informasi tambahan
        st.write("""
        Musim panas merupakan waktu paling diminati untuk bersepeda, didukung oleh cuaca yang cerah dan hangat, liburan, dan tingginya aktivitas luar ruangan. Oleh karena itu, pengelola layanan sewa sepeda dapat mempersiapkan strategi pemasaran dan persediaan sepeda yang lebih baik selama musim panas untuk memenuhi tingginya permintaan.
        """)

    elif analysis_option == "Pola Bulan dan Jam":
        st.header("Analisis Pola Bulan dan Jam dalam Jumlah Sewa Sepeda Harian")
        plot_monthly_hourly_patterns()

        # Informasi tambahan
        st.write("""
        **Pertanyaan 1**

        Berdasarkan grafik di atas, dapat dilihat bahwa jumlah sewa sepeda harian cenderung meningkat dari bulan Januari hingga Agustus, dan kemudian menurun hingga Desember. Pola ini dapat dijelaskan oleh beberapa faktor, yaitu:

        * **Cuaca**. Cuaca yang lebih hangat dan cerah di musim panas membuat orang lebih tertarik untuk bersepeda.
        * **Liburan**. Banyak orang berlibur di musim panas, sehingga mereka lebih sering menggunakan sepeda untuk berkeliling.
        * **Aktivitas**. Di musim panas, banyak orang yang melakukan aktivitas di luar ruangan, sehingga mereka lebih sering menggunakan sepeda.

        **Kesimpulan:**

        Musim panas adalah waktu yang paling baik untuk bersepeda, karena cuaca yang lebih hangat dan cerah membuat orang lebih nyaman dan aman untuk bersepeda.
        """)

        st.write("""
        **Pertanyaan 2**

        Berdasarkan grafik di atas, dapat dilihat bahwa jumlah sewa sepeda harian cenderung meningkat pada bulan Juni dan September. Bulan Juni dan September adalah bulan-bulan di mana musim panas di Indonesia sedang mencapai puncaknya. Cuaca yang lebih hangat dan cerah di bulan-bulan ini membuat orang lebih tertarik untuk bersepeda.

        Pada pagi hari dan sore hari, jumlah sewa sepeda meningkat. Peningkatan jumlah sewa sepeda pada jam-jam ini dapat dijelaskan oleh faktor-faktor berikut:

        * **Kebutuhan transportasi**. Banyak orang menggunakan sepeda untuk bertransportasi ke tempat kerja atau sekolah. Jam 8 pagi dan jam 5 atau 6 sore adalah waktu yang umum bagi orang-orang untuk berangkat dan pulang kerja atau sekolah.
        * **Aktivitas rekreasi**. Banyak orang menggunakan sepeda untuk rekreasi pada pagi hari dan sore hari. Cuaca yang lebih hangat dan cerah di pagi hari dan sore hari membuat orang lebih nyaman untuk bersepeda.

        **Kesimpulan:**

        Musim panas, terutama pada bulan Juni dan September, dan pagi hari dan sore hari adalah waktu yang paling baik untuk bersepeda.
        """)

    elif analysis_option == "Pengaruh Cuaca":
        st.header("Analisis Pengaruh Cuaca Terhadap Jumlah Sewa Sepeda Harian")
        plot_weathersit_influence()

        # Informasi tambahan
        st.write("""
        Berdasarkan gambar box plot di atas, dapat dilihat bahwa jumlah sewa sepeda harian cenderung meningkat pada cuaca cerah, dan menurun pada cuaca hujan atau berawan.

        Cuaca cerah memiliki pengaruh yang signifikan terhadap jumlah sewa sepeda harian. Hal ini dikarenakan cuaca cerah membuat orang lebih nyaman dan aman untuk bersepeda.

        **Kesimpulan:**

        Cuaca cerah adalah waktu yang paling baik untuk bersepeda.
        """)

    elif analysis_option == "Perbandingan Hari Kerja dan Libur":
        st.header("Analisis Perbedaan Antara Hari Kerja dan Hari Libur dalam Jumlah Sewa Sepeda Harian")
        compare_workingday_holiday()

        # Informasi tambahan
        st.write("""
        Berdasarkan gambar box plot di atas, dapat dilihat bahwa jumlah sewa sepeda harian cenderung lebih tinggi pada hari libur daripada hari kerja.

        Hari libur memiliki pengaruh yang signifikan terhadap jumlah sewa sepeda harian. Hal ini dikarenakan orang memiliki lebih banyak waktu luang dan kesempatan untuk bersepeda pada hari libur.

        **Kesimpulan:**

        Hari libur adalah waktu yang paling baik untuk bersepeda.
        """)

if __name__ == "__main__":
    main()
