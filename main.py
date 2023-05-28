"LAB_12"
import tkinter as tk
print("--------------------------------------------------------------------------------------------------------------")
print("ЗАДАНИЕ 12.1", '\n')
def p1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

    class IceCreamStand(Restaurant):
      def __init__(self, restaurant_name, cuisine_type, flavors):
          super().__init__(restaurant_name, cuisine_type)
          self.flavors = flavors

      def display_flavors(self):
          print("Список доступных сортов мороженого:")
          for flavor in self.flavors:
              print("- " + flavor)

    #Создание экземпляра класса IceCreamStand и вызов метода display_flavors()
    ice_cream_stand = IceCreamStand("Мороженое на палочке", "Кафе-мороженное", ["Фисташковое", "Арахисовое", "Крем-брюле"])
    ice_cream_stand.display_flavors()
    print("----------------------------------------------------------------------------------------------------------")
    print("ЗАДАНИЕ 12.2", '\n')

    class IceCreamStand(Restaurant):
      def __init__(self, restaurant_name, cuisine_type, flavors, location, opening_hours):
          super().__init__(restaurant_name, cuisine_type)
          self.flavors = flavors
          self.location = location
          self.opening_hours = opening_hours

      def display_flavors(self):
          print("Список доступных сортов мороженого:")
          for flavor in self.flavors:
              print("- " + flavor)

      def add_flavor(self, new_flavor):
          self.flavors.append(new_flavor)
          print(f"Добавлен новый сорт мороженого: {new_flavor}")

      def remove_flavor(self, flavor):
          if flavor in self.flavors:
              self.flavors.remove(flavor)
              print(f"Сорт мороженого: {flavor} удален.")
          else:
              print(f"Сорт мороженого: {flavor} не найден.")

      def check_flavor_availability(self, flavor):
          if flavor in self.flavors:
              print(f"Сорт мороженого: {flavor} доступен.")
          else:
              print(f"Сорт мороженого: {flavor} недоступен.")

    ice_cream_stand = IceCreamStand("Мороженое на палочке", "Кафе-мороженное", ["Фисташковое", "Арахисовое", "Крем-брюле"], "Улица Красной Луны, 23", "8:00-21:00")
    ice_cream_stand.display_flavors()
    ice_cream_stand.add_flavor("Ванильное")
    ice_cream_stand.remove_flavor("Фисташковое")
    ice_cream_stand.remove_flavor("Банановое")
    ice_cream_stand.check_flavor_availability("Арахисовое")
    ice_cream_stand.check_flavor_availability("Шоколадное")
    print('\n')
    print('Адрес и время работы ресторана:')
    print(ice_cream_stand.location)
    print(ice_cream_stand.opening_hours)
    print("----------------------------------------------------------------------------------------------------------")

    print("ЗАДАНИЕ 12.3")
    class IceCreamStand:
      def __init__(self, flavors):
          self.flavors = flavors

          self.root = tk.Tk()
          self.root.title("Мороженое на палочке")

          self.flavors_label = tk.Label(self.root, text="Список доступных сортов мороженого:")
          self.flavors_label.pack()

          self.flavors_listbox = tk.Listbox(self.root)
          for flavor in self.flavors:
              self.flavors_listbox.insert(tk.END, flavor)
          self.flavors_listbox.pack()

          self.root.mainloop()

    print('Создание экземпляра класса IceCreamStand и запуск графического интерфейса')
    ice_cream_stand = IceCreamStand(["Фисташковое", "Арахисовое", "Крем-брюле"])

p1()
