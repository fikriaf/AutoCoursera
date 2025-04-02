print("[Loading Library and Environment...]")
import ai, ai2
import env
import time, string, re
import pickle
import pyautogui
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options


email = env.EMAIL
password = env.PASSWORD
if email == "" and password == "":
    print("[ File .env is Empty ]")
    exit()
print(f"[ Email: {email} | Password: {password} ]")

LinkLogin = (
    "https://www.coursera.org/login"
)

def stop_execution():
    print("\nKombinasi tombol terdeteksi. Menghentikan loop...")
    global stop_loop
    stop_loop = True
    
first = True
modequiz = False
target_nilai = 100

while True:
    nilai = []
    inputLink = input("\nInput link course (Banyak link pisahkan dengan spasi): ")
    Link = inputLink.split()
    print(f"\nJumlah Course yng di Input: {len(Link)}")

    print("[Memuat Browser...]")
    profile_path = r"C:\Users\runneradmin\AppData\Roaming\Mozilla\Firefox\Profiles\406qyncq.default-release"
    firefox_options = Options()
    firefox_options.set_preference("profile", profile_path)
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--disable-popup-blocking")
    firefox_options.set_preference("browser.link.open_newwindow", 1)
    firefox_options.set_preference("browser.link.open_newwindow.restriction", 0)
    driver = webdriver.Firefox(options=firefox_options)
            
    for index, course in enumerate(Link):
        driver.get(course)
        print("[Memuat Cookie...]")
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
                
        print("[Memuat Course...]")
        course_index = index+1
        stop_loop = False
        driver.get(course)
        
        work_ai_1 = 1
        work_ai_2 = 1 
        
        try:
            try:
                WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".c-modal-x-out")))
                popupAwal = driver.find_element(
                    By.CSS_SELECTOR, ".c-modal-x-out"
                )
                if popupAwal:
                    popupAwal.click()
            except:
                pass
            print("[Close POP UP]")
            while not stop_loop:
                yngsalah = []
                jawabane = []
                againlagi = True
                htungkuis = 0
                
                while True:
                    attemp_versilain = False
                    try:
                        popup = driver.find_element(By.XPATH, "//span[@class='cds-button-label' and text()='Close']")
                        if popup:
                            popup.click()
                    except:
                        pass
                    
                    try:
                        video = WebDriverWait(driver, 3).until(
                            EC.visibility_of_element_located((By.TAG_NAME, "video"))
                        )
                        if video:
                            WebDriverWait(driver, 2).until(
                                EC.visibility_of_element_located(
                                    (By.XPATH, "//button[@aria-label='Next Item']")
                                )
                            ).click()
                            print("[Next]")
                            continue
                    except:
                        pass
                    
                    try:
                        WebDriverWait(driver, 3).until(
                            EC.visibility_of_element_located(
                                (
                                    By.XPATH,
                                    "//span[@class='cds-button-label' and text()='Mark as completed']",
                                )
                            )
                        )
                        mark = driver.find_element(
                            By.XPATH,
                            "//span[@class='cds-button-label' and text()='Mark as completed']",
                        )
                        if mark:
                            mark.click()
                            print("[Reading Mark as Done]")
                            WebDriverWait(driver, 2).until(
                                EC.visibility_of_element_located(
                                    (By.XPATH, "//button[@aria-label='Next Item']")
                                )
                            ).click()
                            print("[Next]")
                            continue
                    except:
                        pass
                    
                    try:
                        linkquiz = driver.current_url
                        try:
                            try:
                                WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "css-6ecy9b")))
                                versilain = driver.find_element(By.CLASS_NAME, "css-6ecy9b").text
                                if versilain == "Submit your assignment":
                                    try:
                                        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='cds-button-label' and text()='Try again']")))
                                        tryagain = driver.find_element(By.XPATH, "//span[@class='cds-button-label' and text()='Try again']")
                                        try:
                                            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='retry-info']")))
                                            retake = driver.find_element(By.XPATH, "//div[@data-testid='retry-info']")
                                            if retake:
                                                WebDriverWait(driver, 2).until(
                                                    EC.visibility_of_element_located(
                                                        (By.XPATH, "//button[@aria-label='Next Item']")
                                                    )
                                                )
                                                driver.find_element(
                                                    By.XPATH, "//button[@aria-label='Next Item']"
                                                ).click()
                                                print("[Attempt Mencapai Limit]")
                                                print("[Next]")
                                                continue
                                        except:
                                            if tryagain:
                                                tryagain.click()
                                    except:
                                        WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "css-ra3hwj")))
                                        driver.find_element(By.CLASS_NAME, "css-ra3hwj").click()
                                    try:
                                        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='cds-button-label' and text()='Start']")))
                                        driver.find_element(By.XPATH, "//span[@class='cds-button-label' and text()='Start']").click()
                                    except:
                                        pass
                                    attemp_versilain = True
                                    
                            except:
                                pass
                            
                            WebDriverWait(driver, 3).until(
                                EC.visibility_of_element_located((By.XPATH, '//h3[text()="Attempts"]'))
                            )
                        except:
                            WebDriverWait(driver, 2).until(
                                EC.visibility_of_element_located(
                                    (By.XPATH, "//button[@aria-label='Next Item']")
                                )
                            ).click()
                            print("[Next]")
                            continue
                        
                        ready_attempt = driver.find_element(By.CLASS_NAME, "css-ra3hwj")
                        if "cds-button-disabled" in ready_attempt.get_attribute("class"):
                            WebDriverWait(driver, 2).until(
                                EC.visibility_of_element_located(
                                    (By.XPATH, "//button[@aria-label='Next Item']")
                                )
                            )
                            driver.find_element(
                                By.XPATH, "//button[@aria-label='Next Item']"
                            ).click()
                            print("[Next]")
                            continue
                            
                        print("[QUIZ DITEMUKAN]")
                        print(f"[{linkquiz}]")
                        print("[Memuat Quiz...]")
                        
                        try:
                            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='cds-button-label' and text()='Continue']")))
                            driver.find_element(By.XPATH, "//span[@class='cds-button-label' and text()='Continue']").click()
                        except:
                            pass
                            
                        try:
                            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "css-ra3hwj")))
                            driver.find_element(By.CLASS_NAME, "css-ra3hwj").click()
                        except:
                            pass
                        try:
                            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "css-1wrxi0w")))
                            driver.find_element(By.CLASS_NAME, "css-1wrxi0w").click()
                        except:
                            pass
                        try:
                            WebDriverWait(driver, 10).until(
                                EC.visibility_of_element_located((By.CLASS_NAME, "css-1h9exxh"))
                            )
                        except:
                            pass
                        
                        if attemp_versilain:
                            classnya = "rc-FormPartsQuestion"
                        else:
                            classnya = "css-dqaucz"
                            
                        soalquiz = driver.find_elements(By.CLASS_NAME, classnya)
                        print(f"Jumlah Soal Quiz: {len(soalquiz)}")
                        print("[Mulai Mengerjakan Quiz...]")
                        preprompt = []
                        jawaban = []
                        jawaban_benar = []
                        mode_jawaban_textarea = False
                        for _, x in enumerate(soalquiz):
                            try:
                                try:
                                    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@id, 'text-area-') and contains(@id, '-input')]")))
                                    soal_input_text = driver.find_element(By.XPATH, "//*[contains(@id, 'text-area-') and contains(@id, '-input')]")
                                except:
                                    soal_input_text = False
                                if len(soalquiz) == 1 and soal_input_text:
                                    soal = driver.find_element(By.CLASS_NAME, classnya).find_element(By.CLASS_NAME, "rc-CML").text
                                    mode_jawaban_textarea = True
                                    print("[Mode Pertanyaan Isian]")
                                    
                                else:
                                    try:
                                        WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@id, 'text-area-') and contains(@id, '-input')]")))
                                        soal_input_text = driver.find_element(By.XPATH, "//*[contains(@id, 'text-area-') and contains(@id, '-input')]")
                                        soal = x.find_element(By.CLASS_NAME, "rc-CML").text
                                        soal_input_text.click()
                                        mode_jawaban_textarea = True
                                        print("[Mode Pertanyaan Isian]")
                                    except:
                                        soal = x.find_element(By.CLASS_NAME, "rc-CML").text
                                
                            except Exception as e:
                                print("errrrrrrrrrr", e)
                                
                            if mode_jawaban_textarea:
                                preprompt.append(f"{_+1}. {soal}")
                                
                            else:
                                opsi_mentah = x.find_elements(By.CLASS_NAME, "rc-Option")
                                try:
                                    for cekk in opsi_mentah:
                                        cek_type = cekk.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
                                        if cek_type:
                                            tipe_checkbox = "[This question is a complex multiple choice]"
                                except:
                                    tipe_checkbox = ""
                                opsi = "\n".join([opsinya.text for opsinya in opsi_mentah])
                                preprompt.append(f"{_+1}. {soal} {tipe_checkbox}\n{opsi}")
                         
                        if work_ai_1 > 2 and work_ai_2 > 2:
                            work_ai_1 = 1
                            work_ai_2 = 1
                            
                        if not yngsalah:
                            if mode_jawaban_textarea:
                                prompt = f"{preprompt}\nAnswer Using Subject 'I'"
                            else:
                                prompt = f"{preprompt}\nThis is a exam, I emphasize that only send the question number and the text of the correct answer. Example: '1. Answer\n2. Answer\netc'"
                            print("[Mendapatkan Kunci Jawaban...]")
                            jawaban = ai.getanswer(prompt).split("\n")
                            
                        else:
                            if work_ai_2 <= 2:
                                print("WRONG ANSWER: ",yngsalah)
                                # prompt = f"I emphasize that you re-send all correct answers (only nomor and answer: 'no. answer', example: '1. Answer\n2. Answer\netc', DONT ANOTHER WORD, DONT ARRAY), YOU MUST CHOOSE ANOTHER OPTION FOR THE WRONG OPTION\n{preprompt}\nAnswer: {jawabane}\n{yngsalah}"
                                prompt = f"You are tasked to re-send the correct answers in the format: 'no. answer', example: '1. Answer\n2. Answer\netc'. You must re-select the correct answer if the current one is wrong. Do not start with any word, do not send an array, and do not output any other words. Output only the answers in the format specified. Nothing else.\n{preprompt}\nAnswer: {jawabane}\nIncorrect: {yngsalah}\nSEND FORMAT 'No. Answer'"
                                print("[Mendapatkan Kunci Jawaban AI 1...]")
                                jawaban = ai2.getanswer(prompt).split("\n")
                                jawabane = []
                                if work_ai_2 >= 2:
                                    yngsalah = []
                                againlagi = not againlagi
                                work_ai_2 += 1
                                    
                            elif work_ai_1 <= 2:
                                print("WRONG ANSWER: ",yngsalah)
                                prompt = f"You are tasked to re-send the correct answers in the format: 'no. answer', example: '1. Answer\n2. Answer\netc'. You must re-select the correct answer if the current one is wrong. Do not start with any word, do not send an array, and do not output any other words. Output only the answers in the format specified. Nothing else.\n{preprompt}\nAnswer: {jawabane}\nIncorrect: {yngsalah}\nSEND FORMAT 'No. Answer'"
                                print("[Mendapatkan Kunci Jawaban AI 2...]")
                                jawaban = ai.getanswer(prompt).split("\n")
                                jawabane = []
                                if work_ai_1 >= 2:
                                    yngsalah = []
                                againlagi = not againlagi
                                work_ai_1 += 1
                                
                        jawabane.append(jawaban)
                        print("[Mengisi Opsi Jawaban...]")
                        try:
                            for index, x in enumerate(soalquiz):
                                if mode_jawaban_textarea:
                                    if len(soalquiz) == 1:
                                        print("[Send Keys Answer]") 
                                        try:
                                            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@id, 'text-area-') and contains(@id, '-input')]")))
                                            soal_input_textny = driver.find_element(By.XPATH, "//*[contains(@id, 'text-area-') and contains(@id, '-input')]")
                                            soal_input_textny.click()
                                            time.sleep(1)
                                            soal_input_textny.send_keys(" ".join(jawaban))
                                        except Exception as e:
                                            print("ERRRRRRR", e)
                                    else:
                                        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
                                        soal_input_textny = x.find_element(By.TAG_NAME, "textarea")
                                        soal_input_textny.click()
                                        time.sleep(1)
                                        soal_input_textny.send_keys(" ".join(jawaban))

                                else:
                                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "rc-Option")))
                                    print("[Memperoleh Semua Data Option]")
                                    opsi_mentah = x.find_elements(By.CLASS_NAME, "rc-Option")
                                    opsi_no_nomor = re.search(r"\d+\.\s*(.*)", jawaban[index]).group(1)
                                    try:
                                        opsi_kata = int(opsi_no_nomor)
                                    except:
                                        opsi_kata = ' '.join(opsi_no_nomor.split())
                                    
                                    for miss_out, click_jawaban in enumerate(opsi_mentah):
                                        if click_jawaban.text not in yngsalah:
                                            try:
                                                try:
                                                    teks_split = click_jawaban.text.split()
                                                    pilihan_opsi = click_jawaban.text
                                                except:
                                                    pilihan_opsi = click_jawaban.text
                                                    
                                                try:
                                                    if int(pilihan_opsi) == opsi_kata:
                                                        print(f"No.{index+1} Click Option: {click_jawaban.text}")
                                                        click_jawaban.click()
                                                        continue
                                                except:
                                                    if pilihan_opsi in opsi_kata:
                                                        print(f"No.{index+1} Click Option: {click_jawaban.text}")
                                                        click_jawaban.click()
                                                        continue
                                                    elif opsi_kata in click_jawaban.text:
                                                        print(f"No.{index+1} Click Option: {click_jawaban.text}")
                                                        click_jawaban.click()
                                                        break
                                                    elif miss_out >= len(opsi_mentah):
                                                        for click_again in opsi_mentah:
                                                            if click_again.text not in yngsalah:
                                                                try:
                                                                    try:
                                                                        teks_splitnya = click_again.text.split(" ")
                                                                        pilihan_opsinya = " ".join(teks_splitnya[-5:])
                                                                    except:
                                                                        pilihan_opsinya = click_again.text
                                                                    
                                                                    if pilihan_opsinya in opsi_kata:
                                                                        print(f"No.{index+1} Click Option: {click_again.text}")
                                                                        click_again.click()
                                                                        continue
                                                                    elif opsi_kata in click_again.text:
                                                                        print(f"No.{index+1} Click Option: {click_again.text}")
                                                                        click_again.click()
                                                                        break
                                                                    
                                                                except Exception as e:
                                                                    print("------------------------",e)
                                                                    print(f"No.{index+1} Click Option [except]: {click_again.text}")
                                                                    click_again.click()
                                                                    continue
                                                            
                                            except Exception as e:
                                                print("------------------------",e)
                                                print(f"No.{index+1} Click Option [except]: {click_jawaban.text}")
                                                click_jawaban.click()
                                                continue

                        except Exception as e:
                            print("[Mengulang Quiz...]")
                            try:
                                WebDriverWait(driver, 3).until(
                                    EC.element_to_be_clickable((By.NAME, "Tunnel Vision Close"))
                                ).click()
                            except:
                                WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Back']")))
                                driver.find_element(By.CSS_SELECTOR, "button[aria-label='Back']").click()
                            time.sleep(2)
                            continue
                        
                        try:
                            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "agreement-checkbox-base")))
                            driver.find_element(By.ID, "agreement-checkbox-base").click()
                        except:
                            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CLASS_NAME, "cds-checkboxAndRadio-label")))
                            driver.find_element(By.CLASS_NAME, "cds-checkboxAndRadio-label").click()
                        print("[Klik Checkbox]")
                        
                        time.sleep(2)
                        try:
                            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, "css-ra3hwj")))
                            driver.find_element(By.CLASS_NAME, "css-ra3hwj").click()
                        except:
                            pass
                        try:
                            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='cds-button-label' and text()='Submit']")))
                            driver.find_element(By.XPATH, "//span[@class='cds-button-label' and text()='Submit']").click()
                        except:
                            pass
                        try:
                            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//button[@data-testid='submit-button']")))
                            driver.find_element(By.XPATH, "//button[@data-testid='submit-button']").click()
                        except:
                            pass
                        print("[Klik Submit]")
                        
                        try:
                            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, "cds-Modal-container")))
                            againclick = driver.find_element(By.CLASS_NAME, "cds-Modal-container")
                            againclick.find_element(By.CLASS_NAME, "css-10bmx1s").click()
                        except:
                            pass
                            
                        print("[Proses Penilaian...]")
                        
                        if attemp_versilain:
                            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "css-1xkgrxp")))
                            indukan = driver.find_element(By.CLASS_NAME, "css-1xkgrxp")
                            grade = indukan.find_element(By.XPATH, ".//span[2]").text
                            
                            print(f"[QUIZ FINISHED] [{driver.current_url}]")
                            print(f"[Your Grade: {grade}]")
                            
                            if int(float(grade.strip('%'))) < target_nilai and htungkuis < 10:
                                WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "rc-FormPartsQuestion")))
                                hasilquiz = driver.find_elements(By.CLASS_NAME, "rc-FormPartsQuestion")
                                
                                for index, hasil in enumerate(hasilquiz):
                                    opsi_no_nomor = re.search(r"\d+\.\s*(.*)", jawaban[index]).group(1)
                                    hasil_jawaban = hasil.text
                                    if "Incorrect" in hasil_jawaban:
                                        yngsalah.append(f"No.{index+1} {opsi_no_nomor} is INCORRECT")
                                    elif "This should not be selected" in hasil_jawaban:
                                        yngsalah.append(f"No.{index+1} is type MULTIPLE CHOICE. PLEASE IDENTIFY AGAIN THE CORRECT ANSWER.")
                                    elif "You didn’t select all the correct answers" in hasil_jawaban:
                                        yngsalah.append(f"No.{index+1} is type MULTIPLE CHOICE. That Answer is CORRECT, BUT You didnt select all the correct answers. Please, vote more than ever in this question.")
                                        
                                print("[Mengulang Quiz...]")
                                htungkuis+=1
                                try:
                                    WebDriverWait(driver, 3).until(
                                        EC.element_to_be_clickable((By.NAME, "Tunnel Vision Close"))
                                    ).click()
                                except:
                                    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Back']")))
                                    driver.find_element(By.CSS_SELECTOR, "button[aria-label='Back']").click()
                                continue
                            
                            else:
                                nilai.append(f"[{linkquiz}]:\n[{grade}]")
                                if modequiz:
                                    break
                                else:
                                    try:
                                        nextitem = WebDriverWait(driver, 3).until(
                                            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.css-ra3hwj"))
                                        )
                                        if nextitem:
                                            nextitem.click()
                                            print("[Next]")
                                            continue
                                    except:
                                        pass
                                    
                                    try:
                                        try:
                                            WebDriverWait(driver, 3).until(
                                                EC.element_to_be_clickable((By.NAME, "Tunnel Vision Close"))
                                            ).click()
                                        except:
                                            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Back']")))
                                            driver.find_element(By.CSS_SELECTOR, "button[aria-label='Back']").click()
                                        time.sleep(2)
                                    except:
                                        pass
                                        
                        else:
                            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "css-bbd009")))
                            indukan = driver.find_element(By.CLASS_NAME, "css-bbd009")
                            grade = indukan.find_element(By.XPATH, ".//span[1]").text

                            print(f"[QUIZ FINISHED] [{driver.current_url}]")
                            print(f"[Your Grade: {grade}]")

                            if int(float(grade.strip('%'))) < target_nilai and htungkuis < 10:
                                WebDriverWait(driver, 300).until(EC.visibility_of_element_located((By.CLASS_NAME, "css-1h9exxh")))
                                semuahasil = driver.find_element(By.CLASS_NAME, "css-1h9exxh")
                                WebDriverWait(driver, 300).until(EC.visibility_of_element_located((By.CLASS_NAME, classnya)))
                                hasilquiz = semuahasil.find_elements(By.CLASS_NAME, classnya)
                                
                                for index, hasil in enumerate(hasilquiz):
                                    opsi_no_nomor = re.search(r"\d+\.\s*(.*)", jawaban[index]).group(1)
                                    hasil_jawaban = hasil.text
                                    if "Incorrect" in hasil_jawaban:
                                        yngsalah.append(f"No.{index+1} {opsi_no_nomor} is INCORRECT")
                                    elif "This should not be selected" in hasil_jawaban:
                                        yngsalah.append(f"No.{index+1} is type MULTIPLE CHOICE. PLEASE IDENTIFY AGAIN THE CORRECT ANSWER.")
                                    elif "You didn’t select all the correct answers" in hasil_jawaban:
                                        yngsalah.append(f"No.{index+1} is type MULTIPLE CHOICE. That Answer is CORRECT, BUT You didnt select all the correct answers. Please, vote more than ever in this question.")
                                        
                                print("[Mengulang Quiz...]")
                                htungkuis+=1
                                try:
                                    WebDriverWait(driver, 3).until(
                                        EC.element_to_be_clickable((By.NAME, "Tunnel Vision Close"))
                                    ).click()
                                except:
                                    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Back']")))
                                    driver.find_element(By.CSS_SELECTOR, "button[aria-label='Back']").click()
                                continue
                            else:
                                nilai.append(f"[{linkquiz}]:\n[{grade}]")
                                if modequiz:
                                    break
                                else:
                                    try:
                                        nextitem = WebDriverWait(driver, 3).until(
                                            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.css-ra3hwj"))
                                        )
                                        if nextitem:
                                            nextitem.click()
                                            print("[Next]")
                                            continue
                                    except:
                                        pass
                                    
                                    try:
                                        try:
                                            WebDriverWait(driver, 3).until(
                                                EC.element_to_be_clickable((By.NAME, "Tunnel Vision Close"))
                                            ).click()
                                        except:
                                            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Back']")))
                                            driver.find_element(By.CSS_SELECTOR, "button[aria-label='Back']").click()
                                        time.sleep(2)
                                    except:
                                        pass
                        
                    except:
                        pass
                    
                    try:
                        WebDriverWait(driver, 3).until(
                            EC.visibility_of_element_located(
                                (By.XPATH, "//button[@aria-label='Next Item']")
                            )
                        )
                        driver.find_element(
                            By.XPATH, "//button[@aria-label='Next Item']"
                        ).click()
                        print("[Next]")
                    except:
                        try:
                            WebDriverWait(driver, 3).until(
                                EC.visibility_of_element_located(
                                    (By.XPATH, "//button[@aria-label='Next Item']")
                                )
                            )
                            driver.find_element(
                                By.XPATH, "//button[@aria-label='Next Item']"
                            ).click()
                            print("[Next]")
                            continue
                        except:
                            break
                break
            
        except KeyboardInterrupt:
            print("[Proses dihentikan oleh pengguna]")
            continue
        
    print("COURSE SUDAH SELESAI DI BOT")
    for _, hasile in enumerate(nilai):
        print("==============================================================================================")
        print(f"[QUIZ {_+1}] {hasile}")
        print("==============================================================================================")
    again = input("Mau Input Course Lgi [y/n]? ")
    if again == "n" or again == "N":
        break
    print("\n")
