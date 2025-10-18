import requests


def get_nav_from_mfapi(scheme_code):
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()
    # "data" is list of dicts with keys 'date' and 'nav'
    nav_list = data.get("data", [])
    #print(nav_list)
    scheme_category = data['meta']['scheme_category']
    print(scheme_category)
    if not scheme_category:
        scheme_category = "NA"
    if not nav_list:
        raise ValueError("No data found for scheme code")
    latest = nav_list[-1]
    return float(latest["nav"])



scheme_code = "118834"  # Axis Long Term Equity Fund
print(get_nav_from_mfapi(scheme_code))

# url = f"https://api.mfapi.in/mf/{scheme_code}"
# response = requests.get(url)
# data = response.json()

# fund_house = data['meta']['fund_house']
# scheme_type = data['meta']['scheme_type']
# scheme_category = data['meta']['scheme_category']

# print(scheme_category)