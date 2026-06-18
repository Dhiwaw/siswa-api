# Testing Guide - REST API Siswa

Panduan lengkap untuk testing semua endpoint API dengan contoh request dan response.

## Persiapan

Pastikan aplikasi sudah berjalan:
```bash
python app.py
```

Aplikasi akan berjalan di `http://localhost:5000`

---

## 1. Health Check

### Request
```bash
curl -X GET http://localhost:5000/
```

### Response (200 OK)
```json
{
  "status": true,
  "message": "API berjalan"
}
```

---

## 2. Get All Siswa (Kosong)

### Request
```bash
curl -X GET http://localhost:5000/siswa
```

### Response (200 OK)
```json
{
  "status": true,
  "message": "Data siswa berhasil diambil",
  "data": [],
  "total": 0
}
```

---

## 3. Create Siswa - Record 1

### Request
```bash
curl -X POST http://localhost:5000/siswa \
  -H "Content-Type: application/json" \
  -d '{
    "nama_siswa": "Dhiya",
    "jenjang": "Kuliah",
    "status_siswa": "Aktif"
  }'
```

### Response (201 Created)
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

---

## 4. Create Siswa - Record 2

### Request
```bash
curl -X POST http://localhost:5000/siswa \
  -H "Content-Type: application/json" \
  -d '{
    "nama_siswa": "Budi Santoso",
    "jenjang": "SMA",
    "status_siswa": "Aktif"
  }'
```

### Response (201 Created)
```json
{
  "status": true,
  "message": "Data siswa berhasil ditambahkan",
  "data": {
    "id_siswa": 2,
    "nama_siswa": "Budi Santoso",
    "jenjang": "SMA",
    "status_siswa": "Aktif"
  }
}
```

---

## 5. Create Siswa - Record 3

### Request
```bash
curl -X POST http://localhost:5000/siswa \
  -H "Content-Type: application/json" \
  -d '{
    "nama_siswa": "Siti Nurhaliza",
    "jenjang": "SMP",
    "status_siswa": "Aktif"
  }'
```

### Response (201 Created)
```json
{
  "status": true,
  "message": "Data siswa berhasil ditambahkan",
  "data": {
    "id_siswa": 3,
    "nama_siswa": "Siti Nurhaliza",
    "jenjang": "SMP",
    "status_siswa": "Aktif"
  }
}
```

---

## 6. Get All Siswa (Dengan Data)

### Request
```bash
curl -X GET http://localhost:5000/siswa
```

### Response (200 OK)
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
    },
    {
      "id_siswa": 2,
      "nama_siswa": "Budi Santoso",
      "jenjang": "SMA",
      "status_siswa": "Aktif"
    },
    {
      "id_siswa": 3,
      "nama_siswa": "Siti Nurhaliza",
      "jenjang": "SMP",
      "status_siswa": "Aktif"
    }
  ],
  "total": 3
}
```

---

## 7. Get Siswa by ID (ID = 1)

### Request
```bash
curl -X GET "http://localhost:5000/siswa?id=1"
```

### Response (200 OK)
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

---

## 8. Get Siswa by ID (ID = 2)

### Request
```bash
curl -X GET "http://localhost:5000/siswa?id=2"
```

### Response (200 OK)
```json
{
  "status": true,
  "message": "Data siswa ditemukan",
  "data": {
    "id_siswa": 2,
    "nama_siswa": "Budi Santoso",
    "jenjang": "SMA",
    "status_siswa": "Aktif"
  }
}
```

---

## 9. Get Siswa by ID (ID = 3)

### Request
```bash
curl -X GET "http://localhost:5000/siswa?id=3"
```

### Response (200 OK)
```json
{
  "status": true,
  "message": "Data siswa ditemukan",
  "data": {
    "id_siswa": 3,
    "nama_siswa": "Siti Nurhaliza",
    "jenjang": "SMP",
    "status_siswa": "Aktif"
  }
}
```

---

## 10. Get Siswa by ID (ID Tidak Ada)

### Request
```bash
curl -X GET "http://localhost:5000/siswa?id=999"
```

### Response (404 Not Found)
```json
{
  "status": false,
  "message": "Data siswa tidak ditemukan"
}
```

---

## 11. Update Siswa (ID = 1)

### Request
```bash
curl -X PUT http://localhost:5000/siswa \
  -H "Content-Type: application/json" \
  -d '{
    "id_siswa": 1,
    "nama_siswa": "Dhiya Putri",
    "jenjang": "Magister",
    "status_siswa": "Aktif"
  }'
