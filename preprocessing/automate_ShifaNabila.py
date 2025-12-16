import pandas as pd
import numpy as np

def preprocess_data(raw_data_path):
    """
    Performs preprocessing on the raw Instax sales transaction data.

    Args:
        raw_data_path (str): The file path to the raw dataset (CSV).

    Returns:
        pandas.DataFrame: The preprocessed DataFrame.
    """
    # 1. Muat dataset
    df = pd.read_csv(raw_data_path)

    # 2. Hapus baris yang mengandung nilai kosong
    df_clean = df.dropna()

    # 3. Hapus data duplikat
    df_clean = df_clean.drop_duplicates()

    # 4. Konversi kolom 'Tanggal' ke tipe data datetime
    df_clean["Tanggal"] = pd.to_datetime(df_clean["Tanggal"])

    # 5. Lakukan one-hot encoding pada kolom kategorikal
    df_encoded = pd.get_dummies(
        df_clean,
        columns=["Kategori", "Lokasi_Toko", "Metode_Bayar"],
        drop_first=True
    )

    # 6. Pilih kolom-kolom untuk DataFrame akhir
    df_final = df_encoded[[
        "Harga_Satuan",
        "Qty",
        "Diskon_IDR",
        "Total_Penjualan"
    ]]

    # 7. Simpan DataFrame hasil preprocessing ke file CSV baru
    df_final.to_csv("instax_sales_preprocessing.csv", index=False)

    print(f"Data preprocessed and saved to instax_sales_preprocessing.csv. Shape: {df_final.shape}")

    return df_final

    if __name__ == "__main__":

           raw_data_file_path = "namadataset_raw/instax_sales_transaction_data.csv"
            preprocessed_df = preprocess_data(raw_data_file_path)

    print("Preprocessing selesai via script otomatis.")
