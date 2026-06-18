# REST API Siswa dengan Flask dan SQLite

REST API untuk mengelola data siswa menggunakan Flask dan SQLite.

## Fitur

- ✅ CRUD operations (Create, Read, Update, Delete)
- ✅ SQLite database dengan parameterized queries (SQL Injection prevention)
- ✅ CORS enabled untuk akses dari domain lain
- ✅ JSON response format
- ✅ Error handling yang baik
- ✅ Siap di-deploy ke Railway

## Struktur Project

```
siswa-api/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── Procfile           # Railway deployment configuration
├── .gitignore         # Git ignore file
└── README.md          # Documentation
```

## Instalasi Lokal

1. Clone repository:
```bash
git clone <repository-url>
cd siswa-api
```

2. Buat virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Jalankan aplikasi:
```bash
python app.py
```

Aplikasi akan berjalan di `http://localhost:5000`

## Deployment ke Railway

1. Push code ke GitHub
2. Connect repository ke Railway
3. Railway akan otomatis mendeteksi `Procfile` dan `requirements.txt`
4. Aplikasi akan di-deploy secara otomatis

## API Endpoints

### 1. Health Check
```
GET /
```

**Response:**
```json
{
  "status": true,
  "message": "API berjalan"
}
```

### 2. Get All Siswa
```
GET /siswa
```

**Response:**
```json
{
  "status": true,
  "message": "Data siswa berhasil diambil",
  "data": [
    {
      "id_siswa": 1,
      "nama_siswa": "Dhiya",
      "jenjang": "Kuliah",
      "status_siswa": "Aktif"
    }
  ],
  "total": 1
}
```

### 3. Get Siswa by ID
```
GET /siswa?id=1
```

**Response:**
```json
{
  "status": true,
  "message": "Data siswa ditemukan",
  "data": {
    "id_siswa": 1,
    "nama_siswa": "Dhiya",
    "jenjang": "Kuliah",
    "status_siswa": "Aktif"
  }
}
```

### 4. Create Siswa
```
POST /siswa
Content-Type: application/json

{
  "nama_siswa": "Dhiya",
  "jenjang": "Kuliah",
  "status_siswa": "Aktif"
}
```

**Response:**
```json
{
  "status": true,
  "message": "Data siswa berhasil ditambahkan",
  "data": {
    "id_siswa": 1,
    "nama_siswa": "Dhiya",
    "jenjang": "Kuliah",
    "status_siswa": "Aktif"
  }
}
```

### 5. Update Siswa
```
PUT /siswa
Content-Type: application/json

{
  "id_siswa": 1,
  "nama_siswa": "Dhiya Update",
  "jenjang": "Kuliah",
  "status_siswa": "Aktif"
}
```

**Response:**
```json
{
  "status": true,
  "message": "Data siswa berhasil diubah",
  "data": {
    "id_siswa": 1,
    "nama_siswa": "Dhiya Update",
    "jenjang": "Kuliah",
    "status_siswa": "Aktif"
  }
}
```

### 6. Delete Siswa
```
DELETE /siswa
Content-Type: application/json

{
  "id_siswa": 1
}
```

**Response:**
```json
{
  "status": true,
  "message": "Data siswa berhasil dihapus",
  "data": {
    "id_siswa": 1
  }
}
```

## Testing dengan cURL

### Health Check
```bash
curl -X GET http://localhost:5000/
```

### Get All Siswa
```bash
curl -X GET http://localhost:5000/siswa
```

### Get Siswa by ID
```bash
curl -X GET "http://localhost:5000/siswa?id=1"
```

### Create Siswa
```bash
curl -X POST http://localhost:5000/siswa \
  -H "Content-Type: application/json" \
  -d '{
    "nama_siswa": "Dhiya",
    "jenjang": "Kuliah",
    "status_siswa": "Aktif"
  }'
```

### Update Siswa
```bash
curl -X PUT http://localhost:5000/siswa \
  -H "Content-Type: application/json" \
  -d '{
    "id_siswa": 1,
    "nama_siswa": "Dhiya Update",
    "jenjang": "Kuliah",
    "status_siswa": "Aktif"
  }'
```

### Delete Siswa
```bash
curl -X DELETE http://localhost:5000/siswa \
  -H "Content-Type: application/json" \
  -d '{
    "id_siswa": 1
  }'
```

## Testing dengan Postman

1. Import collection atau buat request baru
2. Set method dan URL sesuai endpoint
3. Untuk POST/PUT/DELETE, set header `Content-Type: application/json`
4. Masukkan request body sesuai format JSON

## Database

Database SQLite (`siswa.db`) akan dibuat otomatis saat aplikasi pertama kali dijalankan.

### Struktur Tabel `siswa`

| Column | Type | Constraint |
|--------|------|-----------|
| id_siswa | INTEGER | PRIMARY KEY AUTOINCREMENT |
| nama_siswa | TEXT | NOT NULL |
| jenjang | TEXT | NOT NULL |
| status_siswa | TEXT | NOT NULL |

## Security

- ✅ Menggunakan parameterized queries untuk mencegah SQL Injection
- ✅ CORS enabled dengan Flask-CORS
- ✅ Input validation pada setiap endpoint
- ✅ Error handling yang aman

## Teknologi

- **Framework**: Flask 2.3.3
- **Database**: SQLite3
- **CORS**: Flask-CORS 4.0.0
- **Server**: Gunicorn 21.2.0
- **Python**: 3.11+

## License

MIT

