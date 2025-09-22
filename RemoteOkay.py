
import requests
import pandas as pd
import webbrowser

url = "https://remoteok.com/api"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
data = response.json()
webbrowser.open("https://remoteok.com")

jobs = []
for job in data[1:]:  # first element is metadata
    jobs.append({
        "Job Title": job.get("position"),
        "Company": job.get("company"),
        "Location": job.get("location") or "Remote",
        "Tags": ", ".join(job.get("tags", [])),
        "Date Posted": job.get("date"),
        "Link": "https://remoteok.com" + job.get("url", "")
    })

df = pd.DataFrame(jobs)
print(df.head(10))
df.to_csv("remoteok_jobs.csv", index=False)

