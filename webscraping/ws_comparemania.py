from bs4 import BeautifulSoup
import requests

URL = "https://www.comparemania.com.br/cashback-amazon#google_vignette"

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0 (Edition utorrent)"
}

response = requests.get(URL, headers=headers)

message = '';

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'lxml')

    tables = soup.find_all('table', class_='table table-striped')

    if len(tables) >= 2:
        milhas, cashbacks = tables[0], tables[1]

        def extract_data(table, second_td_has_span=True):
            results = []  

            for line in table.find_all('tr'):
                div = line.find('div', class_='d-grid')
                td_text = None

                if div:
                    span = div.find('span')

                    if span:
                        tds = line.find_all('td')

                        if len(tds) >= 2:
                            if second_td_has_span:
                                spans = tds[1].find_all('span')

                                filtered_spans = [span for span in spans if 'badgeGreen' not in span.get('class', [])]

                                if filtered_spans:
                                    td_text = filtered_spans[0].text.strip()
                            else:
                                td_text = tds[1].text.strip()

                        results.append((span.text, td_text))

            return results

        milhas_results = extract_data(milhas, second_td_has_span=True)
        cashbacks_results = extract_data(cashbacks, second_td_has_span=False)

        message += ">>> Lista de parceiros Amazon <<<\n"
        message += "\n"
        message += "Programa - Pontuação\n"
        for span_text, td_text in milhas_results:
            message += f"{span_text.ljust(8,' ')} - {td_text}\n"
        message += "\n"
        message += "Programa     - Cashback\n"
        for span_text, td_text in cashbacks_results:
            message += f"{span_text.ljust(12,' ')} - {td_text}\n"

    else:
        print("Não foram encontradas tabelas suficientes.")
else:
    print(f"Falha ao acessar a página. Status code: {response.status_code}")

bot_token = "6401646362:AAGC1GCu778u9YSj1Q1IiV117GmfrBePFm4"
chat_id = "2075341659"

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
payload = {
    "chat_id": chat_id,
    "text": message
}

response = requests.post(url, data=payload)

if response.status_code == 200:
    print("Mensagem enviada com sucesso!")
else:
    print(f"Falha ao enviar mensagem: {response.status_code}")