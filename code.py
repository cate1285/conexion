import pandas as pd

def datos(cars):
  data_new=input("Quiere ingresar un nuevo dato? si/no")
  
  while data_new.lower() == "si" :
    for key, v in cars.items():
      enter_new_data=0
      if enter_new_data == 0:
        enter_new_data=input("ingrese dato para "+ key)
        if enter_new_data not in v:
          v.append(enter_new_data)
        else:
          print("El usuario ya esta registrado")
          break
    data_new=input("Quiere ingresar un nuevo dato? si/no")
  return cars

def convert_excel(total_data):
  df = pd.DataFrame(total_data, columns = ['nombre', 'apellidos',"compras"])
  print (df)
  # create excel writer object
  writer = pd.ExcelWriter('Datos_drive3.xlsx')
  # write dataframe to excel
  df.to_excel(writer)
  # save the excel
  writer.save()
  print('DataFrame is written successfully to Excel File.')



cars_data = {'nombre': ['Angela','Tito','Fufi','Angie'],
        'apellidos':["Martinez","Gonzales","Castaño","Roncancio"],
        'compras': [22000,25000,27000,35000]
        }

datos_recopilados=datos(cars_data)
convert_excel(datos_recopilados)