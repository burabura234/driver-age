#    開車年齡問答
driver = input('請問你有駕照嗎? ')
age = input('請問你幾歲? ')
age = int(age)
if driver == '有':
  if age >= 18:
    print('回答正確')
  else:
    print('未成年會有駕照??@@騙肖!')
    
if driver == '沒有':
    if age >= 18:
        print('怎麼還不去考駕照?!!?!')
    else:
        print('時間還沒到，駕照考不到')