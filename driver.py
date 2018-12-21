import primeradiant as pr

text = pr.url_to_text('https://www.wired.com/story/inside-the-pentagons-plan-to-win-over-silicon-valleys-ai-experts/')
print(pr.scan(text))
