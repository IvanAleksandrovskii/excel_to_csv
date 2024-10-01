import os
import pandas as pd


def convert_excel_to_csv(input_folder, output_folder):
    # Создаем выходную папку, если она не существует
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Перебираем все файлы в папке input_folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.xlsx') or filename.endswith('.xls'):
            # Полный путь к входному файлу
            input_path = os.path.join(input_folder, filename)
            
            # Создаем имя выходного файла, заменяя расширение на .csv
            output_filename = os.path.splitext(filename)[0] + '.csv'
            output_path = os.path.join(output_folder, output_filename)
            
            # Читаем Excel файл
            df = pd.read_excel(input_path)
            
            # Сохраняем как CSV
            df.to_csv(output_path, index=False)
            
            print(f"Конвертирован {filename} в {output_filename}")

# Пути к папкам
input_folder = 'files_to_convert'
output_folder = 'converted_files'

if __name__ == '__main__':
    # Запускаем конвертацию
    convert_excel_to_csv(input_folder, output_folder)
