    # HOW to use it:
    #run the command: "python auto_query.py http://your-train-ticket-url.com 10000"

import time
import sys
import random
from collections import defaultdict
from queries import Query
# Import necessary functions from the modules
from scenarios import query_and_preserve
from scenarios import query_and_cancel
from scenarios import query_and_collect
from scenarios import query_and_execute
from scenarios import query_and_consign
from scenarios import query_and_pay
from scenarios import query_and_rebook
from scenarios import query_and_rebook
# from query_and_collect_ticket import query_and_collect_ticket
# from query_travel_left import query_travel_left
# from query_admin_basic_config import query_admin_basic_config
# from query_admin_basic_price import query_admin_basic_price
# from query_advanced_ticket import query_advanced_ticket
# # from query_advanced_ticket import query_advanced_ticket
# # from query_and_cancel import query_and_cancel
# # from query_and_collect_ticket import query_and_collect_ticket
# # from query_and_enter_station import query_and_enter_station
# # from query_and_preserve import query_and_preserve
# # from query_and_put_consign import query_and_put_consign
# from query_and_rebook import query_and_rebook
# from query_food import query_food
# # from query_order_and_pay import query_order_and_pay
# from query_route import query_route
from query_travel_left_parallel import query_travel_left_parallel
from query_travel_left import query_travel_left

# Import more functions as needed

# List of functions to be executed randomly
function_list = [
    query_and_preserve,

    query_and_cancel,
    query_and_collect,
    query_and_execute,
    query_and_consign,
    query_and_pay,
    query_and_rebook,

    # query_and_collect_ticket,
    # query_travel_left,
    # query_admin_basic_config,
    # query_admin_basic_price,
    # query_advanced_ticket,
    # query_and_cancel,
    # query_and_collect_ticket,
    # query_and_enter_station,
    # query_and_put_consign,
    # query_and_rebook,
    # query_food,
    # query_order_and_pay,
    # query_route,
    # query_travel_left_parallel,
    # query_travel_left
]

# Create a defaultdict to store the counts of each function
function_counts = defaultdict(int)

def main(url, n_times):
    q = Query(url)
    
    if not q.login():
        print('Login failed')
        return
    
    for i in range(n_times):
        # Randomly select a function to execute
        random_function = random.choice(function_list)

        #test
        # print(random_function)

        # Execute the selected function
        random_function(q)

        # time.sleep(5)

        # Increment the count for the executed function
        function_counts[random_function.__name__] += 1

        print(f"Execution {i+1}/{n_times} of {random_function.__name__} completed.")


    # Print the counts of each function
    print("\nFunction counts:")
    for function_name, count in function_counts.items():
        print(f"{function_name}: {count}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <URL> <N_TIMES>")
        sys.exit(1)
    
    url = sys.argv[1]
    n_times = int(sys.argv[2])

    main(url, n_times)








# ###
# import logging
# from queries import Query
# from scenarios import query_and_preserve

# # 设置日志
# logging.basicConfig(level=logging.INFO)

# # 设置查询的 URL
# url = "https://example.com"

# # 创建查询对象
# g = Query(url)

# # 登录并存储 Cookie
# if not g.login():
#     logging.fatal('登录失败')
#     exit()

# # 定义要执行的查询和场景
# queries_and_scenarios = [
#     ("query_high_speed_ticket", "preserve"),
#     # 在这里添加更多的查询和场景，例如：("query_cancel_ticket", "preserve")
# ]

# # 循环执行查询和场景
# for query_name, scenario_name in queries_and_scenarios:
#     query_function = getattr(g, query_name, None)
#     scenario_function = getattr(query_and_preserve, scenario_name, None)

#     if query_function and scenario_function:
#         logging.info(f"执行查询 {query_name} 并应用场景 {scenario_name}")
#         query_function()
#         scenario_function(g)
#     else:
#         logging.warning(f"无效的查询或场景：{query_name}, {scenario_name}")

# logging.info("所有查询和场景执行完成")
# ###