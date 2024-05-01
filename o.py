url ='https://rozetka.com.ua/promo/bigeastersale/?gad_source=1&section_id=4627858'


def url_query():
    url_query ='source=1&section_id=4627858'
    query= url_query.split('_')
    print(query)
    dict_query = {}
    for element in query:
        key,value = element.split('=')
        dict_query.update({key:value})
    return dict_query

def clear():
    result_list = []
    for key in url_query():
        result_list.append(key + '=' + url_query()[key])
    result = '_'.join(result_list)
    return result



if __name__ == "__main__":
    print(url_query())
    print(clear())


