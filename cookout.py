import math

def main():
    HOT_DOGS_PER_PKG = 10
    BUNS_PER_PKG = 8

    num_people = int(input("Enter the number of people attending the cookout: "))
    hot_dogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))

    total_hot_dogs_needed = num_people * hot_dogs_per_person

    packages_of_dogs = math.ceil(total_hot_dogs_needed / HOT_DOGS_PER_PKG)
    packages_of_buns = math.ceil(total_hot_dogs_needed / BUNS_PER_PKG)

    leftover_dogs = (packages_of_dogs * HOT_DOGS_PER_PKG) - total_hot_dogs_needed
    leftover_buns = (packages_of_buns * BUNS_PER_PKG) - total_hot_dogs_needed

    print(f"Minimum packages of hot dogs required: {packages_of_dogs}")
    print(f"Minimum packages of hot dog buns required: {packages_of_buns}")
    print(f"Number of hot dogs that will be left over: {leftover_dogs}")
    print(f"Number of hot dog buns that will be left over: {leftover_buns}")

if __name__ == "__main__":
    main()