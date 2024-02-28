import openai
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

openai.api_key = "sk-JmlwEmWiNtFqSD7IDaF981Dd8a7447FfBcE768755cB38010"
openai.api_base = "https://api.keya.pw/v1"
def find_product_section(company_name):
    driver = webdriver.Chrome()  # 使用Chrome浏览器，确保已安装Chrome驱动程序并将其路径添加到系统PATH中
    driver.get("https://www.google.com")

    search_box = driver.find_element("name", "q")
    search_box.send_keys(company_name + " official website")
    search_box.send_keys(Keys.RETURN)


    try:
        official_website = driver.find_element(By.CSS_SELECTOR, ".g cite").text
        driver.get(official_website)

        # 等待一段时间，确保页面加载完成
        driver.implicitly_wait(5)
        driver.get(official_website)

        #all_elements = driver.find_element("xpath", "//*")
        ## 打印每个元素的tag name 和 text
        #print("元素标签名：", all_elements.text)
        #print("元素文本内容：", text)
        # 这里是一个示例，您可能需要根据实际网站结构来定位产品栏的链接

        try:
            product_link = driver.find_element("link text", "Products")
        except:
            product_link = None

        if product_link == None:
            try:
                product_link = driver.find_element("link text", "产品中心")
            except:
                product_link = None

        if product_link == None:
            try:
                product_link = driver.find_element("link text", "产品")
            except:
                product_link = None

        product_url = product_link.get_attribute("href")


    except Exception as e:
        print("Error:", e)
            product_url = None

    driver.quit()
    return product_url
  
# 示例用法
#company_name = "北京海光仪器有限公司"
company_name = "北京欧润科学仪器有限公司"
product_section_link = find_product_section(company_name)
if product_section_link:
    print(f"The product section link of {company_name} is: {product_section_link}")
else:
    print(f"Product section link not found for {company_name}")

driver = webdriver.Chrome()
driver.get(product_section_link)
#
# 获取页面文本内容并打印
page_text = driver.find_element("tag name", 'body').text
print("页面文本内容：", page_text)

question_system_prompt = """你是一个产品专家，下面是一个页面介绍，麻烦介绍一下页面中的产品"""
prompt = "请根据下面的网页页面文本内容介绍其对应的产品：\n" + page_text + "\n 只需要给出产品名字，不需要给出其它信息。"
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": question_system_prompt},
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.2
)
answer = response["choices"][0]["message"]["content"]
print(answer)
                                                                                                                                                                                                 90,13        底端

                                                                                   
