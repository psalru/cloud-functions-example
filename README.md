# Пример использования облачных функций

Данный репозиторий посвящён тому, как с использованием [облачных функций](https://cloud.yandex.ru/services/functions) в Я.Облаке можно генерировать отчёты. Для примера взяты данные по вакансиям университетов, [регулярно собираемые](https://psal.ru/docs/tools/airflow#dag-%D1%81%D0%BE%D0%B1%D0%B8%D1%80%D0%B0%D1%8E%D1%89%D0%B8%D0%B9-%D0%B2%D0%B0%D0%BA%D0%B0%D0%BD%D1%81%D0%B8%D0%B8-%D1%83%D0%BD%D0%B8%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82%D0%BE%D0%B2) в рамках проекта ПСАЛ.

Сгенерировать отчёт вы можете в [соответствующей вкладке](https://datalens.yandex/qv1g5xwqyzysg?tab=dw) 📊 дашборда в DataLens.

## Использования репозитория

* [func.py](https://gitflic.ru/project/psal/cloud-functions-example/blob?file=func.py&branch=master) — для облачной функции
* [cli.py](https://gitflic.ru/project/psal/cloud-functions-example/blob?file=cli.py&branch=master) — для работы из командной строки

Примеры вызова из командной строки для ВШЭ (ID университета 109):

```shell
python cli.py -i 109
```

Возможные параметры вызова через консоль

* `-h` или `--help` — подсказка 
* `--i` или `--id` (**обязательный**) — ID университета (можно посмотреть [здесь](https://datalens.yandex/qv1g5xwqyzysg?tab=dw))
* `-f` или `--folder` — папка куда сохранятся результаты работы (должна быть, по умолчанию `tmp`)
* `-w` или `--width` — размер генерируемых изображений (по умолчанию `13`)

