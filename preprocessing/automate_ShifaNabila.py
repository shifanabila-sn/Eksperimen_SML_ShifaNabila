import pandas as pd
import numpy as np

def preprocess_data(raw_data_path):
    print(f"[Log] Starting preprocessing with raw_data_path: {raw_data_path}")
    try:
        # 1. Muat dataset
        df = pd.read_csv(raw_data_path)
        print(f"[Log] Dataset loaded successfully. Shape: {df.shape}")

        # 2. Hapus baris yang mengandung nilai kosong
        df_clean = df.dropna()
        print(f"[Log] Missing values handled. Shape after dropna: {df_clean.shape}")

        # 3. Hapus data duplikat
        df_clean = df_clean.drop_duplicates()
        print(f"[Log] Duplicates removed. Shape after drop_duplicates: {df_clean.shape}")

        # 4. Konversi kolom 'Tanggal' ke tipe data datetime
        df_clean["Tanggal"] = pd.to_datetime(df_clean["Tanggal"])
        print("[Log] 'Tanggal' column converted to datetime.")

        # 5. Lakukan one-hot encoding pada kolom kategorikal
        df_encoded = pd.get_dummies(
            df_clean,
            columns=["Kategori", "Lokasi_Toko", "Metode_Bayar"],
            drop_first=True
        )
        print(f"[Log] Categorical columns encoded. Shape after encoding: {df_encoded.shape}")

        # 6. Pilih kolom-kolom untuk DataFrame akhir
        df_final = df_encoded[[
            "Harga_Satuan",
            "Qty",
            "Diskon_IDR",
            "Total_Penjualan"
        ]]
        print(f"[Log] Final features selected. Final shape: {df_final.shape}")

        # 7. Simpan DataFrame hasil preprocessing ke file CSV baru
        df_final.to_csv("instax_sales_preprocessing.csv", index=False)
        print(f"[Log] Data preprocessed and saved to instax_sales_preprocessing.csv. Shape: {df_final.shape}")

        print("[Log] Preprocessing function finished successfully.")
        return df_final
    except Exception as e:
        print(f"[ERROR] An error occurred during preprocessing: {e}")
        import traceback
        traceback.print_exc()
        raise 

if __name__ == "__main__":
    print("[Log] Script started from __main__ block.")
    raw_data_file_path = "namadataset_raw/instax_sales_transaction_data.csv"
    preprocessed_df = preprocess_data(raw_data_file_path)

    print("Preprocessing selesai via script otomatis.")
