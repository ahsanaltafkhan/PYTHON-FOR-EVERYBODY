"""\nJSON\n\n"""\n\nimport json

data = {"name": "Ahsan", "skills": ["Python", "AI"]}
text = json.dumps(data, indent=2)
print(text)
print(json.loads(text)["skills"])\n