years = {
  "明治":[1868, 1912],
  "大正":[1912, 1926],
  "昭和":[1926, 1989],
  "平成":[1989, 2019],
  "令和":[2019, 2022],
}
def convert_gengo():
  get_year = int(input('数値を入力：'))
  for k in years:
    if years[k][0] <= get_year < years[k][1]:
      gengo_year = get_year - years[k][0] + 1
      print(f'{k}{gengo_year}年')

convert_gengo()
