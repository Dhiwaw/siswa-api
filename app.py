import sqlite3
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

DATABASE = 'siswa.db'

def get_db_connection():
    """Membuat koneksi ke database SQLite"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Inisialisasi database dan membuat tabel jika belum ada"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS siswa (
            id_siswa INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT NOT NULL,
            jenjang TEXT NOT NULL,
            status_siswa TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

@app.route('/', methods=['GET'])
def home():
    """Endpoint untuk mengecek status API"""
    return jsonify({
        "status": True,
        "message": "API berjalan"
    }), 200

@app.route('/siswa', methods=['GET'])
def get_siswa():
    """
    GET /siswa - Mengambil seluruh data siswa
    GET /siswa?id=1 - Mengambil satu data siswa berdasarkan id_siswa
    """
    try:
        id_siswa = request.args.get('id')
        conn = get_db_connection()
        cursor = conn.cursor()
        
        if id_siswa:
            # Mengambil satu data siswa berdasarkan id
            cursor.execute('SELECT * FROM siswa WHERE id_siswa = ?', (id_siswa,))
            row = cursor.fetchone()
            conn.close()
            
            if row:
                siswa = {
                    'id_siswa': row['id_siswa'],
                    'nama_siswa': row['nama_siswa'],
                    'jenjang': row['jenjang'],
                    'status_siswa': row['status_siswa']
                }
                return jsonify({
                    "status": True,
                    "message": "Data siswa ditemukan",
                    "data": siswa
                }), 200
            else:
                return jsonify({
                    "status": False,
                    "message": "Data siswa tidak ditemukan"
                }), 404
        else:
            # Mengambil seluruh data siswa
            cursor.execute('SELECT * FROM siswa')
            rows = cursor.fetchall()
            conn.close()
            
            siswa_list = []
            for row in rows:
                siswa_list.append({
                    'id_siswa': row['id_siswa'],
                    'nama_siswa': row['nama_siswa'],
                    'jenjang': row['jenjang'],
                    'status_siswa': row['status_siswa']
                })
            
            return jsonify({
                "status": True,
                "message": "Data siswa berhasil diambil",
                "data": siswa_list,
                "total": len(siswa_list)
            }), 200
    
    except Exception as e:
        return jsonify({
            "status": False,
            "message": f"Terjadi kesalahan: {str(e)}"
        }), 500

@app.route('/siswa', methods=['POST'])
def create_siswa():
    """
    POST /siswa - Menambahkan data siswa baru
    Request JSON:
    {
        "nama_siswa": "Dhiya",
        "jenjang": "Kuliah",
        "status_siswa": "Aktif"
    }
    """
    try:
        data = request.get_json()
        
        # Validasi input
        if not data:
            return jsonify({
                "status": False,
                "message": "Request body tidak boleh kosong"
            }), 400
        
        nama_siswa = data.get('nama_siswa')
        jenjang = data.get('jenjang')
        status_siswa = data.get('status_siswa')
        
        # Validasi field yang diperlukan
        if not nama_siswa or not jenjang or not status_siswa:
            return jsonify({
                "status": False,
                "message": "Field nama_siswa, jenjang, dan status_siswa harus diisi"
            }), 400
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Menggunakan parameterized query untuk mencegah SQL Injection
        cursor.execute(
            'INSERT INTO siswa (nama_siswa, jenjang, status_siswa) VALUES (?, ?, ?)',
            (nama_siswa, jenjang, status_siswa)
        )
        
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        
        return jsonify({
            "status": True,
            "message": "Data siswa berhasil ditambahkan",
            "data": {
                "id_siswa": new_id,
                "nama_siswa": nama_siswa,
                "jenjang": jenjang,
                "status_siswa": status_siswa
            }
        }), 201
    
    except Exception as e:
        return jsonify({
            "status": False,
            "message": f"Terjadi kesalahan: {str(e)}"
        }), 500

@app.route('/siswa', methods=['PUT'])
def update_siswa():
    """
    PUT /siswa - Mengubah data siswa
    Request JSON:
    {
        "id_siswa": 1,
        "nama_siswa": "Dhiya Update",
        "jenjang": "Kuliah",
        "status_siswa": "Aktif"
    }
    """
    try:
        data = request.get_json()
        
        # Validasi input
        if not data:
            return jsonify({
                "status": False,
                "message": "Request body tidak boleh kosong"
            }), 400
        
        id_siswa = data.get('id_siswa')
        nama_siswa = data.get('nama_siswa')
        jenjang = data.get('jenjang')
        status_siswa = data.get('status_siswa')
        
        # Validasi field yang diperlukan
        if not id_siswa or not nama_siswa or not jenjang or not status_siswa:
            return jsonify({
                "status": False,
                "message": "Field id_siswa, nama_siswa, jenjang, dan status_siswa harus diisi"
            }), 400
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Cek apakah data siswa ada
        cursor.execute('SELECT * FROM siswa WHERE id_siswa = ?', (id_siswa,))
        existing = cursor.fetchone()
        
        if not existing:
            conn.close()
            return jsonify({
                "status": False,
                "message": "Data siswa tidak ditemukan"
            }), 404
        
        # Menggunakan parameterized query untuk mencegah SQL Injection
        cursor.execute(
            'UPDATE siswa SET nama_siswa = ?, jenjang = ?, status_siswa = ? WHERE id_siswa = ?',
            (nama_siswa, jenjang, status_siswa, id_siswa)
        )
        
        conn.commit()
        conn.close()
        
        return jsonify({
            "status": True,
            "message": "Data siswa berhasil diubah",
            "data": {
                "id_siswa": id_siswa,
                "nama_siswa": nama_siswa,
                "jenjang": jenjang,
                "status_siswa": status_siswa
            }
        }), 200
    
    except Exception as e:
        return jsonify({
            "status": False,
            "message": f"Terjadi kesalahan: {str(e)}"
        }), 500

@app.route('/siswa', methods=['DELETE'])
def delete_siswa():
    """
    DELETE /siswa - Menghapus data siswa
    Request JSON:
    {
        "id_siswa": 1
    }
    """
    try:
        data = request.get_json()
        
        # Validasi input
        if not data:
            return jsonify({
                "status": False,
                "message": "Request body tidak boleh kosong"
            }), 400
        
        id_siswa = data.get('id_siswa')
        
        # Validasi field yang diperlukan
        if not id_siswa:
            return jsonify({
                "status": False,
                "message": "Field id_siswa harus diisi"
            }), 400
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Cek apakah data siswa ada
        cursor.execute('SELECT * FROM siswa WHERE id_siswa = ?', (id_siswa,))
        existing = cursor.fetchone()
        
        if not existing:
            conn.close()
            return jsonify({
                "status": False,
                "message": "Data siswa tidak ditemukan"
            }), 404
        
        # Menggunakan parameterized query untuk mencegah SQL Injection
        cursor.execute('DELETE FROM siswa WHERE id_siswa = ?', (id_siswa,))
        
        conn.commit()
        conn.close()
        
        return jsonify({
            "status": True,
            "message": "Data siswa berhasil dihapus",
            "data": {
                "id_siswa": id_siswa
            }
        }), 200
    
    except Exception as e:
        return jsonify({
            "status": False,
            "message": f"Terjadi kesalahan: {str(e)}"
        }), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=False, host='0.0.0.0', port=5000)

