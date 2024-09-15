from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inisialisasi WebDriver
driver = webdriver.Chrome()

# Akses halaman
driver.get('https://www.nc-gym.com')

# Tunggu agar Cloudflare selesai
time.sleep(5)

# Akses API setelah verifikasi
api_url = "https://www.nc-gym.com/api/gate-log"
payload = {'id': '786195', 'status': 'keluar'}
driver.execute_script(f'''
    fetch("{api_url}", {{
        method: "POST",
        headers: {{
            "Content-Type": "application/json"
        }},
        body: JSON.stringify({payload})
    }}).then(response => response.text()).then(data => console.log(data));
''')

time.sleep(5)  # Tunggu hasil
driver.quit()