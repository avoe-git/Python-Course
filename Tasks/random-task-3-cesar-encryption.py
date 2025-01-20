from InquirerPy import inquirer
ascii=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def kodlama():
    a = input('Dekodlaşdırılmış sətir daxil edin: ')
    k = int(input('Kod əmsalınızı daxil edin: '))
    result = []
    for i in a:
        if i != ' ':
            if i == i.lower():
                result.append(ascii[(ascii.index(i)+k)%len(ascii)])
            else:
                i = i.lower()
                result.append(ascii[(ascii.index(i)+k)%len(ascii)].upper())
        else:
            result.append(' ')
    print('Kodlaşdırılmış nəticə: '+''.join(result))
def dekodlama():
    a = input('Kodlaşdırılmış sətir daxil edin: ')
    k = int(input('Kod əmsalınızı daxil edin: '))
    result = []
    for i in a:
        if i != ' ':
            if i == i.lower():
                result.append(ascii[(ascii.index(i)-k)%len(ascii)])
            else:
                i = i.lower()
                result.append(ascii[(ascii.index(i)-k)%len(ascii)].upper())
        else:
            result.append(' ')
    print('Dekodlaşdırılmış nəticə: '+''.join(result))

def main():
    # Define the options
    choices = [
        "Kodlaşdırma",
        "Dekodlaşdırma",
        "Çıxış - tətbiqin işini sonlandırın",
    ]

    # Prompt the user to select an option
    selection = inquirer.select(
        message="Sezar kodlama tətbiqinə xoş gəldiniz, funksiyayı seçin:",
        choices=choices,
        default="Kodlaşdırma",
        pointer="> ",
        instruction="(Klaviatura oxlarından istifadə edərək seçim edin)",
    ).execute()

    # Display the selected option
    if selection != "Çıxış - tətbiqin işini sonlandırın":
        if selection == "Kodlaşdırma":
            kodlama()
        elif selection == "Dekodlaşdırma":
            dekodlama()  
    else:
        print("Çıxış olunur... Təşəkkürlər!")

if __name__ == "__main__":
    main()
