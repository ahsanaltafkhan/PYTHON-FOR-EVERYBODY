"""\nExtract Email Addresses\n\n"""\n\nimport re

text = "Contact a@example.com or support@example.org."
print(re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", text))\n