```

### Response (200 OK)
```json
{
  "status": true,
  "message": "Data siswa berhasil diubah",
  "data": {
    "id_siswa": 1,
    "nama_siswa": "Dhiya Putri",
    "jenjang": "Magister",
    "status_siswa": "Aktif"
  }
}
```

---

## 12. Update Siswa (ID = 2)

### Request
```bash
curl -X PUT http://localhost:5000/siswa \
  -H "Content-Type: application/json" \
  -d '{
    "id_siswa": 2,
    "nama_siswa": "Budi Santoso",
    "jenjang": "SMA",
    "status_siswa": "Tidak Aktif"
  }'
```

### Response (200 OK)
```json
{
  "status": true,
  "message": "Data siswa berhasil diubah",
  "data": {
    "id_siswa": 2,
    "nama_siswa": "Budi Santoso",
    "jenjang": "SMA",
    "status_siswa": "Tidak Aktif"
  }
}
```

---

## 13. Update Siswa (ID Tidak Ada)

### Request
```bash
curl -X PUT http://localhost:5000/siswa \
  -H "Content-Type: application/json" \
  -d '{
    "id_siswa": 999,
    "nama_siswa": "Tidak Ada",
    "jenjang": "Kuliah",
    "status_siswa": "Aktif"
  }'
```

### Response (404 Not Found)
```json
{
  "status": false,
  "message": "Data siswa tidak ditemukan"
}
```

---

## 14. Get All Siswa (Setelah Update)

### Request
```bash
curl -X GET http://localhost:5000/siswa
```

### Response (200 OK)
```json
{
  "status": true,
  "message": "Data siswa berhasil diambil",
  "data": [
    {
      "id_siswa": 1,
      "nama_siswa": "Dhiya Putri",
      "jenjang": "Magister",
      "status_siswa": "Aktif"
    },
    {
      "id_siswa": 2,
      "nama_siswa": "Budi Santoso",
      "jenjang": "SMA",
      "status_siswa": "Tidak Aktif"
    },
    {
      "id_siswa": 3,
      "nama_siswa": "Siti Nurhaliza",
      "jenjang": "SMP",
      "status_siswa": "Aktif"
    }
  ],
  "total": 3
}
```

---

## 15. Delete Siswa (ID = 2)

### Request
```bash
curl -X DELETE http://localhost:5000/siswa \
  -H "Content-Type: application/json" \
  -d '{
    "id_siswa": 2
  }'
```

### Response (200 OK)
```json
{
  "status": true,
  "message": "Data siswa berhasil dihapus",
  "data": {
    "id_siswa": 2
  }
}
```

---

## 16. Get All Siswa (Setelah Delete)

### Request
```bash
curl -X GET http://localhost:5000/siswa
```

### Response (200 OK)
```json
{
  "status": true,
  "message": "Data siswa berhasil diambil",
  "data": [
    {
      "id_siswa": 1,
      "nama_siswa": "Dhiya Putri",
      "jenjang": "Magister",
      "status_siswa": "Aktif"
    },
    {
      "id_siswa": 3,
      "nama_siswa": "Siti Nurhaliza",
      "jenjang": "SMP",
      "status_siswa": "Aktif"
    }
  ],
  "total": 2
}
```

---

## 17. Delete Siswa (ID Tidak Ada)

### Request
```bash
curl -X DELETE http://localhost:5000/siswa \
  -H "Content-Type: application/json" \
  -d '{
    "id_siswa": 999
  }'
```

### Response (404 Not Found)
```json
{
  "status": false,
  "message": "Data siswa tidak ditemukan"
}
```

---

## 18. Error Handling - Missing Required Field (POST)

### Request
```bash
curl -X POST http://localhost:5000/siswa \
  -H "Content-Type: application/json" \
  -d '{
    "nama_siswa": "Incomplete Data"
  }'
```

### Response (400 Bad Request)
```json
{
  "status": false,
  "message": "Field nama_siswa, jenjang, dan status_siswa harus diisi"
}
```

---

## 19. Error Handling - Empty Request Body (POST)

### Request
```bash
curl -X POST http://localhost:5000/siswa \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Response (400 Bad Request)
```json
{
  "status": false,
  "message": "Field nama_siswa, jenjang, dan status_siswa harus diisi"
}
```

---

## 20. Error Handling - Missing ID Field (DELETE)

