=> Run File Python
    python <nameFile>.py

=> API
    => Membuat Lingkungan Virtual/Folder Untuk Python
        => Create Python (ENVIRONTMEN (Didalam Folder Yang Telah Dibuat)(Seperti Vendor))
            mkdir API
            cd API
            python -m venv venv
        => Mengaktifkannya
            venv/scripts/activate
    => INSTALL LIBRARY
        => "pymssql" (Untuk Menghubungkan Dengan SQL SERVER (Connecting)) Dan "python-dotenv" (Untuk Membuat Bekerja Dengan .env)
            pip install pymssql python-dotenv
        => Menghasilkan "requirements.txt" File Yang Menyertakan Semua Dependensi/Library
            pip freeze > requirements.txt
        => Untuk Connect Ke Database
            pip install pyodbc
        => Install Pandas (Jika Perlu)
            pip install pandas
        => Buat File .env
            type nul > .env
        => Buat Folder config
            mkdir config
        => Buat File .env
            type nul > connection.py