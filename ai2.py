import requests, time, sys, string, random, re
import json


hashnya = "3a77cbriih5"
url = "https://qwen-qwen2-72b-instruct.hf.space/queue/join?__theme=light"
url_res = "https://qwen-qwen2-72b-instruct.hf.space/queue/data?session_hash="+hashnya
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",
}
hist = []
n=1
def getanswer(soal):
    teks = soal
    
    print("AI : ")
    # Data JSON yang dikirim
    data = {
        "data": [
            teks,
            hist,
            "You are a helpful assistant."
        ],
        "event_data": "null",
        "fn_index": 0,
        "trigger_id": 12,
        "session_hash": hashnya
    }
    
    requests.post(url, json=data, headers=headers)
    
    start_time = time.time()
    berhenti=False
    respon = ""
    try:
        with requests.get(url_res, stream=True) as get_res1:
            for chunk in get_res1.iter_content(chunk_size=1280000000000):
                if chunk:
                    data_string = chunk.decode('utf-8')
                    messages = data_string.split('\n\ndata: ')
                    if "process_completed" in data_string:
                        berhenti = True
                    for mess in messages:
                        if "process_generating" in mess:
                            try:
                                mesh = re.sub(r'^data: ', '', mess)
                                jsonnya = json.loads(mesh)
                                if 'output' in jsonnya and 'data' in jsonnya['output']:
                                    data_list = jsonnya['output']['data'][1]
                                    for item in data_list:
                                        if isinstance(item, list) and len(item) > 1:
                                            text_value = item[1] 
                                            if isinstance(text_value, str):
                                                if all(i[1] != text_value for i in hist):
                                                    print(text_value, end="", flush=True)
                                                    respon += text_value
                                                    break
                            except:
                                pass
                    for message in messages:
                        if berhenti:
                            sys.exit()
                        if "process_generating" in message:
                            try:
                                meshh = re.sub(r'^data: ', '', message)
                                jsonnyaa = json.loads(meshh)
                                if 'output' in jsonnyaa and 'data' in jsonnyaa['output']:
                                    data_listt = jsonnyaa['output']['data'][1]
                                    for item in data_listt:
                                        if isinstance(item, list) and len(item) > 1:
                                            text_value = item[2]  
                                            if isinstance(text_value, str) and text_value not in hist: 
                                                print(text_value, end="", flush=True)
                                                respon += text_value
                            except:
                                pass
    except:
        print("\n")
    hist.append([teks, respon])
    end_time = time.time()
    print(f"Waktu respons: {end_time - start_time:.3f} detik\n")
    return respon
    