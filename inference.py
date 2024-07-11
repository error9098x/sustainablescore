import requests

def run_inference(query):
    api_url = "http://34.16.234.21:5432/Chat"
    headers = {"Content-Type": "application/json"}

    data = {"query": query}
    response = requests.post(api_url, headers=headers, json=data)

    # Handle the response
    if response.status_code == 200:
        raw_text = response.text

        # Trim the response to include only JSON content
        start_idx = raw_text.find('{')
        end_idx = raw_text.rfind('}') + 1  # +1 to include the closing brace

        if start_idx == -1 or end_idx == -1:
            raise ValueError("The response does not contain valid JSON")
            
        trimmed_text = raw_text[start_idx:end_idx]
        return trimmed_text
    else:
        response.raise_for_status()

# Example usage (assuming the query is stored in a variable named `prompt`):
# prompt = "Your prompt here"
# result = run_inference(prompt)
# print(result)