import json

# 點菜
template_type = input('請輸入要設定的客戶是Only GA4 或 UA+GA4\n').lower()
print(template_type)
while template_type != 'only ga4' and template_type != 'ua+ga4':
    template_type = input("""
    無法判斷，請重新輸入並注意空格或加號(無視大小寫)
    請輸入要設定 'Only GA4' 或 'UA+GA4'
    """).lower()
    print(template_type)

# 讀檔
if template_type == 'ua+ga4':
    a_file = open(r"./file/TEMPLATE/UA+GA4 TEMPLATE.json", "r", encoding="utf-8")  # 是相對路徑，記得進到資料夾
elif template_type == 'only ga4':
    a_file = open(r"./file/TEMPLATE/Only GA4 TEMPLATE.json", "r", encoding="utf-8")  # 是相對路徑，記得進到資料夾
else :
    print(f'找不到範本檔，或是程式錯誤(version = {template_type})')
    xx = input()  #  卡一個input讓視窗不關閉，但還是關了ㄎ
json_object = json.load(a_file)
a_file.close()
json_object_new = json.dumps(json_object)

# 編寫
cus_Gtag = input('請貼上MEASUREMENT ID，例：G-ABC123ZXC0\n')
cus_domain = input('請貼上客戶網址，不用www跟之前的東西。例：example.com.tw\n')
json_object_new = json_object_new.replace('G-toBechange', cus_Gtag)
json_object_new = json_object_new.replace('clientsDomain', cus_domain)
if template_type == 'ua+ga4':
    cus_UAtag = input('請貼上UAID，例：UA-123456789-0\n')
    json_object_new = json_object_new.replace('UA-toBeChan-ge', cus_UAtag)

'''
確定可用但改用replace
json_object_new = json_object
json_object_new["containerVersion"]["variable"][4]["parameter"][0]["value"] = cus_Gtag
json_object_new["containerVersion"]["variable"][0]["parameter"][8]["value"] = cus_UAtag
'''

# 存檔
json_object_new = json.loads(json_object_new)
template_type_formatted = json_object_new["iSB_comment"]
a_file = open(f"{cus_domain.replace('.','')}_{template_type_formatted}.json", "w")  # 不用encode匯入後也是中文
json.dump(json_object_new, a_file)  # 不用indent也可以成功匯入
a_file.close()
print('JSON檔案已建立')

'''
在 terminal輸入'pyinstaller code.py' 來製作exe檔
再用bat製作相對路徑檔案在外層
所有input都可以再優化，取掉空白換行等等，可以直接寫function
'''