import requests
import json

def request(sent, token):
    res = requests.post("http://140.116.245.157:2001", data={"data":sent, "token":token})
    if res.status_code == 200:
        return json.loads(res.text)
    else:
        return None
    
def open_file(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.readlines()
    return content

ner_list = open_file("ner.txt")
ner_list = [item.replace('\n', '') for item in ner_list]

def create_dict(data_list):
    word_dict = {}
    repeat = []
    index = 0
    for item in data_list:
        index += len(item)
        if item in word_dict.keys():
            repeat.append((item, index - 1))
        else:
            word_dict[item] = ""
    # print(repeat)   
    return word_dict, repeat

############################################ DATA ##############################################

norp = ["阿美族", "排灣族", "泰雅族", "布農族", 
        "太魯閣族", "卑南族", "魯凱族", "賽德克族", 
        "鄒族", "賽夏族", "雅美族", "噶瑪蘭族", 
        "撒奇萊雅族", "邵族", "拉阿魯哇族", "卡那卡那富族"]
percent = ["百分之", "%", "％"]
time = ["年", "月", "日", "時", "點",
        "分", "分鐘", "秒", "秒鐘", "週", "季",
        "年度", "月份", "時期", "時段"]
date = ["年", "月", "日", "號", "節", "世紀"]
event = ["事件", "戰爭"]
money = ["元", "塊", "美金", "日圓", "韓元", "歐元", "英鎊", "澳幣", "新加坡幣", "港幣", "人民幣", "台幣"]
language = ["中文", "英文", "日文", "韓文", 
            "法文", "德文", "俄文", "西班牙文", 
            "葡萄牙文", "義大利文", "荷蘭文", "希臘文", 
            "瑞典文", "挪威文", "丹麥文", "芬蘭文", 
            "捷克文", "匈牙利文", "波蘭文", "土耳其文", 
            "阿拉伯文", "希伯來文", "波斯文", "印度文", 
            "泰文", "越南文", "印尼文", "馬來文", 
            "菲律賓文", "緬甸文", "柬埔寨文", "蒙古文", 
            "藏文", "尼泊爾文", "僧加羅文", "緬甸文", 
            "老撾文", "孟加拉文", "巴斯克文", 
            "加泰隆尼亞文", "加利西亞文", "巴斯克文", 
            "阿爾巴尼亞文", "保加利亞文", "克羅埃西亞文", 
            "愛沙尼亞文", "拉脫維亞文", "立陶宛文", 
            "斯洛維尼亞文", "斯洛伐克文", "塞爾維亞文", 
            "波斯尼亞文", "黑山文", "馬其頓文", "阿爾巴尼亞文", 
            "克羅埃西亞文"]
law = ["民法", "刑法", "憲法", "商法", "法", "條例", "公約", "法案", "法典"]
ordinal = ["第一", "第二", "第三", "第四", 
           "第五", "第六", "第七", "第八", "第九", 
           "第十", "第", "No.", "Top"]
org = ["組織", "台灣合作社", "基金會", "協會", 
       "公會", "盟", "會", "救國團", "機構", 
       "聯合國", "領事館", "院", "總部", "部", "處",
       "局", "署", "所", "社", "會", "公司", "企業",
       "集團", "行", "商行", "行號", "銀行", "信用合作社",
       "保險公司", "證券公司", "證券商", "證券投資信託公司",
       "新聞", "報", "雜誌", "刊", "台灣報", "中央社", "大學"]
quantity = ["公斤", "公噸", "公克", "毫升", 
            "升", "斤", "磅", "盎司", "加侖", 
            "夸脫", "公分", "公尺", "公里", 
            "英吋", "英尺", "英碼", "英里", 
            "海里", "英寸"]
loc = ["美洲", "歐洲", "亞洲", "非洲", "澳洲", "南極洲"]
gpe = open_file("gpe.txt")
gpe = [item.replace('\n', '') for item in gpe]

################################################################################################

''' Check Functions '''
def check_norp(word):
    if word in norp:
        return True
    for item in norp:
        if item in word:
            return True
    return False
    
def check_percent(word):
    if word in percent:
        return True
    for item in percent:
        if item in word:
            return True
    return False

def check_time(word, pos):
    if word in time:
        return True
    for item in time:
        if item in word and word[-len(item):] == item:
            if pos == "Nd" or pos == "Neu":
                return True
            else:
                return False
    return False

def check_date(word, pos):
    if word in date:
        return True
    for item in date:
        if item in word and word[-len(item):] == item:
            return True
    return False

def check_event(word):
    if word in event:
        return True
    for item in event:
        if item in word:
            return True
    return False

def check_money(word):
    if word in money:
        return True
    for item in money:
        if item in word:
            return True
    return False

def check_language(word):
    if word in language:
        return True
    for item in language:
        if item in word:
            return True
    return False

def check_law(word):
    if word in law:
        return True
    for item in law:
        if item in word:
            return True
    return False

def check_ordinal(word):
    if word in ordinal:
        return True
    for item in ordinal:
        if item in word:
            return True
    return False

def check_org(word):
    if word in org:
        return True
    for item in org:
        if item in word and word[-len(item):] == item:
            return True
    return False

def check_quantity(word):
    if word in quantity:
        return True
    for item in quantity:
        if item in word:
            return True
    return False

def check_loc(word):
    if word in loc:
        return True
    for item in loc:
        if item in word:
            return True
    return False

def check_gpe(word):
    if word in gpe:
        return True
    for item in gpe:
        if item in word:
            return True
    return False

''' Check Functions End'''

''' Analysis Function End'''
def analysis_ws_pos(ws_data, pos_data):
    ws_dict, repeat = create_dict(ws_data)
    for word, pos in zip(ws_data, pos_data):
        if pos == "Nd": # 時間詞
            if check_date(word, pos):
                ws_dict[word] = "DATE"
            elif check_time(word, pos):
                ws_dict[word] = "TIME"
        elif pos == "Neu": # 數詞定詞
            if check_time(word, pos):
                ws_dict[word] = "TIME"
            elif check_date(word, pos):
                ws_dict[word] = "DATE"
            elif check_money(word):
                ws_dict[word] = "MONEY"
            elif check_quantity(word):
                ws_dict[word] = "QUANTITY"
            elif check_ordinal(word):
                ws_dict[word] = "ORDINAL"
            else:
                ws_dict[word] = "CARDINAL"
        elif pos == "Nc": # 地名詞
            if check_norp(word):
                ws_dict[word] = "NORP"
            elif check_loc(word):
                ws_dict[word] = "LOC"
            elif check_gpe(word):
                ws_dict[word] = "GPE"
            elif check_org(word):
                ws_dict[word] = "ORG"
        elif pos == "Nf":
            if check_percent(word):
                ws_dict[word] = "PERCENT"
            elif check_ordinal(word):
                ws_dict[word] = "ORDINAL"
            elif check_quantity(word):
                ws_dict[word] = "QUANTITY"
            elif check_time(word, pos):
                ws_dict[word] = "TIME"
        elif pos == "Nb":
            if check_norp(word):
                ws_dict[word] = "NORP"
            elif check_loc(word):
                ws_dict[word] = "LOC"
            elif check_event(word):
                ws_dict[word] = "EVENT"
            elif check_gpe(word):
                ws_dict[word] = "GPE"
            elif check_org(word):
                ws_dict[word] = "ORG"
            elif check_law(word):
                ws_dict[word] = "LAW"
            elif check_language(word):
                ws_dict[word] = "LANGUAGE"
            else:
                ws_dict[word] = "PERSON"
        elif pos == "Neqa":
            if check_percent(word):
                ws_dict[word] = "PERCENT"
        elif pos == "FW":
            if check_ordinal(word):
                ws_dict[word] = "ORDINAL"
        elif pos == "Na":
            if check_norp(word):
                ws_dict[word] = "NORP"
            elif check_loc(word):
                ws_dict[word] = "LOC"
            elif check_gpe(word):
                ws_dict[word] = "GPE"
            elif check_org(word):
                ws_dict[word] = "ORG"
            elif check_language(word):
                ws_dict[word] = "LANGUAGE"
            elif check_law(word):
                ws_dict[word] = "LAW"
            elif check_event(word):
                ws_dict[word] = "EVENT"
            elif check_date(word, pos):
                ws_dict[word] = "DATE"
            elif check_time(word, pos):
                ws_dict[word] = "TIME"
            
    return ws_dict, repeat

''' Analysis Function End'''

if __name__ == "__main__":
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJleHAiOjE3MjUxNTQwNTIsImF1ZCI6IndtbWtzLmNzaWUuZWR1LnR3IiwidmVyIjowLjEsInNjb3BlcyI6IjAiLCJzZXJ2aWNlX2lkIjoiMSIsInVzZXJfaWQiOiI0OTQiLCJpc3MiOiJKV1QiLCJpZCI6NzA2LCJpYXQiOjE3MDk2MDIwNTIsIm5iZiI6MTcwOTYwMjA1Miwic3ViIjoiIn0.vD_F7xIueK-dOhUGpxEQxV34ZOoOGhR8rAKjubhu_zx_6YtyO6D9xYiWHL3ctZjbP8YbuZMIjd_CA72gaIP1VFR_quvbDiK5K6Aice2oZeivjKqFtRSeoCrgm6PHvWtCIe99XSsd-uQvYp9NtmCVXVsU883ffzPoH1FKXoNG-L8"
    sent = "「《發言的勇氣》充滿了魅力和原創性，帶著清晰的批判精神和溫柔的推力，就像你最好的商業夥伴，在耳邊輕輕督促你，勇敢大膽地說出心聲、掌控全場。」—凱洛琳‧希爾德（Carolyn Hilders），領導聯盟（Chief）共同創始人暨執行長，以及琳西‧卡普蘭（Lindsay Kaplan），領導聯盟共同創始人暨品牌長"
    r = request(sent, token)

    print(r)
    # print(r['ws'][0])

    ''' Process string -> Combine some noun '''
    noun_na = ""
    noun_neu_nf = ""
    noun_list = []
    for ws, pos in zip(r['ws'][0], r['pos'][0]):
        if pos == "Na":
            noun_na += ws
        elif pos == "Neu" or pos == "Nf":
            noun_neu_nf += ws
        else:
            # usually Neu + Nf + Na not Na + Neu + Nf
            if noun_na != "" and noun_neu_nf != "":
                noun_list.append(noun_neu_nf)
                noun_list.append(noun_na)
                noun_na = ""
                noun_neu_nf = ""
                noun_list.append(ws)
                continue

            if noun_na != "":
                noun_list.append(noun_na)
                noun_na = ""

            if noun_neu_nf != "":
                noun_list.append(noun_neu_nf)
                noun_neu_nf = ""
            noun_list.append(ws)
    # Neu + Nf befoer Na
    if noun_neu_nf != "":
        noun_list.append(noun_neu_nf)
    if noun_na != "":
        noun_list.append(noun_na)
    print(noun_list)
    ''' Process string -> Combine some noun End '''

    ''' Analysis word and pos '''
    rst_dict, rep = analysis_ws_pos(r['ws'][0], r['pos'][0])
    print(rst_dict)
    ''' Analysis word and pos End '''

    ''' Final Check '''
    end = 0
    for k, v in rst_dict.items():
        end += len(k)
        for rep_word, rep_index in rep:
            if rep_index == end:
                end += len(rep_word)
                break
        if v != "":
            for n in noun_list:
                if k in n or k == n:
                    print(f"{n} -> {v}")
                    break
    ''' Final Check End '''
    
    ''' ART_OF_WORK '''
    pre = 0
    if "《" in noun_list:
        for i in range(noun_list.index("《"), len(noun_list)):
            if "《" in noun_list[i]:
                pre = i
            if "》" in noun_list[i]:
                print(f"{''.join(noun_list[pre:i+1])} -> ART_OF_WORK")
                pre = 0
    ''' ART_OF_WORK End '''
