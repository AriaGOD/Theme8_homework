import csv

# пути к файлам
csv_file_path = 'Вставить сюда путь до csv файла'
txt_file_path = 'Вставить сюда путь до txt файла'

try:
    # чтение csv
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)


    # описание клиента
    def generate_description(row):
        age = row.get('age', '')
        age_description = age.strip() if age.strip() else 'None'
        if age_description != 'None':
            try:
                age_description = str(int(float(age)))
            except ValueError:
                age_description = 'None'

        return (
            f"Customer Name: {row.get('name', 'Unknown')}\n"
            f"Gender: {row.get('sex', 'Unknown').capitalize()}\n"
            f"Age: {age_description}\n"
            f"Device Used: {row.get('device_type', 'Unknown')}\n"
            f"Browser: {row.get('browser', 'Unknown')}\n"
            f"Purchase Amount: ${float(row.get('bill', 0)):.2f}\n"
            f"Region of Purchase: {row.get('region', 'Unknown')}\n"
            "----------------------------------------\n"
        )

    # генерация описаний
    descriptions = [generate_description(row) for row in rows]

    # запись в txt
    with open(txt_file_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(descriptions)

    print(f"Descriptions saved to {txt_file_path}")


except Exception as e:
    print(f"Произошла ошибка: {e}")