### Request
```bash
curl -X DELETE http://localhost:5000/siswa \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Response (400 Bad Request)
```json
{
  "status": false,
  "message": "Field id_siswa harus diisi"
}
```

---

## Testing dengan Postman

### Langkah-langkah:

1. **Buka Postman**
2. **Buat Collection baru** (opsional)
3. **Untuk setiap endpoint:**
   - Set **Method** (GET, POST, PUT, DELETE)
   - Set **URL** (http://localhost:5000/...)
   - Untuk POST/PUT/DELETE: 
     - Klik tab **Body**
     - Pilih **raw**
     - Pilih **JSON** dari dropdown
     - Paste request JSON
   - Klik **Send**

### Contoh untuk POST:
```
Method: POST
URL: http://localhost:5000/siswa
Headers: Content-Type: application/json
Body (raw):
{
  "nama_siswa": "Dhiya",
  "jenjang": "Kuliah",
  "status_siswa": "Aktif"
}
```

---

## Testing dengan Python Requests

```python
import requests
import json

BASE_URL = "http://localhost:5000"

# 1. Health Check
response = requests.get(f"{BASE_URL}/")
print("Health Check:", response.json())

# 2. Create Siswa
data = {
    "nama_siswa": "Dhiya",
    "jenjang": "Kuliah",
    "status_siswa": "Aktif"
}
response = requests.post(f"{BASE_URL}/siswa", json=data)
print("Create Siswa:", response.json())

# 3. Get All Siswa
response = requests.get(f"{BASE_URL}/siswa")
print("Get All Siswa:", response.json())

# 4. Get Siswa by ID
response = requests.get(f"{BASE_URL}/siswa?id=1")
print("Get Siswa by ID:", response.json())

# 5. Update Siswa
data = {
    "id_siswa": 1,
    "nama_siswa": "Dhiya Update",
    "jenjang": "Kuliah",
    "status_siswa": "Aktif"
}
response = requests.put(f"{BASE_URL}/siswa", json=data)
print("Update Siswa:", response.json())

# 6. Delete Siswa
data = {"id_siswa": 1}
response = requests.delete(f"{BASE_URL}/siswa", json=data)
print("Delete Siswa:", response.json())
```

---

## Testing dengan JavaScript/Fetch

```javascript
const BASE_URL = "http://localhost:5000";

// 1. Health Check
fetch(`${BASE_URL}/`)
  .then(res => res.json())
  .then(data => console.log("Health Check:", data));

// 2. Create Siswa
fetch(`${BASE_URL}/siswa`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    nama_siswa: "Dhiya",
    jenjang: "Kuliah",
    status_siswa: "Aktif"
  })
})
  .then(res => res.json())
  .then(data => console.log("Create Siswa:", data));

// 3. Get All Siswa
fetch(`${BASE_URL}/siswa`)
  .then(res => res.json())
  .then(data => console.log("Get All Siswa:", data));

// 4. Get Siswa by ID
fetch(`${BASE_URL}/siswa?id=1`)
  .then(res => res.json())
  .then(data => console.log("Get Siswa by ID:", data));

// 5. Update Siswa
fetch(`${BASE_URL}/siswa`, {
  method: "PUT",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    id_siswa: 1,
    nama_siswa: "Dhiya Update",
    jenjang: "Kuliah",
    status_siswa: "Aktif"
  })
})
  .then(res => res.json())
  .then(data => console.log("Update Siswa:", data));

// 6. Delete Siswa
fetch(`${BASE_URL}/siswa`, {
  method: "DELETE",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ id_siswa: 1 })
})
  .then(res => res.json())
  .then(data => console.log("Delete Siswa:", data));
```

---

## HTTP Status Codes

| Code | Meaning | Contoh |
|------|---------|--------|
| 200 | OK | GET, PUT, DELETE berhasil |
| 201 | Created | POST berhasil membuat resource |
| 400 | Bad Request | Input tidak valid |
| 404 | Not Found | Resource tidak ditemukan |
| 500 | Server Error | Error di server |

---

## Tips Testing

1. **Gunakan ID yang valid** saat melakukan GET by ID, UPDATE, atau DELETE
2. **Pastikan Content-Type header** adalah `application/json` untuk POST/PUT/DELETE
3. **Validasi response status code** untuk memastikan request berhasil
4. **Cek response body** untuk melihat detail error jika ada
5. **Gunakan tools seperti Postman atau Insomnia** untuk testing yang lebih mudah

---

## Troubleshooting

### Error: "Connection refused"
- Pastikan aplikasi sudah berjalan dengan `python app.py`
- Pastikan port 5000 tidak digunakan aplikasi lain

### Error: "Invalid JSON"
- Pastikan JSON format benar (gunakan JSON validator)
- Pastikan semua string menggunakan double quotes

### Error: "Field ... harus diisi"
- Pastikan semua required field ada di request body
- Cek spelling field name

### Database Error
- Pastikan file `siswa.db` tidak corrupt
- Hapus `siswa.db` dan jalankan aplikasi lagi untuk reset database

---

## Kesimpulan

API sudah siap untuk production deployment ke Railway. Semua endpoint telah ditest dan berfungsi dengan baik.

