
def filter_users(user_data_list):
    result_list = []
    for user_tuple in user_data_list:
        user_id, user_name, age, country = user_tuple
        if age > 30 and (country == "USA" or country == "Canada"):
            result_list.append(user_name)
    return result_list

def analyze_user_list(users):
    users.sort(key=lambda x: x[2], reverse=True)
    oldest_users = users[:10]
    
    name_counts = {}
    for user in users:
        name = user[1]
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1
    
    repeated_names = [name for name, count in name_counts.items() if count > 1]
    return oldest_users, repeated_names

# Part 2 Functions


def count_unique(transaction_data):
    unique_ids = set()
    for data in transaction_data:
        if len(data) >= 4:
            unique_ids.add(data[1])
    return len(unique_ids)


def find_highest_transaction(trans_list):
    if not trans_list:
        return None
    max_trans = trans_list[0]
    for transaction in trans_list:
        if len(transaction) >= 4 and transaction[2] > max_trans[2]:
            max_trans = transaction
    return max_trans

def separate_ids_func(trans_data):
    trans_ids = []
    users_ids = []
    for item in trans_data:
        if len(item) == 4:
            trans_ids.append(item[0])
            users_ids.append(item[1])
        else:
            print("Error: Transaction data is not complete.")
    return trans_ids, users_ids

# Part 3 Functions

def visitors_both(pages_A, pages_B):
    return pages_A & pages_B

def visitors_xor(pages_A, pages_C):
    return pages_A ^ pages_C


def update_page(page, new_ids):
    page.update(new_ids)
    return page

def remove_ids(page, ids):
    page.difference_update(ids)
    return page

# Part 4 Functions


def sort_feedback(feed_dict):
    high_ratings = {}
    for key, value in feed_dict.items():
        if value['rating'] >= 4:
            high_ratings[key] = value['rating']

    sorted_ratings = sorted(high_ratings.items(), key=lambda item: item[1], reverse=True)[:5]
    return dict(sorted_ratings)


def combine_feedbacks(dicts_list):
    combined_feedback = {}
    for dict_item in dicts_list:
        for id, info in dict_item.items():
            if id in combined_feedback:
                combined_rating = max(info['rating'], combined_feedback[id]['rating'])
                combined_feedback[id] = {'rating': combined_rating, 'comments': combined_feedback[id]['comments'] + " " + info['comments']}
            else:
                combined_feedback[id] = info
    return combined_feedback


def create_high_rating_dict(feed_dict):
    result_dict = {}
    for id, info in feed_dict.items():
        if info['rating'] > 3:
            result_dict[id] = info['rating']
    return result_dict