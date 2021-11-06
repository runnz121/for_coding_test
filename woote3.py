def solution(ings, menu, sell):
    answer = 0
    ing_list = dict()
    menu_list = dict()
    sell_list = dict()

    for i in ings:
        ing = i.split()
        name_ing = ing[0]
        name_val = int(ing[1])
        ing_list[name_ing] = [name_val]

    for j in menu:
        men = j.split()
        men_name = men[0]
        men_ings = men[1]
        men_price = int(men[2])
        menu_list[men_name] = [men_ings, men_price]


    for k in sell:
        sel = k.split()
        sel_name = sel[0]
        sel_price = int(sel[1])
        sell_list[sel_name] = [sel_price]

    sums = 0
    for x in menu_list.keys():
        men = menu_list.get(x)[0]
        for j in men:
            for k in ing_list.keys():
                if j == k:
                    sums += ing_list.get(j)[0]
        sums = menu_list.get(x)[1] - sums
        menu_list[x] = [sums]


    return answer

#1161
ings =["r 10", "a 23", "t 124", "k 9"]
menu =["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"]
sell =["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]

#-80
ings1=["x 25", "y 20", "z 1000"]
menu1=["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"]
sell1=["BBBB 3", "TTT 2"]

print(solution(ings, menu, sell))

# product = dict()
# sell_dict = dict()
# ing_spi = dict()
# ingre_prices_total = 0
#
# for i in menu:
#     menus = i.split()
#     name = menus[0]
#     ingre = menus[1]
#     name_price = int(menus[2])
#     for k in ingre:
#         for x in ings:
#             ings_spl = x.split()
#             ing_name = ings_spl[0]
#             ing_price = int(ings_spl[1])
#             ing_spi[ing_name] = [ing_price]
#             if k == ing_spi.keys():
#                 ingre_prices_total += ing_spi.get(k)[0]
#                 print(ingre_prices_total)
#     product[name] = [ingre, name_price, ingre_prices_total]
# # print(product)
# # print(product.get("PIZZA"))
#
#
# # for k in ings:
# #     ingss = k.split()
# #     ing_name = ingss[0]
# #     ing_price = int(ingss[1])
# #     ing_spi[ing_name] = [ing_price]
#
#
# for i in sell:
#     sells = i.split()
#     sell_menu = sells[0]
#     sell_price = int(sells[1])
#     sell_dict[sell_menu] = [sell_price]
#
# #
# # for x in product.keys():
# #     ingsss = product(x)[1]
# #     for j in ingsss:
# #         if j == ing_spi.keys():
# #             total_ing_price = ing_spi.get(j)[0]
# #             print(total_ing_price)
#
#
# total = 0
# for i in sell_dict.keys():
#     for j in product.keys():
#         if i == j:
#             total = product.get(j)[1] * sell_dict.get(i)[0]
#             # print(total, i)
#
