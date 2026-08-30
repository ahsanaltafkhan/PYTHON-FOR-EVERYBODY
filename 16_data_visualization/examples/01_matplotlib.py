"""\nBasic Visualization\n\n"""\n\ntry:
    import matplotlib.pyplot as plt
except ImportError:
    raise SystemExit("Install dependencies with: pip install -r requirements.txt")

months = ["Jan", "Feb", "Mar", "Apr"]
values = [10, 14, 12, 19]
plt.plot(months, values, marker="o")
plt.title("Example Trend")
plt.xlabel("Month")
plt.ylabel("Value")
plt.show()\n