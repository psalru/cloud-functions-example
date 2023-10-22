from argparse import ArgumentParser
from generators import gen_report, gen_content

parser = ArgumentParser(
    prog='Отчёт по вакансиям на Cloud Functions',
    description='Пример генерализации отчёта по вакансиям университетов с использованием Cloud Functions Яндекс.Облака',
    epilog='Реализован в образовательных целях в рамках проекта https://psal.ru/.'
)

parser.add_argument('-i', '--id', type=int, required=True, help='ID университета.')
parser.add_argument('-f', '--folder', default='tmp', help='Папка, куда сохранится окончательный отчёт.')
parser.add_argument('-w', '--width', type=int, default=13, help='Ширина изображений чартов.')
parser.add_argument('-d', '--debug', action='store_true', help='Режим отладки. Если указан CLI показывает полный трек ошибок.')
args = parser.parse_args()

gen_report(vars(args))
gen_content(vars(args))
