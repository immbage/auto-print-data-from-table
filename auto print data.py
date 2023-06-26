from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.bi.go.id/id/statistik/informasi-kurs/transaksi-bi/default.aspx")

# Fill in "Harian"
date_field = driver.find_element(By.ID, 'ctl00_PlaceHolderMain_g_6c89d4ad_107f_437d_bd54_8fda17b556bf_ctl00_txtTanggal')
date_field.clear()
date_field.send_keys("09-jun-2023")

# Click "Cari"
search_button = driver.find_element(By.ID, 'ctl00_PlaceHolderMain_g_6c89d4ad_107f_437d_bd54_8fda17b556bf_ctl00_btnSearch2')
search_button.click()

# Extract table data
data_table = driver.find_element(By.ID, 'ctl00_PlaceHolderMain_g_6c89d4ad_107f_437d_bd54_8fda17b556bf_ctl00_gvSearchResult1')
rows = data_table.find_elements(By.TAG_NAME, "tr")

# Store data in a list
data_list = []
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    row_data = [cell.text for cell in cells]
    data_list.append(row_data)

# Print the extracted data
for data in data_list:
    print(data)

driver.quit()
