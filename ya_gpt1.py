import requests
# To get token
# http://84.252.139.11:6969/iam_token


def get_yadex_gpt_response(message):
  IAM_TOKEN  = 't1.9euelZrPz43Pmc6cl5nIz47PypuYm-3rnpWalZ6WmJeWmpCWj8mQjpqTkYvl9Pd9CxpM-e9UTy-q3fT3PToXTPnvVE8vqs3n9euelZrMkMaUjYzKnpiSzpyXnpCdzu_8xeuelZrMkMaUjYzKnpiSzpyXnpCdzg.GaESMMjY5IE70RvhZmBbR714_bSACbm-NhvIUfeoBq_yn6bpAw3vMtpPDRrbOmhZhz91og9lHt9nfQnABc0aDw'
  ID_YC_USER = 'b1gjk1e4ulv69rmqmo4f'
  headers = {
      'Authorization': f'Bearer {IAM_TOKEN}',
      'x-folder-id': ID_YC_USER,
      'Content-Type': 'application/json'
      }


  body = {
      "modelUri": f"gpt://{ID_YC_USER}/yandexgpt-lite",
      "completionOptions": {
        "stream": False,
        "temperature": 0.6,
        "maxTokens": "2000"
      },
      "messages": [
        {
          "role": "user",
          "text": message
        }
      ]
    }


  url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'
  res = requests.post(url, headers=headers, json=body)
  return res.json()['result']['alternatives'][0]['message']['text']

if __name__ == "__main__":
    print(get_yadex_gpt_response('Кто такой джордано бруно?'))