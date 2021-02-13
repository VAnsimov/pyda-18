import json

def main():
    logs = convert_log_to_json('purchase_log.txt')
    combine_logs_and_file(logs, 'visit_log.csv')

def convert_log_to_json(file: str) -> dict:
    logs = dict()

    with open(file, mode='r') as purchase_log_file:

        # skipping the first line
        purchase_log_file.readline()

        for line in purchase_log_file:
            log_json = json.loads(line)
            user_id_key = 'user_id'
            category_key = 'category'

            if user_id_key not in log_json \
                or category_key not in log_json:
                continue

            user_id = log_json[user_id_key]
            category =  log_json[category_key]

            logs.setdefault(user_id, [])
            logs[user_id].append(category)

    return logs

def combine_logs_and_file(logs: dict, file: str):
    with open(file, mode='r') as file:
        with open('funnel.csv', mode='w') as funnel_file:

            first_line = file.readline().strip()
            funnel_file.write(first_line + ',purchase_category\n')

            for index, origin_line in enumerate(file):
                line = origin_line.strip().split(',')

                if len(line) != 2:
                    continue

                user_id = line[0]

                if user_id in logs:
                    # when writing with spaces, macos big sur does not read csv correctly
                    category = ' & '.join(logs[user_id]).replace(' ', '_')
                    line.append(category)

                if len(line) > 2:
                    result = ','.join(line) + '\n'
                    funnel_file.write(result)

main()