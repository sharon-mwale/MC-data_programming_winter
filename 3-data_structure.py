if __name__ == "__main__":
    names = ["Neria", "Ethel", "Mirriam", "Mwila"]
    names[3] = "Rody"
    print(names.sort())
    print(names[1])
    names.clear()
    setOfNums = (1,3,4, 10, 12)
    setOfNums.count(3)
    setOfNums.index(4)
    
    student = {
        "name": "Sharron",
        "age": 27
    }
    print(student["name"])
    student["favourite_color"] = "Black"

    print(student.keys)