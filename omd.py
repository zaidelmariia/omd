
print("---------------------------------")
print("Задача 1")

moscow = {201, 202, 203, 204}
kazan = {203, 204, 205, 206}

print("---------------------------------")

print("что можно забрать в любом из двух городов")
print(set(moscow)&set(kazan))
print("---------------------------------")

print("что есть только в Москве")
print(set(moscow)-set(kazan))
print("---------------------------------")

print("что есть только в Казани")
print(set(kazan)-set(moscow))
print("---------------------------------")

print("сколько разных товаров на обоих складах вместе")
print(len(set(moscow)|set(kazan)))
print("---------------------------------")




print("---------------------------------")
print("Задача 2")

queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]

print("---------------------------------")

print("сколько всего поисковых запросов в ленте")
print(len(queries))
print("---------------------------------")

print("сколько раз ввели каждый запрос")
queries_dict = dict()
for query in queries:
    if query not in queries_dict:
        queries_dict[query] = 1
    else:
        queries_dict[query] += 1
print(queries_dict)
print("---------------------------------")

queries_set = set(queries)

print("какой запрос вводили чаще всего")
max_query_freq = 1
modal_query = queries[0]
for query in queries_set:
    if queries_dict[query] > max_query_freq:
        max_query_freq = queries_dict[query]
        modal_query = query
print(modal_query)
print("---------------------------------")

print("какую долю всех поисков он занимает")
freq_sum = 0
for query in queries_set:
    freq_sum += queries_dict[query]
print(max_query_freq/freq_sum)
print("---------------------------------")

print("какие запросы встретились один раз")
unique_queries = []
for query in queries_set:
    if queries_dict[query] == 1:
        unique_queries.append(query)
print(unique_queries)
print("---------------------------------")






print("---------------------------------")
print("Задача 3")
orders = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
]

print("---------------------------------")


print("на какую сумму оформили возвраты")
returns_sum = 0
for order in orders:
    if order["status"] == "returned":
        returns_sum += order["amount"] 
print(returns_sum)
print("---------------------------------")

print("кто хотя бы раз вернул заказ")
buyers_with_returns = set()
for order in orders:
    if order["status"] == "returned":
        buyers_with_returns.add(order["buyer"])
print(buyers_with_returns)
print("---------------------------------")

print("сколько заказов доставлено покупателю")
num_deliv_ord = 0
for order in orders:
    if order["status"] == "delivered":
        num_deliv_ord += 1
print(num_deliv_ord)
print("---------------------------------")

print("средний чек доставленных заказов")
deliv_orders_sum = 0
for order in orders:
    if order["status"] == "delivered":
        deliv_orders_sum += order["amount"] 
print(deliv_orders_sum/num_deliv_ord)
print("---------------------------------")





print("---------------------------------")
print("Задача 4")
days = [
    {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
]

print("---------------------------------")

print("выручка за всю неделю")
print(sum([day["revenue"] for day in days]))
print("---------------------------------")

print("день с самой большой выручкой")
max_rev = 0
max_rev_day = days[0]["day"]
for day in days:
    if day["revenue"] > max_rev:
        max_rev = day["revenue"]
        max_rev_day = day["day"]
print(max_rev_day)
print("---------------------------------")

print("средняя выручка на один заказ в каждый день")
print("считая только доставленные заказы")
print({day["day"] : day["revenue"]/(day["orders"] - day["returns"]) for day in days if day["orders"] - day["returns"]> 0})
print("считая все заказы")
print({day["day"] : day["revenue"]/day["orders"] for day in days if day["orders"] > 0})
print("---------------------------------")

print("дни, где возвратов больше 20% заказов")
print([day["day"] for day in days if day["orders"] != 0 and day["returns"]/day["orders"] > 0.2 ])
print("---------------------------------")




print("---------------------------------")
print("Задача 5")
reviews = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "Чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]

print("---------------------------------")


print("средняя оценка каждого товара")
products_set = set(rev["product"].lower() for rev in reviews)
sum_rate = {prod : [0,0] for prod in products_set} #первое число в паре - сумма звезд, второе - количество отзывов
for rev in reviews:
     sum_rate[rev["product"].lower()][0] += rev["stars"]
     sum_rate[rev["product"].lower()][1] += 1
avg_rate = {prod : sum_rate[prod][0]/sum_rate[prod][1] for prod in sum_rate.keys()}
print(avg_rate)
print("---------------------------------")

print("худший товар по средней оценке среди тех, у кого хотя бы два отзыва")
min_rate = 5
worst_prod = []
for prod in sum_rate.keys():
     if sum_rate[prod][1] >= 2:
        if avg_rate[prod] < min_rate:
            min_rate = avg_rate[prod]
for prod in avg_rate.keys():
    if avg_rate[prod] == min_rate:
        worst_prod.append(prod)
print(worst_prod)
print("---------------------------------")

print("сколько отзывов на 1 или 2 звезды")
rev_num_1_or_2 = sum([ 1 if rev["stars"] < 3 else 0 for rev in reviews])
print(rev_num_1_or_2)
print("---------------------------------")

print("какую долю всех отзывов они составляют")
print(rev_num_1_or_2 / len(reviews))
print("---------------------------------")
