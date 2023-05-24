from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


loginURL     = "https://twitter.com/login"
hashTagURL   = "https://twitter.com/search?q=Pharaoh&src=trend_click&vertical=trends"
email        = ""
password     = ""
dataNameJSON = "Pharaoh.json"
trendName    = "Pharaoh"
delay        = 10
iterations   = 50   # almost 10 or 5 Tweets For Each Iteration


try:
    with open(dataNameJSON,'r+') as file:
        old = file.read()
        file.write('\n'+'')

except:
    with open(dataNameJSON,'w') as file:
        file.write('\n'+'')
        print('file Created')

# Initialize The Browser Interface
driver = webdriver.Chrome()

# Open the Base URL
driver.get(loginURL)

# Wait a Delay to Make Sure that The Page is Loaded
print(f"Delay: {delay}")
time.sleep(delay)

# Wait until Some Component Show Up on The Page
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[type='text']")))

#Enter Email and Click Login
driver.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys(email)
btn = driver.find_element(By.CSS_SELECTOR,"#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div:nth-child(6) > div")
btn.click()

# Wait until Some Component Show Up on The Page
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div.css-1dbjc4n.r-mk0yit.r-13qz1uu > div > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div.css-901oao.r-1awozwy.r-18jsvk2.r-6koalj.r-37j5jr.r-1inkyih.r-16dba41.r-135wba7.r-bcqeeo.r-13qz1uu.r-qvutc0 > input')))

# Enter the Password
driver.find_element(By.CSS_SELECTOR,'#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div.css-1dbjc4n.r-mk0yit.r-13qz1uu > div > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div.css-901oao.r-1awozwy.r-18jsvk2.r-6koalj.r-37j5jr.r-1inkyih.r-16dba41.r-135wba7.r-bcqeeo.r-13qz1uu.r-qvutc0 > input').send_keys(password)

# Wait until Some Component Show Up on The Page
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div.css-1dbjc4n > div > div > div')))

# Click Login
driver.find_element(By.CSS_SELECTOR,'#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div.css-1dbjc4n > div > div > div').click()

# Wait a Delay to Make Sure that The Page is Loaded
print(f"Delay: {delay}")
time.sleep(delay)

# Go To HashTag Page After Login
driver.get(hashTagURL)

# Extract the Data Just after The Page is Loaded
data = []
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(3) > div > section > div > div')))
tweets = driver.find_element(By.CSS_SELECTOR,'#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(3) > div > section > div > div')
repeat = 0
scrolltoTop = 0 
for i in range(iterations):
    try:
        alltweets = tweets.find_elements(By.TAG_NAME,'article')
        for twe in alltweets:
            try:
                autherName = twe.find_element(By.CSS_SELECTOR,'div[data-testid="User-Name"] a span').text
                autherID   = (twe.find_elements(By.CSS_SELECTOR,'div[data-testid="User-Name"] a span'))[3].text
                autherText = (twe.find_element(By.CSS_SELECTOR,'div[data-testid="tweetText"]').text).replace("\n"," ")
                tweetData  = {
                    "autherName":autherName,
                    "autherID":autherID,
                    "trend" : trendName,
                    "tweetText": autherText
                }
                
                if not (tweetData in data):
                    data.append(tweetData)
                    print(f"The Overall Data Collected is : {len(data)} in {i+1} Iteration")
                    repeat = 0
                    scrolltoTop = 0
                else:
                    repeat+=1
                    print(f"Repeated Data !! {repeat}")

                # Terminal if No New Data Is Being Collected
                if repeat > 10:
                    scrolltoTop+=1
                    driver.execute_script("window.scrollTo(0,window.scrollY-3000)")
                    if scrolltoTop >3:
                        print("Data is Being Repeated\nNo New Data Detected\nthe Code will Be Terminated ...")
                        break
                    repeat = 0

            except:
                 print(f"Error in tweet in {i}")
                 continue


        # Terminal if No New Data Is Being Collected
        if repeat > 10:
            print("Data is Being Repeated\nNo New Data Detected\nthe Code will Be Terminated ...")
            break
        with open(dataNameJSON,'w') as file:
            json.dump(data,file) 
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5*delay)
    except:
        print(f"Error in Iteration: {i}")
        continue
print('------------------------')
print("The Length Of Extracted Data is :",len(data))



with open('final.json','w') as file:
        json.dump(data,file) 
print("File Saved!")
print("The Proccess is Done, Close or Wait a Minute To Auto Close")
time.sleep(50)
driver.quit()