import wolframalpha

app_id = "QKK8K9-U7AQ3Q4T3H"
client = wolframalpha.Client(app_id)

res = client.query('((z^3)/((z-2i)^3(2+5i)^4)),z=4i')
print(next(res.results).text)